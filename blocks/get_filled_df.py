import pandas as pd
import os
import sys

sys.path.insert(0, os.getcwd())

from blocks.get_raw_df import get_raw_df


def fill_na(sub_df: pd.DataFrame) -> pd.DataFrame:
    sub_df = sub_df.drop_duplicates("date").set_index("date")
    sub_df = sub_df.reindex(pd.date_range(sub_df.index.min(),
                                          sub_df.index.max()))
    sub_df.index = sub_df.index.rename("date")
    sub_df.miss = sub_df.miss.fillna(1)
    sub_df.miss = sub_df.miss.astype(int)
    sub_df = sub_df.ffill().reset_index().set_index("id")
    sub_df.index = sub_df.index.astype(int)
    sub_df.category_id = sub_df.category_id.astype(int)
    return sub_df


def get_filled_df():
    df = get_raw_df()
    fill_df = df.groupby("site_link").apply(lambda x: fill_na(x),
                                            include_groups=False)
    return fill_df


if __name__ == "__main__":
    df = get_filled_df()
    print(df.tail())
