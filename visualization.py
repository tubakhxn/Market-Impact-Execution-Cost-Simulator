"""
Visualization utilities: 3D surface, animation, heatmap, charts
"""
import plotly.graph_objs as go
import numpy as np
import pandas as pd

def plot_3d_surface(order_sizes, participation_rates, slippage_matrix):
    fig = go.Figure(data=[go.Surface(z=slippage_matrix, x=order_sizes, y=participation_rates, colorscale='Viridis')])
    fig.update_layout(scene=dict(
        xaxis_title='Order Size',
        yaxis_title='Participation Rate',
        zaxis_title='Slippage',
        bgcolor='#181818'),
        template='plotly_dark', margin=dict(l=0, r=0, b=0, t=40))
    return fig

def plot_price_animation(prices, impacted_prices):
    # Placeholder for animated price path
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=prices, mode='lines', name='No Impact'))
    fig.add_trace(go.Scatter(y=impacted_prices, mode='lines', name='With Impact'))
    fig.update_layout(template='plotly_dark', xaxis_title='Step', yaxis_title='Price',
                      legend=dict(bgcolor='#222', font_color='white'))
    return fig

def plot_cost_breakdown(costs):
    fig = go.Figure(data=[go.Pie(labels=list(costs.keys()), values=list(costs.values()), hole=0.4)])
    fig.update_layout(template='plotly_dark', legend=dict(bgcolor='#222', font_color='white'))
    return fig

def plot_heatmap(data, x, y, zlabel):
    fig = go.Figure(data=go.Heatmap(z=data, x=x, y=y, colorscale='Inferno'))
    fig.update_layout(template='plotly_dark', xaxis_title=x, yaxis_title=y, margin=dict(l=0, r=0, b=0, t=40))
    return fig
