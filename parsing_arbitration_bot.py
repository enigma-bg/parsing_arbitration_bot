import requests

binance_url = f'https://api.binance.com/api/v3/ticker/price'
kucoin_url = f"https://api.kucoin.com/api/v1/market/allTickers"
headers = {
    "accept": "application/json, text/plain, */*"
}

coins = ["APT", "ETH", "SOL", "FTM", "TIA", "MAGIC"]

def get_price_binance(coins):
    response_binance = requests.get(binance_url)
    binance_price = {}
    if response_binance.status_code == 200:
        binance_data = response_binance.json()
        for coin in coins:
            symbol = f"{coin}USDT"
            for item in binance_data:
                if item['symbol'] == symbol:
                    binance_price[coin] = float(item['price'])
    return binance_price

def get_price_kucoin(coins):
    response_kucoin = requests.get(kucoin_url)
    kucoin_price = {}
    if response_kucoin.status_code == 200:
        kucoin_data = response_kucoin.json()['data']['ticker']
        for coin in coins:
            symbol = f"{coin}-USDT"
            for item in kucoin_data:
                if item['symbolName'] == symbol:
                    kucoin_price[coin] = float(item['last'])
    return kucoin_price

def arbitrage(binance_price, kucoin_price):
    user_diff = float(input("Введите минимальную разницу в цене: "))
    for coin in coins:
        binance_price = binance_prices.get(coin)
        kucoin_price = kucoin_prices.get(coin)
        if binance_price is not None and kucoin_price is not None:
            difference = abs(binance_price - kucoin_price)
            if difference >= user_diff:
                if binance_price < kucoin_price:
                    buy_price = binance_price
                    sell_price = kucoin_price
                    platform_buy = "Binance"
                    platform_sell = "Kucoin"
                else:
                    buy_price = kucoin_price
                    sell_price = binance_price
                    platform_buy = "Kucoin"
                    platform_sell = "Binance"

                profit = sell_price - buy_price
                print(f"Нашел спред на монете {coin} с {platform_buy} на {platform_sell}.")
                print(f"Покупка: ${buy_price}")
                print(f"Продажа: ${sell_price}")
                print(f"Профит: ${profit:.4f}\n")
            else:
                print(f"{coin}: Разница слишком мала({difference:.4}), требуется разница >={user_diff:.4}")

binance_prices = get_price_binance(coins)
kucoin_prices = get_price_kucoin(coins)
arbitrage(binance_prices, kucoin_prices)