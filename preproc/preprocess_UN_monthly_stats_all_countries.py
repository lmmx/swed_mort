from .data import dir_path as data_dir

all_countries_in_tsv = "UNdata_Export_20200913_131342392.txt"
all_countries_out_prefix = "UNdata_monthly_deaths_1980_2020_all_countries"
all_countries_out_tsv = f"{all_countries_out_prefix}.tsv"
all_countries_footnotes_tsv = f"{all_countries_out_prefix}_footnotes.tsv"

with open(data_dir / all_countries_in_tsv, "r") as f:
    lines = f.readlines()
    assert lines.count("\n") == 1, "Multiple blank lines: expected a single separator"

def semicolon_to_tab(tsv_lines):
    return [l.replace(";", "\t") for l in tsv_lines]

def main():
    """
    Process UN data files into TSVs
    """
    sep_line = lines.index("\n")
    main_tsv = "".join(semicolon_to_tab(lines[:sep_line]))
    footnote_tsv = "".join(semicolon_to_tab(lines[sep_line + 1:]))

    with open(data_dir / all_countries_out_tsv, "w") as f:
        f.write(main_tsv)

    with open(all_countries_footnotes_tsv, "w") as f:
        f.write(footnote_tsv)
