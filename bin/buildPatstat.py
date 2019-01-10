from google.cloud import bigquery

from open_patstat.utils.gcp import create_table, load_gcs_file, delete_table
from open_patstat.utils.schema import Schema

client = bigquery.Client()

job_config = bigquery.LoadJobConfig()
job_config.skip_leading_rows = 1
job_config.max_bad_records = 10
job_config.source_format = bigquery.SourceFormat.CSV
dataset_ref = client.dataset('raw')

# Useful cli: bq show patstat2016a:raw.table (to check that the table has well been created and populated)

# # Create and populate tls207

create_table(client,
             dataset_id='raw',
             table_id='tls207',
             schema=Schema().tls207)

table_ref = dataset_ref.table('tls207')
job_config.schema = Schema().tls207
load_gcs_file(client, 'gs://cellar-patstat/tls207_*.txt', table_ref, job_config)

# # Create and populate tls206

create_table(client,
             dataset_id='raw',
             table_id='tls206',
             schema=Schema().tls206)

table_ref = dataset_ref.table('tls206')
job_config.schema = Schema().tls206
load_gcs_file(client, 'gs://cellar-patstat/tls206_*.txt', table_ref, job_config)

# # Create and populate tls209

create_table(client,
             dataset_id='raw',
             table_id='tls209',
             schema=Schema().tls209)

table_ref = dataset_ref.table('tls209')
job_config.schema = Schema().tls209
load_gcs_file(client, 'gs://cellar-patstat/tls209_*.txt', table_ref, job_config)

# # Create and populate tls224

create_table(client,
             dataset_id='raw',
             table_id='tls224',
             schema=Schema().tls224)

table_ref = dataset_ref.table('tls224')
job_config.schema = Schema().tls224
load_gcs_file(client, 'gs://cellar-patstat/tls224_*.txt', table_ref, job_config)

# # Create and populate tls202

create_table(client,
             dataset_id='raw',
             table_id='tls202',
             schema=Schema().tls202)

table_ref = dataset_ref.table('tls202')
job_config.schema = Schema().tls202
load_gcs_file(client, 'gs://cellar-patstat/tls202_part01.txt', table_ref, job_config)
load_gcs_file(client, 'gs://cellar-patstat/tls202_part02.txt', table_ref, job_config)
load_gcs_file(client, 'gs://cellar-patstat/tls202_part03.txt', table_ref, job_config)
# too many errors when loading all at once ie between 10 and 30 rows raise an issue

# # Create and populate tls202_wordcount

create_table(client,
             dataset_id='raw',
             table_id='tls2012_wordcount',
             schema=Schema().tls2012_wordcount)

table_ref = dataset_ref.table('tls2012_wordcount')
job_config.schema = Schema().tls2012_wordcount
job_config.null_marker = 'None'
load_gcs_file(client, 'gs://cellar-patstat/countWord/fullCW*.txt', table_ref, job_config)

