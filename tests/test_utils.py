import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import pytest

from src.exist.utils import plot_box, plot_histogram


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "score": [10, 12, 14, 15, 18, 20, 22, 25, 27, 30],
            "group": ["A", "A", "B", "A", "B", "A", "B", "A", "B", "A"],
            "value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        }
    )


@pytest.mark.parametrize(
    "func, kwargs",
    [
        (plot_histogram, {"x": "score"}),
        (plot_histogram, {"x": "score", "bins": 6, "kde": False, "grid": True}),
        (plot_histogram, {"x": "score", "hue": "group", "title": "Score by group"}),
        (plot_box, {"x": "score"}),
        (plot_box, {"x": "group", "y": "score", "grid": False}),
        (plot_box, {"x": "group", "y": "value", "title": "Value by group"}),
    ],
    ids=[
        "hist_default",
        "hist_custom_bins",
        "hist_with_hue",
        "box_default",
        "box_group_vs_score",
        "box_group_vs_value",
    ],
)
def test_plotting_functions_do_not_raise(sample_df, func, kwargs):
    plt.close("all")

    func(data=sample_df, **kwargs)

    plt.close("all")
