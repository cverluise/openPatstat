import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
from datetime import datetime
import stop_words
import string

"""
This is a Beam Python SDK count word adapted to patstat2016a
    - input     BQ:'patstat2016a.raw.tls2012_cp'
    - output    'gs://cellar-patstat/countWord/fullCW*.txt'

"""


def get_time():
    """
    Returns the date "yyyymmddhhmmss" (str)
    """
    return ''.join(str(t) for t in datetime.now().timetuple()[:-2])


def formatPairTitle(line):
    """
    Gets a BQ dict {'appln_title_lg:'en', year:2010, ...} and returns a KV tuple 
    ((appln_title_lg, appln_auth, year), appln_title)

    :param line: dict
    :return: tuple
    """
    import string  # for remote machines (not sure it is required)
    return ((line['appln_title_lg'], line['appln_auth'], line['year']),
            line['appln_title'].encode('utf-8').translate(None, string.punctuation).lower())


class SplitAndPairWithKey(beam.DoFn):
    """
    Gets a KV tuple of the form ((appln_title_lg, appln_auth, year), appln_title) and returns a 
    Pcoll
    KV tuple of the form ((appln_title_lg, appln_auth, year, word), 1)
    :return: tuple
    """

    def process(self, pair):
        for word in pair[1].split(' '):
            yield ((pair[0] + (word,)), 1)


def filterStopWords(word):
    """
    Filters out (english) stop words
    :param word: str
    :return: bool 
    """
    import stop_words  # for remote machines (not sure it is required)
    sw = stop_words.get_stop_words("en")
    return word not in sw


def formatCSV(pair):
    """
    Formats the KV tuple ((K1, K2, ...), V) in a csv formatted string 'K1, K2, ..., V' 
    :param pair: tuple
    :return: str 
    """
    return ', '.join(str(p) for p in (pair[0] + (pair[1],)))


PROJECT = 'patstat2016a'
BUCKET = 'gs://cellar-patstat'


def run():
    argv = [
        '--project={0}'.format(PROJECT),
        '--job_name={}'.format('wcount' + get_time()),
        '--save_main_session',
        '--region=europe-west1',
        '--requirements_file=requirements.txt',
        '--staging_location={}/staging/'.format(BUCKET),
        '--temp_location={}/staging/'.format(BUCKET),
        '--runner=DataflowRunner'
    ]

    p = beam.Pipeline(argv=argv)  # sys.argv
    # input = ''
    table_spec = bigquery.TableReference(
        projectId='patstat2016a',
        datasetId='raw',
        tableId='tls2012_cp')
    output_prefix = '{}/countWord/fullCW'.format(BUCKET)

    query = 'SELECT\
            appln_title_lg,\
            appln_title,\
            appln_auth,\
            year\
            FROM\
            `patstat2016a.raw.tls2012_cp`\
            WHERE\
            appln_title_lg="en"'

    (p
     | 'ReadTable' >> beam.io.Read(
                beam.io.BigQuerySource(query=query, use_standard_sql=True))  # more efficient
     # |'ReadTable' >> beam.io.Read(beam.io.BigQuerySource(table_spec))        
     # |'FilterLg' >> beam.Filter(lambda line: line['appln_title_lg']=='en')  
     | 'FormatPairTitle' >> beam.Map(lambda line: formatPairTitle(line))
     | 'FormatPairWord' >> beam.ParDo(SplitAndPairWithKey())
     | 'GroupAndSum' >> beam.CombinePerKey(sum)
     | 'FilterSW' >> beam.Filter(lambda (w, c): filterStopWords(w[-1]))
     | 'FormatCSV' >> beam.Map(lambda pair: formatCSV(pair))
     | 'Write' >> beam.io.WriteToText(output_prefix, file_name_suffix='.txt')
     )

    p.run()


if __name__ == '__main__':
    run()  # p.run().wait_until_finish()
