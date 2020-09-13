from ..proc import mort_swed, pop_swed
from .fig import dir_path as fig_dir
from matplotlib import pyplot as plt
import pandas as pd

def scale_mort(mort_swed, pop_swed):
    pop_scaled_mort = pd.merge(mort_swed, pop_swed, on="Year").rename(columns={
        "Value_x": "Unscaled_deaths", "Value_y": "Pop"
    })
    pop_scaled_mort["Pop_per_mil"] = pop_scaled_mort.Pop / 1e6
    pop_scaled_mort["Scaled_deaths"] = pop_scaled_mort.Unscaled_deaths / pop_scaled_mort.Pop_per_mil
    return pop_scaled_mort

def plot_graph():
    dates_deaths = mort_swed[["ym_date", "Value"]].copy()
    plt.plot_date(mort_swed.ym_date, mort_swed.Value, linestyle="solid", marker=None)
    mv_avg = mort_swed.rolling(36, on="ym_date").Value.mean()
    pop_scaled_mort = scale_mort(mort_swed, pop_swed)
    plt.plot_date(mort_swed.ym_date, mv_avg, linestyle="dotted", color="purple", marker=None)
    plt.xlabel("Year")
    plt.ylabel("Deaths by month of death per million population (census/estimates via UN)")
    plt.show()

def save_graph():
    plt.rcParams['figure.figsize'] = 24, 12
    plt.tight_layout()
    dates_deaths = mort_swed[["ym_date", "Value"]].copy()
    plt.plot_date(mort_swed.ym_date, mort_swed.Value, linestyle="solid", marker=None)
    mv_avg = mort_swed.rolling(36, on="ym_date").Value.mean()
    pop_scaled_mort = scale_mort(mort_swed, pop_swed)
    plt.plot_date(mort_swed.ym_date, mv_avg, linestyle="dotted", color="purple", marker=None)
    plt.xlabel("Year")
    plt.ylabel("Deaths by month of death per million population (census/estimates via UN)")
    plt.savefig(fig_dir / "sweden_scaled_mortality_figure.png", bbox_inches="tight", dpi=200)
