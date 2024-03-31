import pandas as pd
import os
import sys
sys.path.insert(0, os.getcwd())

from utils.get_connection import get_connection

connection = get_connection()


def get_raw_df():
    df = pd.read_sql(sql="select * from ane_base.parser_app_pricesraw",
                     con=connection)
    return df


if __name__ == "__main__":
    df = get_raw_df()
    print(df.head())
