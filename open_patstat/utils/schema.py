from google.cloud import bigquery

INT = 'INTEGER'
STR = 'STRING'
BOO = 'BOOLEAN'
FLO = 'FLOAT'
DAT = 'DATE'
GEO = 'GEOGRAPHY'

NULL = 'NULLABLE'
REQ = 'REQUIRED'


class Schema:
    """
    This class contains the schema of PatStat2016a tables
    TODO: CHECK SCHEMA
    """

    def __init__(self):
        self.tls201 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_auth', STR, NULL, None, ()),
            bigquery.SchemaField('appln_nr', STR, NULL, None, ()),  # detected as FLOAT
            bigquery.SchemaField('appln_kind', STR, NULL, None, ()),
            bigquery.SchemaField('appln_filing_date', DAT, NULL, None, ()),
            bigquery.SchemaField('appln_filing_year', INT, NULL, None, ()),
            bigquery.SchemaField('appln_nr_epodoc', STR, NULL, None, ()),
            bigquery.SchemaField('appln_nr_original', STR, NULL, None, ()),  # detected as FLOAT
            bigquery.SchemaField('ipr_type', STR, NULL, None, ()),
            bigquery.SchemaField('internat_appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('int_phase', BOO, NULL, None, ()),
            bigquery.SchemaField('reg_phase', BOO, NULL, None, ()),
            bigquery.SchemaField('nat_phase', BOO, NULL, None, ()),  # detected as STRING
            bigquery.SchemaField('earliest_filing_date', DAT, NULL, None, ()),
            bigquery.SchemaField('earliest_filing_year', INT, NULL, None, ()),
            bigquery.SchemaField('earliest_filing_id', INT, NULL, None, ()),
            bigquery.SchemaField('earliest_publn_date', DAT, NULL, None, ()),
            bigquery.SchemaField('earliest_publn_year', INT, NULL, None, ()),
            bigquery.SchemaField('earliest_pat_publn_id', INT, NULL, None, ()),
            bigquery.SchemaField('granted', BOO, NULL, None, ()),  # detected as STRING
            bigquery.SchemaField('docdb_family_id', INT, NULL, None, ()),
            bigquery.SchemaField('inpadoc_family_id', INT, NULL, None, ()),
            bigquery.SchemaField('docdb_family_size', INT, NULL, None, ()),
            bigquery.SchemaField('nb_citing_docdb_fam', INT, NULL, None, ()),
            bigquery.SchemaField('nb_applicants', INT, NULL, None, ()),
            bigquery.SchemaField('nb_inventors', INT, NULL, None, ())
        ]
        self.tls207 = [
            bigquery.SchemaField('person_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('applt_seq_nr', INT, NULL, None, ()),
            bigquery.SchemaField('invt_seq_nr', INT, NULL, None, ())
        ]
        self.tls206 = [
            bigquery.SchemaField('person_id', INT, REQ, None, ()),
            bigquery.SchemaField('person_name', STR, NULL, None, ()),
            bigquery.SchemaField('person_address', STR, NULL, None, ()),
            bigquery.SchemaField('person_ctry_code', STR, NULL, None, ()),
            bigquery.SchemaField('doc_std_name_id', INT, NULL, None, ()),
            bigquery.SchemaField('doc_std_name', STR, NULL, None, ()),
            bigquery.SchemaField('psn_id', INT, NULL, None, ()),  # check STR
            bigquery.SchemaField('psn_name', STR, NULL, None, ()),
            bigquery.SchemaField('psn_level', INT, NULL, None, ()),  # check STR
            bigquery.SchemaField('psn_sector', STR, NULL, None, ()),  # check STR
            # bigquery.SchemaField('han_id', INT, NULL, None, ()),  # check STR
            # bigquery.SchemaField('han_name', STR, NULL, None, ()),
            # bigquery.SchemaField('han_harmonized', STR, NULL, None, ())
        ]
        self.tls209 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('ipc_class_symbol', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_class_level', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_version', DAT, NULL, None, ()),
            bigquery.SchemaField('ipc_value', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_position', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_gener_auth', STR, NULL, None, ())
        ]
        self.tls224 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('cpc_class_symbol', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_scheme', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_version', DAT, NULL, None, ()),
            bigquery.SchemaField('cpc_value', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_position', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_gener_auth', STR, NULL, None, ()),
        ]
        self.tls202 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_title_lg', STR, NULL, None, ()),
            bigquery.SchemaField('appln_title', STR, NULL, None, ()),
        ]
        self.tls2012_wordcount = [
            bigquery.SchemaField('appln_title_lg', STR, NULL, None, ()),
            bigquery.SchemaField('appln_auth', STR, NULL, None, ()),
            bigquery.SchemaField('year', INT, NULL, None, (), ),
            bigquery.SchemaField('word', STR, NULL, None, ()),
            bigquery.SchemaField('count', INT, NULL, None, ()),
        ]
        self.inv_geo = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('patent_office', STR, NULL, None, ()),
            bigquery.SchemaField('priority_date', DAT, NULL, None, ()),
            bigquery.SchemaField('name_0', STR, NULL, None, ()),
            bigquery.SchemaField('name_1', STR, NULL, None, ()),
            bigquery.SchemaField('name_2', STR, NULL, None, ()),
            bigquery.SchemaField('name_3', STR, NULL, None, ()),
            bigquery.SchemaField('name_4', STR, NULL, None, ()),
            bigquery.SchemaField('name_5', STR, NULL, None, ()),
            bigquery.SchemaField('city', STR, NULL, None, ()),
            bigquery.SchemaField('lat', FLO, NULL, None, ()),
            bigquery.SchemaField('lng', FLO, NULL, None, ()),
            bigquery.SchemaField('data_source', STR, NULL, None, ()),
            bigquery.SchemaField('coord_source', STR, NULL, None, ()),
            bigquery.SchemaField('source', INT, NULL, None, ()),
            bigquery.SchemaField('priority_year', INT, NULL, None, ())
        ]
        self.app_geo = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('patent_office', STR, NULL, None, ()),
            bigquery.SchemaField('priority_date', DAT, NULL, None, ()),
            bigquery.SchemaField('name_0', STR, NULL, None, ()),
            bigquery.SchemaField('name_1', STR, NULL, None, ()),
            bigquery.SchemaField('name_2', STR, NULL, None, ()),
            bigquery.SchemaField('name_3', STR, NULL, None, ()),
            bigquery.SchemaField('name_4', STR, NULL, None, ()),
            bigquery.SchemaField('name_5', STR, NULL, None, ()),
            bigquery.SchemaField('city', STR, NULL, None, ()),
            bigquery.SchemaField('lat', FLO, NULL, None, ()),
            bigquery.SchemaField('lng', FLO, NULL, None, ()),
            bigquery.SchemaField('data_source', STR, NULL, None, ()),
            bigquery.SchemaField('coord_source', STR, NULL, None, ()),
            bigquery.SchemaField('source', INT, NULL, None, ()),
            bigquery.SchemaField('priority_year', INT, NULL, None, ())
        ]
        self.date_utils = [
            bigquery.SchemaField('date', DAT, NULL, None, ()),
            bigquery.SchemaField('year', INT, NULL, None, ())
        ]
