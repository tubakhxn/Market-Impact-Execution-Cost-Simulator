"""
Market Impact Models: Square-root, Temporary, Permanent
"""
import numpy as np

def square_root_impact(order_size, adv, volatility, impact_coeff=0.5):
    # Almgren-Chriss square-root model
    return impact_coeff * volatility * np.sqrt(order_size / adv)

def temporary_impact(order_size, adv, participation_rate, temp_coeff=0.1):
    return temp_coeff * (order_size / adv) ** 0.5 * participation_rate

def permanent_impact(order_size, adv, perm_coeff=0.05):
    return perm_coeff * (order_size / adv)
