"""
Simulate execution and price path deviation
"""
import numpy as np
from impact_models import square_root_impact, temporary_impact, permanent_impact

def simulate_execution(order_size, adv, participation_rate, volatility, risk_aversion, steps=100):
    # Placeholder: Simulate price path with and without impact
    np.random.seed(42)
    dt = 1 / steps
    price = 100
    prices = [price]
    impacted_prices = [price]
    for i in range(steps):
        dW = np.random.normal(0, np.sqrt(dt))
        price += volatility * price * dW
        impact = square_root_impact(order_size, adv, volatility)
        impacted_price = prices[-1] + volatility * prices[-1] * dW - impact * dt
        prices.append(price)
        impacted_prices.append(impacted_price)
    return np.array(prices), np.array(impacted_prices)
