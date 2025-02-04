#!/usr/bin/env python
import sys
import warnings
from varcrew.crew import create_crew
from pydantic import BaseModel, ConfigDict
import json

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
# Create an agent

# Create a task

class PortfolioEntry(BaseModel):
    type: str
    notional: float
    model_config = ConfigDict(extra="allow")
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

portfolio_data = {
  "AAPL": {
    "type": "stock",
    "notional": 500000,
    "currency": "USD",
    "sector": "Technology",
    "region": "US",
    "price": 175.50,
    "volume": 2000000,
    "beta": 1.2
  },
  "TSLA_OPTION": {
    "type": "option",
    "notional": 200000,
    "currency": "USD",
    "underlying": "TSLA",
    "strike": 250,
    "expiry": "2024-06-21",
    "delta": 0.75,
    "volatility": 0.35
  },
  "US-TREASURY": {
    "type": "bond",
    "notional": 300000,
    "currency": "USD",
    "maturity": "2030-12-31",
    "coupon": 0.05,
    "credit_rating": "AA"
  }
}

data = {
    "user": {
        "name": "Alice Smith",
        "address": {
            "street": "456 Oak Rd",
            "city": "London",
            "postal_code": "SW1A 1AA"
        }
    }
}

def run():
    """
    Run the crew.
    """
    
    
    #validated_data = {k: PortfolioEntry(**v).dict() for k, v in portfolio_data.items()}
    #print("Now Validated data")
    #print(validated_data)
    json_data = json.dumps(portfolio_data)

# Create and run crew
    data_crew = create_crew()
    inputs = {"portfolio_json": json_data}
    results = data_crew.kickoff(inputs=inputs)

    print("\n\nFinal Results:")
    print(results)
    
    
   

'''
def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Varcrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Varcrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Varcrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
'''