from game_sdk.agent import GameAgent

class ArbiXAgent(GameAgent):
    def __init__(self):
        super().__init__(name="ArbiX")
        self.description = "An autonomous DeFi arbitrage agent"

    def plan(self, goal, memory):
        return [
            {"function": "fetch_prices"},
            {"function": "calculate_opportunity"},
            {"function": "execute_swap"}
        ]