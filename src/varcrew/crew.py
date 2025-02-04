from crewai import Crew, Process
from varcrew.agents.portfolio_profiling import financial_analyst
from varcrew.tasks.portfolio_pro_task.portfolio_profiling_task import securities_classifier_task, derivative_exposure_task, liquidity_evaluator_task


def create_crew():
    return Crew(
        agents=[financial_analyst],
        tasks=[securities_classifier_task, derivative_exposure_task, liquidity_evaluator_task],
        process=Process.sequential,
        verbose=True
    )