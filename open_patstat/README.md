

# First words

The purpose of this package is to help disseminate Statistical Data on Patents (so called PatStat) by providing tools to
explore these data using Google Cloud Platform, a simple, yet powerful Big Data environment. This is a development release,
comments and remarks are most welcome. We also provide exploratory data analysis notebooks.

Basically, this library can be divided into 3 parts:

- Data loading from local to Google Cloud Storage: `mp_pcu_gcs.py` (command line). It implements a multiprocessing layer on top of the 
`parallel composite upload` from `gsutil`. This might well save you a lot of time. Read full documentation: `python mp_pcu_gcs.py --help`.
<font color=red>WARNING: non mac-users might be unable to run the parallel composite upload.</font>

- Project management for BigQuery: `buildPatstat.py`. Loads data from Google Cloud Storage and builds tables in you BigQuery
project. Note that we did not write it as a "build from scratch" so far (it might well be the case in future release). Users are thus kindly 
invited to adapt our code to their own needs. It is based on our `gcp` utils which are themselves built on top of the Google 
Cloud Python client API. Users planning to manage their BigQuery Project from the Python API could find this utils library useful.

- Exploratory analysis: `open_patstat.documentation` and `open_patstat.plots` respectively provide a short documentation 
for PatStat tables and variables and a library of plots that where found useful when exploring PatStat. The documentation was originally parsed from 
the official EPO Data Catalog - completeness is not guaranteed. Notebooks `tls*` provide practical examples of how they can be used together with exploratory 
data analysis.


# Install

```
cd path/to/open_patstat
pip install -e .
```

# Tree

```shell
.
├── LICENSE.txt
├── README.md
├── __init__.py
├── __pycache__
├── documentation
│   ├── __pycache__
│   └── shortdoc.py
├── patstat2016a_doc_api.pickle
├── plots.py
├── requirements.txt
├── setup.py
└── utils
    ├── __init__.py
    ├── __pycache__
    ├── gcp.py
    └── schema.py
```

# What next

This is a development release, everything remains to be made.  