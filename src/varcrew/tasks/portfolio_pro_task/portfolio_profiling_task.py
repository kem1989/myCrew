from crewai import Task
from varcrew.agents.portfolio_profiling import financial_analyst
from varcrew.tools.securities_classifier import securities_classifier_tool
from varcrew.tools.derivative_exposure import derivative_exposure_tool
from varcrew.tools.liquidity_evaluator import liquidity_evaluator_tool

securities_classifier_task = Task(
    description="Analyze the portfolio's instrument types using data: {portfolio_json}",
    expected_output="JSON with percentages for equity, fixed_income, derivatives, etc.",
    agent=financial_analyst,
    tools=[securities_classifier_tool]
    )
    
	
derivative_exposure_task = Task(
    description="Identify instruments of the portfolio data: {portfolio_json} with non-linear payoffs (e.g., options, convertible bonds)",
    expected_output="List of derivatives with tickers, types, and notionals",
    agent=financial_analyst,
    tools=[derivative_exposure_tool]
    )
    
liquidity_evaluator_task = Task(
    description="Evaluate liquidity of holdings of the portfolio data: {portfolio_json} based on trading volume and asset class",
    expected_output="Risk score (1-5) for liquidity, list of illiquid assets",
    agent=financial_analyst,
    tools=[liquidity_evaluator_tool]
    )