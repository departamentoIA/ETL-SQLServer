# settings.py
"""This file uses the 'config.py' file."""
import pyodbc
import pandas as pd
import time
import math
import warnings
from pkg.config import DB_CONFIG

# Global variables ----------------------------------------

log_file = "LogFile.txt"
result_folder = "results"
table_list = ['CFDIS_2020']
MAX_ROWS_PER_TABLE = 600_000              # Maximum number of rows per excel file
# -------------------------------------------------------


# File to write some text
f = open(log_file, "w", encoding="utf-8")

conn_str = (
    f"DRIVER={DB_CONFIG['driver']};"
    f"SERVER={DB_CONFIG['server']};"
    f"DATABASE={DB_CONFIG['database']};"
    f"UID={DB_CONFIG['username']};"
    f"PWD={DB_CONFIG['password']};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

# To ignore all warnings
warnings.filterwarnings("ignore")
