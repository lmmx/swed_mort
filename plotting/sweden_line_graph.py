from ..proc import mort_swed
from matplotlib import pyplot as plt

def plot_graph():
    dates_deaths = mort_swed[["ym_date", "Value"]].copy()
    plt.plot_date(mort_swed.ym_date, mort_swed.Value, linestyle="solid", marker=None)
    mv_avg = mort_swed.rolling(36, on="ym_date").Value.mean()
    plt.plot_date(mort_swed.ym_date, mv_avg, linestyle="dotted", color="purple", marker=None)
    plt.xlabel("Year")
    plt.ylabel("Deaths by month of death")
    plt.show()
