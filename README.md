
# 3D Market Impact Simulator

## Developer / Creator: tubakhxn

A production-ready Streamlit app to model institutional trade execution and visualize market impact in 3D.

## Features
- Square-root, temporary, and permanent market impact models
- User controls for order size, ADV, participation rate, volatility, risk aversion
- 3D surface visualization of slippage
- Animated simulation of price path deviation
- Cost breakdown chart, impact heatmap, risk-adjusted cost
- Dark, institutional-grade UI

## Execution Theory
Institutional trading impacts market prices. The **square-root impact model** (Almgren-Chriss) suggests that market impact grows with the square root of order size relative to ADV. **Temporary impact** reflects short-term price moves from liquidity demand, while **permanent impact** reflects lasting price changes. **Implementation shortfall** measures the difference between the decision price and the final execution price, capturing both impact and opportunity cost.

## Tech Stack
- Streamlit
- NumPy, Pandas, SciPy
- Plotly

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run: `streamlit run app.py`

## How to Fork
1. Click the **Fork** button at the top right of the repository page on GitHub.
2. Clone your forked repository:
	```sh
	git clone https://github.com/your-username/3d-market-impact-simulator.git
	```
3. Install dependencies and start developing!

## File Structure
- `app.py`: Main Streamlit app
- `impact_models.py`: Market impact models
- `execution_simulator.py`: Execution and price simulation
- `visualization.py`: 3D/animated/heatmap visualizations
- `metrics.py`: Cost and risk metrics
