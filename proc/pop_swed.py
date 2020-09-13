from ..preproc import swed_pop_out_prefix
from ..preproc.data import dir_path as data_dir
import pandas as pd

def pd_tsv(tsv_path):
    return pd.read_csv(tsv_path, sep="\t")

def remove_non_sum_ages_areas_sexes(df):
    return df[((df.Age == "Total") & (df.Area == "Total") & (df.Sex == "Both Sexes"))]

pop_swed = pd_tsv(data_dir / f"{swed_pop_out_prefix}.tsv")
pop_swed.drop(["Reliability", "Source Year"], axis=1, inplace=True)
pop_swed = remove_non_sum_ages_areas_sexes(pop_swed)
pop_swed.Value = pop_swed.Value.astype(int)
pop_swed = pop_swed.sort_values(by="Year")
# As there are multiple estimates and census figures, but they're all pretty similar
# just group the 2 or 3 values each year and take the mean as an integer
pop_swed_avg = pop_swed.groupby("Year").mean().astype(int)
# Lastly to extend to 2020, let's increment by the same as last year incremented
new_value = int(pop_swed_avg.Value[2019] + pop_swed_avg.diff().Value[2019])
new_year = pd.DataFrame.from_dict({"Year": [2020], "Value": [new_value]})
new_year = new_year.set_index("Year")
pop_swed_avg = pop_swed_avg.append(new_year)

fn_pop_swed = pd_tsv(data_dir / f"{swed_pop_out_prefix}_footnotes.tsv")

# Omitting the rest of the countries for now
