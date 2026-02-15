"""
Metrics calculations: slippage, execution cost, implementation shortfall, risk-adjusted cost
"""
import numpy as np
from impact_models import square_root_impact, temporary_impact, permanent_impact

def expected_slippage(order_size, adv, participation_rate, volatility):
    return square_root_impact(order_size, adv, volatility) + temporary_impact(order_size, adv, participation_rate)

def execution_cost(order_size, adv, participation_rate, volatility):
    return expected_slippage(order_size, adv, participation_rate, volatility) * order_size

def implementation_shortfall(order_size, adv, participation_rate, volatility, benchmark_price, executed_price):
    return (executed_price - benchmark_price) * order_size

def risk_adjusted_cost(cost, risk_aversion, volatility):
    return cost + risk_aversion * volatility
