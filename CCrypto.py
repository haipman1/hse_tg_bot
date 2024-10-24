from tradingview_ta import TA_Handler, Interval

def get_crypto_price(crypto_name):
    crypto = TA_Handler(
        symbol=crypto_name + "USDT",
        screener="crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_DAY,
        # proxies={'http': 'http://example.com:8080'}  # Uncomment to enable proxy (replace the URL).
    )
    return crypto.get_indicators()['close']