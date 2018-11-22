import argparse
import multiprocessing as mp
import os

from boltons import iterutils

from open_patstat.utils.gcp import parallel_upload_gcs

parser = argparse.ArgumentParser()
parser.description = "Implements multi-processing on top of the gsutil parallel composite upload. Recommended for Mac " \
                     "users but might fail for others. See gsutil help for more on that. Ex: python " \
                     "mp_pcu_mp_pcu_gcs.py gs://cellar-patstat $PWD/data/ tls206"
parser.add_argument('bucket', help='The gcs destination bucket. Ex: gs://my_bucket.', type=str)
parser.add_argument('directory', help='Path to your local file. Ex: path/to/my/file.', type=str)
parser.add_argument('pattern',
                    help='Common pattern of the bigfiles that will be processed in parallel. Ex: if "bigfile" passed, '
                         '"bigfile_part01, bigfile_part02, etc" will be processed. Note: If you target only one file, '
                         'just input the full file name', type=str)
parser.add_argument('nb_process',
                    help='Upper bound on the number of processes that can be launched in parallel. Default value is '
                         'the number of cores on your machine.', nargs='?', default=mp.cpu_count(), type=int)
args = parser.parse_args()

list_bigfiles = [bigfile for bigfile in os.listdir(args.directory) if args.pattern in bigfile]

process_dict = {}
if __name__ == '__main__':
    for bigfile in list_bigfiles:
        process_dict[bigfile] = mp.Process(name=bigfile, target=parallel_upload_gcs,
                                           args=(args.directory + bigfile, args.bucket,))

# print(args)

for sublist_bigfiles in iterutils.chunked_iter(list_bigfiles, args.nb_process):
    for bigfile in sublist_bigfiles:
        process_dict[bigfile].start()
    for bigfile in sublist_bigfiles:
        process_dict[bigfile].join()
