import datetime
import multiprocessing
import subprocess
import time
import warnings

import pandas as pd
from google.cloud import bigquery
from tqdm import tqdm


# TODO: USE ASSERT TO CONTROL OUTPUT
# TODO: ADD JOBS ANALYTICS WRAPPER
# TODO: ADD EXAMPLES
# TODO: think about adding **kwargs
# CHECK THAT EVERYTHING IS FINE

def create_dataset(client: bigquery.Client, dataset_id: str, location: str = 'EU',
                   description: str = "Creation date: {}".format(datetime.datetime.now())):
    """
    Creates a dataset with following referece project_id:dataset_id

    Args:
        client: BQ API client
        dataset_id: dataset to be created
        location: location of the dataset (default is Europe for legal reasons)
        description: description of the dataset (default is date oc creation)

    Returns:

    """
    # TODO: ADD CHECK OF EXISTENCE
    dataset_ref = client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = location
    dataset.description = description
    client.create_dataset(dataset)


def delete_dataset(client: bigquery.Client, dataset_id: str, delete_contents: bool = True, ):
    """
    Deletes dataset from the current project

    Args:
        client: BQ API client
        dataset_id: dataset to be deleted
        delete_contents: (default is True)

    Returns:
        deletes dataset

    """
    # TODO: ADD CHECK OF EXISTENCE
    dataset_ref = client.dataset(dataset_id)
    client.delete_dataset(dataset_ref, delete_contents)


def create_table(client: bigquery.Client, dataset_id: str, table_id: str, schema: list):
    """
    Creates a table according to the given schema in the specified project:dataset

    Args:
        client: BQ API client
        dataset_id: destination dataset
        table_id: table to be created
        schema: schema of the table to be created

    Returns:

    Examples:
        create_table(client, 'my_dataset', 'my_table', my_schema)
    """
    dataset_ref = client.dataset(dataset_id=dataset_id)
    tables_list = [t.table_id for t in list(client.list_tables(dataset_ref))]

    if table_id in tables_list:
        print("THIS TABLE ALREADY EXISTS IN {}:{}".format(client.project, dataset_id))
    else:
        table_ref = dataset_ref.table(table_id)
        client.create_table(bigquery.Table(table_ref, schema))


def delete_table(client: bigquery.Client, dataset_id: str, table_id: str):
    """
    Deletes the specified table in the given project:dataset

    Args:
        client: BQ API client
        dataset_id: destination dataset
        table_id: table to be deleted

    Returns:

    Examples:
        delete_table(client, 'my_dataset', 'my_table')
    """
    dataset_ref = client.dataset(dataset_id=dataset_id)
    tables_list = [t.table_id for t in list(client.list_tables(dataset_ref))]

    if table_id not in tables_list:
        print("THIS TABLE DOES NOT EXIST IN {}:{}".format(client.project, dataset_id))
    else:
        table_ref = dataset_ref.table(table_id)
        client.delete_table(table_ref)


def list_tables(client: bigquery.Client, dataset_id: str):
    """
    Lists the tables in project:dataset

    Args:
        client: BQ API client
        dataset_id: dataset to be inspected

    Returns:
        list

    Examples:
        list_tables(client, 'my_dataset')
    """
    dataset_ref = client.dataset(dataset_id)
    return [t.table_id for t in client.list_tables(dataset_ref)]


def list_datasets(client: bigquery.Client):
    """
    Lists the dataset in project

    Args:
        client: BQ API client (default project defined in you GOOGLE_APPLICATION_CREDENTIALS)

    Returns:
        list

    Examples:
        list_datasets(client)
    """
    return [d.dataset_id for d in list(client.list_datasets())]


