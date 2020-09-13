from .data import dir_path as data_dir

swed_in_tsv = "UNdata_Export_20200913_125246907.txt"
swed_out_prefix = "UNdata_monthly_deaths_1980_2020_sweden"
swed_out_tsv = f"{swed_out_prefix}.tsv"
swed_footnotes_tsv = f"{swed_out_prefix}_footnotes.tsv"

with open(data_dir / swed_in_tsv, "r") as f:
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

    with open(data_dir / swed_out_tsv, "w") as f:
        f.write(main_tsv)

    with open(swed_footnotes_tsv, "w") as f:
        f.write(footnote_tsv)
