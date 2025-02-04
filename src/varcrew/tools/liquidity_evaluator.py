from crewai.tools import BaseTool
import json

class Liquidity_Evaluator(BaseTool):
    name: str = "Liquidity Evaluator Tool"
    description: str = "Processes data and evaluates liquidity risk"

    def _run(self, portfolio_json: str) -> str:
        try:
            data = json.loads(portfolio_json)
            illiquid_assets = [
                ticker for ticker, details in data.items() 
                if details.get("volume", 0) < 1e6
            ]
            risk_score = min(len(illiquid_assets), 5)
            return json.dumps({"score": risk_score, "illiquid_assets": illiquid_assets})
        except Exception as e:
            return json.dumps({"error": str(e)})

liquidity_evaluator_tool = Liquidity_Evaluator()
