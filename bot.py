import ccxt

# إنشاء كائن للبورصة
exchange = ccxt.binance()

# جلب بيانات آخر سعر لزوج BTC/USDT
ticker = exchange.fetch_ticker('BTC/USDT')

# طباعة السعر الحالي
print(f"السعر الحالي للبيتكوين: {ticker['last']} USDT")
