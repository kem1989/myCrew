from crewai.tools import BaseTool
import json

class SecuritiesClassifier(BaseTool):
    name: str = "Securities Classifier Tool"
    description: str = "Processes nested dictionaries from JSON strings"

    def _run(self, portfolio_json: str) -> str:
        try:
            data = json.loads(portfolio_json)
            
            breakdown = {"equity": 0.0, "fixed_income": 0.0, "derivatives": 0.0}
            for entry in data.values():
                if entry["type"] in ["stock", "etf"]:
                    breakdown["equity"] += entry["notional"]
                elif entry["type"] in ["bond", "treasury"]:
                    breakdown["fixed_income"] += entry["notional"]
                elif entry["type"] in ["option", "future"]:
                    breakdown["derivatives"] += entry["notional"]

            total = sum(breakdown.values())
            return {k: round(v / total * 100, 2) if total != 0 else 0.0 for k, v in breakdown.items()}
        except Exception as e:
            return f"Error: {str(e)}"

securities_classifier_tool = SecuritiesClassifier()