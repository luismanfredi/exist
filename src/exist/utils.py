import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_histogram(
    data: pd.DataFrame,
    x: str | pd.Series,
    y: str | None = None,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str = "Count",
    figsize: tuple = (8, 5),
    bins: str = "auto",
    hue: str | None = None,
    kde: bool = True,
    grid: bool = True,
) -> None:
    """Create and show a standart histogram from a column of a DataFrame.

    The function adjust automatically the labels, add a basic grid and display the graph with plt.show()

    Args:
        data (pd.DataFrame): The DataFrame with the data to be analyzed.
        x (str): The name of the column ultilized in the x axis.
        y (str, None): The name of the column ultilized in the y axis. Defaults to None.
        title (str, None): Title of the graph. If None, it generates an automatically in the "{x} distribution" format. Defaults to None.
        xlabel (str, None): Name of the x  axis label. If None, x will be used as the label name. defaults to None.
        ylabel (str): Name of the y axis label. Defaults to "Count".
        figsize (tuple): The size of the graph in 100px (e.g., figsize=(8, 5) means 800px-500px). Defaults to (8, 5).
        bins (str): Rule or quantity of bins in the histogram. Defaults to "auto".
        hue (str, None): Color-encoding a third variable. Defaults to None.
        kde (bool): A continuos line chart that shows the probability density of a continuos data variable. Defaults to True.
        grid (bool): If True it generates a basic grid. If False, does not generates a grid. Defaults to True.

    Returns:
        None

    Raises:
        KeyError: If the column "x" does not exist in the DataFrame.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'u': [1, 2, 2, 3, 4]})
        >>> plot_histogram(df, x='u', title='Ultraviolet')
    """

    plt.figure(figsize=figsize)

    sns.histplot(data=data, x=x, y=y, bins=bins, kde=kde, hue=hue)

    plt.title(title or f"{x.capitalize} distribution")

    if type(x) is str:
        plt.xlabel(xlabel or x.capitalize())

    plt.ylabel(ylabel)

    if grid:
        plt.grid(True, linestyle="--", alpha=0.6)

    plt.show()


def plot_box(
    data: pd.DataFrame,
    x: str,
    y: str | None = None,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str = "Count",
    figsize: tuple = (8, 5),
    grid: bool = True,
) -> None:
    """Create and show a standart boxplot from a column of a DataFrame.

    The function adjust automatically the labels, add a basic grid and display the graph with plt.show()

    Args:
        data (pd.DataFrame): The DataFrame with the data to be analyzed.
        x (str): The name of the column ultilized in the x axis.
        y (str, None): The name of the column ultilized in the y axis. Defaults to None.
        title (str, None): Title of the graph. If None, it generates an automatically in the "{x} distribution" format. Defaults to None.
        xlabel (str, None): Name of the x  axis label. If None, x will be used as the label name. Defaults to None.
        ylabel (str): Name of the y axis label. Defaults to "Count".
        figsize (tuple): The size of the graph in 100px (e.g., figsize=(8, 5) means 800px-500px). Defaults to (8, 5).
        grid (bool): If True it generates a basic grid. If False, does not generates a grid. Defaults to True.

    Returns:
        None

    Raises:
        KeyError: If the column "x" does not exist in the DataFrame.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'u': [1, 2, 2, 3, 4]})
        >>> plot_box(df, x='u', title='Ultraviolet')
    """

    plt.figure(figsize=figsize)

    sns.boxplot(data=data, x=x, y=y)

    plt.title(title or f"{x.capitalize} distribution")

    plt.xlabel(xlabel or x.capitalize())

    plt.ylabel(ylabel)

    if grid:
        plt.grid(True, linestyle="--", alpha=0.6)

    plt.show()
