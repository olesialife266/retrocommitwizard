import random
import time
from datetime import datetime

COINS = ['BTC', 'ETH', 'SOL', 'XRP', 'ADA']

def get_fake_price():
    return round(random.uniform(10, 60000), 2)

def log_price(symbol):
    price = get_fake_price()
    timestamp = datetime.now().isoformat()
    line = f"{timestamp} - {symbol}: ${price}"
    with open("log.txt", "a") as f:
        f.write(line + "\n")
    print("Logged:", line)

def main():
    for _ in range(5):
        coin = random.choice(COINS)
        log_price(coin)
        time.sleep(1)

if __name__ == "__main__":
    main()
