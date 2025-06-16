from agent import ArbiXAgent
import time

agent = ArbiXAgent()

while True:
    result = agent.execute("Find arbitrage opportunities now")
    print(result)
    time.sleep(30)