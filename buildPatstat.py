from google.cloud import bigquery

from open_patstat.utils.gcp import create_table, load_gcs_file
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
