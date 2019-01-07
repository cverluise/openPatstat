import colorlover as cl
import pandas as pd
import plotly.graph_objs as go

"""
This library is built on top of Plotly (Plotly Technologies Inc.).
The goal is to streamline and standardize plots across the Pathora projects. 
"""


# NOTE: The two could me merged via **kwargs + handling of the case where there is no cluster


def bar_chart(series: pd.Series, colors: str = 'Blues', **kwargs):
    """
    Returns a bar chart from a pd.Series with:
        x-axis defined by the index
        y-values determined by the values

    Args:
        series: pd.Series
        colors: color-scale from the colorlover package. Argument should be taken from available
        token in cl.flipper()['seq']
        **kwargs: keyworded arguments that will be passed to go.Layout

    Returns: go.Figure object that can be displayed, saved, etc

    """
    tmp = series.copy()
    data = [go.Bar(
        x=tmp.index,
        y=tmp.values,
        marker=dict(color=cl.flipper()['seq']['3'][colors][-1])
    )]
    layout = go.Layout(**kwargs)
    return go.Figure(data, layout)


def stacked_bar_chart(df: pd.DataFrame, clusters: str, values: str,
                      colors: tuple = ('seq', 'Blues'), **kwargs):
    """
    Returns a stacked bar chart from a pd.DataFrame with:
        x-axis defined by the index
        stacks defined by the 'cluster' variable
        y-values determined by the 'values' variable

    Args:
        df: pd.DataFrame
        clusters: str specifying the clustering variable
        values: str specifying the values variable
        colors: color-scale from the colorlover package. Argument should be taken from available
        token in cl.flipper()['seq']
        **kwargs: keyworded arguments that will be passed yo go.Layout

    Returns: go.Figure object that can be displayed, saved, etc

    """
    tmp = df.copy()
    tmp = tmp.rename(columns={clusters: 'cluster'})

    cluster_list = tmp['cluster'].unique()
    if len(cluster_list) >= 3:
        nb_col = len(cluster_list)
    else:
        nb_col = 3

    data = []
    i = 0
    for clu in cluster_list:
        data += [
            go.Bar(
                x=tmp.query("cluster == @clu").index,
                y=tmp.query('cluster == @clu')[values].values,
                name=clu,
                marker=dict(color=cl.scales[str(nb_col)][colors[0]][colors[1]][i], ))
        ]
        i += 1
    layout = go.Layout(barmode='stack', **kwargs)
    return go.Figure(data=data, layout=layout)


def pie_chart(series: pd.Series, colors: tuple = ('div', 'RdYlBu'), **kwargs):
    """
    Returns a pie chart from a pd.Series with:
        labels defined by the index
        areas determined by the values

    Args:
        series:
        colors: color-scale from the colorlover package. Argument should be taken from available
        token in cl.flipper()['seq']
        **kwargs: keyworded arguments that will be passed yo go.Layout

    Returns: go.Figure object that can be displayed, saved, etc

    """
    tmp = series.copy()
    if len(tmp) >= 3:
        nb_col = len(tmp)
    else:
        nb_col = 3

    trace = go.Pie(labels=tmp.index, values=tmp.values,
                   marker=dict(colors=cl.scales[str(nb_col)][colors[0]][colors[1]], ))
    layout = go.Layout(barmode='stack', **kwargs)
    return go.Figure([trace], layout)


def line_chart(df: pd.DataFrame, colors: tuple = ('div', 'RdYlBu'), **kwargs):
    """

    Args:
        series: pd.Series
        colors: color-scale from the colorlover package. Argument should be taken from available
        token in cl.flipper()['seq']
        **kwargs: keyworded arguments that will be passed to go.Layout

    Returns: go.Figure object that can be displayed, saved, ect

    """
    tmp = df.copy()
    x = list(tmp.index)
    trace = []

    if len(tmp.columns) >= 3:
        nb_col = min(len(tmp.columns), 11)
        i = 0
    else:
        nb_col = 3
        i = -1

    for s in tmp.columns:
        trace += [go.Scatter(
            x=x,
            y=tmp[s].values,
            name=s,
            line=dict(color=cl.scales[str(nb_col)][colors[0]][colors[1]][i], )
        )]
        if i < 10:
            i += 1
        else:
            i = 0

    layout = go.Layout(**kwargs)

    return go.Figure(trace, layout)
