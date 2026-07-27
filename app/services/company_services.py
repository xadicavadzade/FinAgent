import yfinance as yf


SMA_SHORT = 20
SMA_LONG = 50
RSI_PERIOD = 14


class CompanyService:

    def _get_stock(self, symbol: str):
        return yf.Ticker(symbol.upper())

    def get_company_info(self, symbol: str):
        try:
            stock = self._get_stock(symbol)
            info = stock.info

            return {
                "symbol": symbol.upper(),
                "company": info.get("longName"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "country": info.get("country"),
                "website": info.get("website"),
                "market_cap": info.get("marketCap"),
            }

        except Exception as e:
            return {
                "error": f"Failed to fetch company information: {str(e)}"
            }

    def get_market_data(self, symbol: str):
        try:
            stock = self._get_stock(symbol)

            history = stock.history(period="3mo").dropna()

            if history.empty:
                return {
                    "error": f"No market data found for {symbol.upper()}"
                }

            close = history["Close"]

            current_price = round(close.iloc[-1], 2)

            sma20 = round(
                close.rolling(SMA_SHORT).mean().iloc[-1],
                2,
            )

            sma50 = round(
                close.rolling(SMA_LONG).mean().iloc[-1],
                2,
            )

            delta = close.diff()

            gain = delta.clip(lower=0)
            loss = -delta.clip(upper=0)

            avg_gain = gain.rolling(RSI_PERIOD).mean()
            avg_loss = loss.rolling(RSI_PERIOD).mean()

            rs = avg_gain / avg_loss

            rsi = round(
                (100 - (100 / (1 + rs))).iloc[-1],
                2,
            )

            trend = (
                "Bullish"
                if sma20 > sma50
                else "Bearish"
            )

            return {
                "symbol": symbol.upper(),
                "current_price": current_price,
                "sma20": sma20,
                "sma50": sma50,
                "rsi": rsi,
                "trend": trend,
            }

        except Exception as e:
            return {
                "error": f"Failed to fetch market data: {str(e)}"
            }


company_service = CompanyService()