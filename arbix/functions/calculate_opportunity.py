def calculate_opportunity(prices):
    uniswap = prices["ETH_USDC_Uniswap"]
    camelot = prices["ETH_USDC_Camelot"]

    if camelot > uniswap * 1.01:
        return {
            "arbitrage_found": True,
            "buy_from": "Uniswap",
            "sell_on": "Camelot",
            "expected_profit": camelot - uniswap
        }
    else:
        return {"arbitrage_found": False}