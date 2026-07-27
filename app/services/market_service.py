import yfinance as yf


class MarketService:

    INDEXES = {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "Dow Jones": "^DJI",
    }

    def get_market_overview(self):
        result = []

        for name, ticker in self.INDEXES.items():

            try:
                stock = yf.Ticker(ticker)

                history = stock.history(period="1mo").dropna()

                if len(history) < 2:
                    continue
                if history.empty:
                    continue

                current = history["Close"].iloc[-1]
                previous = history["Close"].iloc[-2]

                change = ((current - previous) / previous) * 100

                result.append({
                    "name": name,
                    "price": round(current, 2),
                    "change_percent": round(change, 2),
                })

            except Exception:
                continue

        return result


market_service = MarketService()