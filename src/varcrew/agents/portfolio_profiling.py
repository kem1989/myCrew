from crewai import Agent
from varcrew.tools.securities_classifier import securities_classifier_tool

financial_analyst = Agent(
        role='Senior Portfolio Risk Analyst',
        goal='Analyze portfolio composition to identify instrument types, liquidity risks, and non-linear exposures',
        backstory="""A quantitative analyst specializing in dissecting portfolio structures for risk modeling""",
        tools=[securities_classifier_tool],
        verbose=True
    )

