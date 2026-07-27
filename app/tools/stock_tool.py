from langchain_core.tools import tool
import yfinance as yf


@tool
def stock_price_tool(symbol: str) -> dict:
    """
    Get the latest stock price and daily change for a company.

    Args:
        symbol: Stock ticker symbol (e.g. AAPL, TSLA, NVDA)
    """

    stock = yf.Ticker(symbol.upper())

    info = stock.fast_info

    return {
        "symbol": symbol.upper(),
        "current_price": info.get("lastPrice"),
        "previous_close": info.get("previousClose"),
        "day_high": info.get("dayHigh"),
        "day_low": info.get("dayLow"),
        "volume": info.get("lastVolume"),
    }