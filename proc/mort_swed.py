from ..preproc import all_countries_out_prefix, swed_out_prefix
from ..preproc.data import dir_path as data_dir
import pandas as pd

def pd_tsv(tsv_path):
    return pd.read_csv(tsv_path, sep="\t")

def remove_non_months(df):
    df = df[((df.Month != "Total") & (df.Month != "Unknown"))]
    return df

def date_column_from_months(df):
    return df.apply(lambda x: pd.to_datetime(f"{x.Year} {x.Month}"), axis=1)

mort_swed = pd_tsv(data_dir / f"{swed_out_prefix}.tsv")
mort_swed["Value Footnotes"] = mort_swed["Value Footnotes"].convert_dtypes()
mort_swed.drop(["Record Type", "Reliability", "Area"], axis=1, inplace=True)
mort_swed = remove_non_months(mort_swed)
mort_swed["ym_date"] = date_column_from_months(mort_swed)
mort_swed = mort_swed.sort_values(by="ym_date")

fn_swed = pd_tsv(data_dir / f"{swed_out_prefix}_footnotes.tsv")

# There's some dodgy data entries so can't do for all countries without cleaning:

mort_all = pd_tsv(data_dir / f"{all_countries_out_prefix}.tsv")
mort_all.drop(["Record Type", "Reliability", "Area"], axis=1, inplace=True)
mort_all = remove_non_months(mort_all)
# mort_all = process_df_dates(mort_all)
# Dates not processed as they contain ranges of months!

fn_all = pd_tsv(data_dir / f"{all_countries_out_prefix}_footnotes.tsv")

