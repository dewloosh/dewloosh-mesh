# -*- coding: utf-8 -*-
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from ...explode import explode_mesh


__all__ = ['plot_lines_3d']


def _scatter_lines_3d(fig, coords, topo, *args, **kwargs):
    # this only works if all the lines form a continuous path
    # in a way, that the first node of the lext line always
    # coincides with the end node of the previous line
    X, _ = explode_mesh(coords, topo)
    x = X[:, 0]
    y = X[:, 1]
    z = X[:, 2]
    scatter_cells = go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        line=dict(
            color='black',
            width=4
        ),
        showlegend=False
    )
    scatter_cells.update(hoverinfo='skip')
    fig.add_trace(scatter_cells)


def _stack_lines_3d(fig, coords, topo, *args, **kwargs):
    X, _ = explode_mesh(coords, topo)
    x = X[:, 0]
    y = X[:, 1]
    z = X[:, 2]

    def _stack_line_3d(i):
        scatter_cells = go.Scatter3d(
            x=x[2*i: 2*(i+1)],
            y=y[2*i: 2*(i+1)],
            z=z[2*i: 2*(i+1)],
            mode='lines',
            line=dict(
                color='black',
                width=4
            ),
            showlegend=False
        )
        scatter_cells.update(hoverinfo='skip')
        fig.add_trace(scatter_cells)
    list(map(_stack_line_3d, range(topo.shape[0])))


def _scatter_points_3d(coords, *args, dofsol=None,
                       case=0, markersize=1, **kwargs):
    x = coords[:, 0]
    y = coords[:, 1]
    z = coords[:, 2]
    if dofsol is not None:
        u = dofsol[:, 0, case]
        v = dofsol[:, 1, case]
        w = dofsol[:, 2, case]
    dfdata = {'x': x, 'y': y, 'z': z,
              'size': np.full(len(x), markersize),
              'symbol': np.full(len(x), 4),
              'id': np.arange(1, len(x)+1)}
    hover_data = ["x", "y", "z"]
    if dofsol is not None:
        hover_data = ["u", "v", "w"]
        dfdata.update(u=u, v=v, w=w)
    custom_data = ['u', 'v', 'w'] if dofsol is not None else None
    df = pd.DataFrame.from_dict(dfdata)
    fig = px.scatter_3d(
        df,
        x='x', y='y', z='z',
        hover_name="id",
        hover_data=hover_data,
        size='size',
        text="id",
        custom_data=custom_data,
    )
    if dofsol is not None:
        fig.update_traces(
            hovertemplate="<br>".join([
                "u: %{customdata[0]:.4e}",
                "v: %{customdata[1]:.4e}",
                "w: %{customdata[2]:.4e}",
            ]))
    else:
        fig.update_traces(
            hovertemplate="<br>".join([
                "x: %{x}",
                "y: %{y}",
                "z: %{z}",
            ]))
    return fig


def plot_lines_3d(coords, topo, *args, dofsol=None, **kwargs):

    n2 = topo[:, [0, -1]].max() + 1
    _dofsol = dofsol[:n2] if dofsol is not None else None
    fig = _scatter_points_3d(coords[:n2], *args, dofsol=_dofsol, **kwargs)

    for i, _ in enumerate(fig.data):
        #fig.data[i].marker.symbol = 'diamond'
        fig.data[i].marker.size = 5

    _stack_lines_3d(fig, coords, topo)

    fig.update_layout(
        template="plotly",
        autosize=True,
        # width=720,
        # height=250,
        margin=dict(l=1, r=1, b=1, t=1, pad=0),
        scene=dict(
            aspectmode='data',
            #xaxis = dict(nticks=5, range=[xmin - delta, xmax + delta],),
            #yaxis = dict(nticks=5, range=[ymin - delta, ymax + delta],),
            #zaxis = dict(nticks=5, range=[zmin - delta, zmax + delta],),
        )
    )

    return fig
