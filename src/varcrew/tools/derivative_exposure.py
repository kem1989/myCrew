from crewai.tools import BaseTool
import json

class DerivativeExposure(BaseTool):
    name: str = "Derivative Exposure Tool"
    description: str = "Process the data and shows us the derivatives"

    def _run(self, portfolio_json: str) -> str:
        try:
            data = json.loads(portfolio_json)
            # Your processing logic here
            derivatives = []
            for ticker, entry in data.items():
                if entry["type"] in ["option", "swap", "warrant"]:
                    derivatives.append({
                        "ticker": ticker,
                        "type": entry["type"],
                        "notional": entry["notional"],
                        **{k: v for k, v in entry.items() if k not in ["type", "notional"]}
                    })
            return derivatives
        except Exception as e:
            return f"Error: {str(e)}"

derivative_exposure_tool = DerivativeExposure()