from game_sdk.worker import GameWorker
from functions.fetch_prices import fetch_prices
from functions.calculate_opportunity import calculate_opportunity
from functions.execute_swap import execute_swap

class ArbiXWorker(GameWorker):
    def __init__(self):
        super().__init__(name="ArbiXWorker")

    def run_function(self, function_name, input_data):
        if function_name == "fetch_prices":
            return fetch_prices(input_data)
        elif function_name == "calculate_opportunity":
            return calculate_opportunity(input_data)
        elif function_name == "execute_swap":
            return execute_swap(input_data)
        else:
            return {"error": "Function not found"}