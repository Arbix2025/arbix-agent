def execute_swap(opportunity):
    if opportunity.get("arbitrage_found"):
        print(f"Simulated Trade: Buying on {opportunity['buy_from']} and selling on {opportunity['sell_on']}")
        return {
            "status": "Simulated trade",
            "details": opportunity
        }
    return {"status": "No arbitrage opportunity"}