import yfinance as yf


class FinancialService:

    def get_key_metrics(self, ticker: str):

        stock = yf.Ticker(ticker)

        info = stock.info

        return {
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "eps": info.get("trailingEps"),
            "revenue": info.get("totalRevenue"),
            "beta": info.get("beta"),
            "dividend_yield": info.get("dividendYield"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
            "current_price": info.get("currentPrice"),
            "currency": info.get("currency"),
        }


financial_service = FinancialService()