def chunk_file(file_in: str, files_out: str, extension: str = '.txt', chunk_size: int = 100000):
    """
    Reads, divides and saves a large csv file in multiple smaller files

    Args:
        file_in: (path) of the file to be read
        files_out: pattern of the files to be created
        extension: extension of the files to be created (def: .txt)
        chunk_size: number of lines in each sub-file

    Returns:

    Alternative: use the unix split command (more efficient)
    ex: split -l 100000 myfile myfile_
    Best option: let gsutil magic operate
    ex: gsutil -o GSUtil:parallel_composite_upload_threshold=150M cp bigfile gs://your-bucket
    """
    warnings.warn("Switch to the unix split command (more efficient) split -l 100000 myfile myfile_ \
                  or let gsutil magic operate 'gsutil -o GSUtil:parallel_composite_upload_threshold=150M cp \
                  bigfile gs://your-bucket'", DeprecationWarning)
    i = 0
    for chunk in tqdm(pd.read_csv(file_in,
                                  index_col=0,
                                  chunksize=chunk_size)):
        i += 1
        chunk.to_csv('{}{}{}'.format(files_out, i, extension))


def load_local_file(client: bigquery.Client,
                    filename: str,
                    table_ref: bigquery.table.TableReference,
                    job_config: bigquery.LoadJobConfig,
                    # job_id: str = str(datetime.datetime.now()).replace(' ', ''),
                    ):
    """
    Args:
        client:
        filename:
        table_ref:
        job_config:

    Returns:

    Examples:

    """

    with open(filename, 'rb') as source_file:
        load_job = client.load_table_from_file(
            file_obj=source_file,
            destination=table_ref,
            # job_id=job_id,
            job_id_prefix='llf-',
            job_config=job_config)  # API request
    tic = time.time()
    print('Starting job {} at {}'.format(load_job.job_id, tic))
    load_job.result()
    print('Job took {} seconds'.format(time.time() - tic))
    assert load_job.state == 'DONE'


def parallel_upload_gcs(big_file: str,
                        destination_bucket: str):
    """
    Just a wrapper around the parallel composite upload from gsutil

    Args:
        big_file:
        destination_bucket:

    Returns:
    Parallel composite upload of big_file to destination bucket

    Ex:
    TODO: TEST THIS SNIPPET
    import multiprocessing
    import os
    from boltons import iterutils

    my_bucket = 'gs://cellar-patstat'
    data_path = 'data/'
    nbp = multiprocessing.cpu_count()

    list_bigfiles = os.listdir(data_path)
    regex = 'tls201'
    list_bigfiles = [bigfile for bigfile in list_bigfiles if regex in bigfile]

    process_dict = {}
    if __name__ == '__main__':
    for bigfile in list_bigfiles:
        print(bigfile)
        process_dict[bigfile] = multiprocessing.Process(name=bigfile,
                                                        target=parallel_upload,
                                                        args=(data_path + bigfile, my_bucket,))

    for sublist_bigfiles in iterutils.chunked_iter(list_bigfiles, nbp):
        for bigfile in sublist_bigfiles:
            process_dict[bigfile].start()
    """
    name = multiprocessing.current_process().name
    print(name, "starting")
    subprocess.call(["gsutil", "-o",
                     "GSUtil:parallel_composite_upload_threshold=150M",
                     "cp", big_file, destination_bucket])
    print(name, "exiting")


def load_gcs_file(client: bigquery.Client,
                  uri: str,
                  table_ref: bigquery.table.TableReference,
                  job_config: bigquery.LoadJobConfig,
                  # job_id: str = str(datetime.datetime.now()).replace(' ', ''),
                  ):
    """

    Args:
        client:
        uri:
        table_ref:
        job_config:
        job_id:

    Returns:

    Examples:

    """

    load_job = client.load_table_from_uri(
        source_uris=uri,
        destination=table_ref,
        # job_id=job_id,
        job_id_prefix='lgs-',
        job_config=job_config,
    )

    tic = time.time()
    print('Starting job {}'.format(load_job.job_id))
    load_job.result()
    print('Job took {} seconds'.format(time.time() - tic))
    assert load_job.state == 'DONE'
