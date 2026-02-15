# 3D Market Impact Simulator
import streamlit as st
from impact_models import *
from execution_simulator import *
from visualization import *
from metrics import *


st.set_page_config(page_title="3D Market Impact Simulator", layout="wide", page_icon="💹", initial_sidebar_state="expanded")

# --- Sidebar: User Inputs ---
st.sidebar.title("Execution Parameters")
order_size = st.sidebar.number_input("Order Size", min_value=1, value=100000, step=1000, format="%d")
adv = st.sidebar.number_input("Average Daily Volume (ADV)", min_value=1, value=1000000, step=10000, format="%d")
participation_rate = st.sidebar.slider("Participation Rate (%)", min_value=1, max_value=100, value=10) / 100
volatility = st.sidebar.number_input("Volatility (daily, %)", min_value=0.01, value=2.0, step=0.01) / 100
risk_aversion = st.sidebar.slider("Risk Aversion", min_value=0, max_value=10, value=2)

# --- Main Title ---
st.markdown("""
<h1 style='color:#e0e0e0; font-size:2.8rem; font-weight:700; letter-spacing:1px;'>3D Market Impact Simulator</h1>
<span style='color:#aaa; font-size:1.1rem;'>Model institutional trade execution and visualize market impact in 3D</span>
""", unsafe_allow_html=True)

# --- Calculations ---
slippage = expected_slippage(order_size, adv, participation_rate, volatility)
cost = execution_cost(order_size, adv, participation_rate, volatility)
benchmark_price = 100.0
executed_price = benchmark_price + slippage
shortfall = implementation_shortfall(order_size, adv, participation_rate, volatility, benchmark_price, executed_price)
risk_cost = risk_adjusted_cost(cost, risk_aversion, volatility)

# --- 3D Surface Data ---
import numpy as np
order_sizes = np.linspace(0.01*adv, 0.5*adv, 30)
participation_rates = np.linspace(0.01, 1.0, 30)
slippage_matrix = np.zeros((len(participation_rates), len(order_sizes)))
for i, pr in enumerate(participation_rates):
	for j, os in enumerate(order_sizes):
		slippage_matrix[i, j] = expected_slippage(os, adv, pr, volatility)

# --- Layout ---
col1, col2 = st.columns([2, 1])
with col1:
	st.subheader("3D Slippage Surface")
	fig_surface = plot_3d_surface(order_sizes, participation_rates, slippage_matrix)
	st.plotly_chart(fig_surface, use_container_width=True)

with col2:
	st.subheader("Cost Breakdown")
	costs = {"Slippage": slippage, "Shortfall": shortfall, "Risk Adj.": risk_cost}
	fig_pie = plot_cost_breakdown(costs)
	st.plotly_chart(fig_pie, use_container_width=True)
	st.metric("Expected Slippage", f"{slippage:,.2f}")
	st.metric("Execution Cost", f"{cost:,.2f}")
	st.metric("Implementation Shortfall", f"{shortfall:,.2f}")
	st.metric("Risk-Adjusted Cost", f"{risk_cost:,.2f}")

# --- Animated Simulation ---
st.subheader("Price Path Simulation")
prices, impacted_prices = simulate_execution(order_size, adv, participation_rate, volatility, risk_aversion)
fig_anim = plot_price_animation(prices, impacted_prices)
st.plotly_chart(fig_anim, use_container_width=True)

# --- Heatmap ---
st.subheader("Impact Intensity Heatmap")
heatmap = slippage_matrix
fig_heat = plot_heatmap(heatmap, order_sizes, participation_rates, "Impact Intensity")
st.plotly_chart(fig_heat, use_container_width=True)

# --- Footer ---
st.markdown("""
<div style='text-align:center; color:#666; margin-top:2em;'>
<small>© 2026 3D Market Impact Simulator &mdash; Institutional Execution Analytics</small>
</div>
""", unsafe_allow_html=True)
