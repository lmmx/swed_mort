grep ';' UNdata_Export_20200913_131342392.txt | grep -vE "footnote|Unrevised data" | tr ';' '	' > UNdata_sweden_monthly_deaths_1980_2020.tsv
