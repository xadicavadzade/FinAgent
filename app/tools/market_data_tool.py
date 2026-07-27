from langchain_core.tools import tool
from app.services.company_services import company_service



@tool
def market_tool(symbol: str) -> dict:
    """
    Get current market data and technical indicators for a stock.

    Args:
        symbol: Stock ticker symbol (e.g. AAPL, TSLA, NVDA)
    """

    return company_service.get_market_data(symbol)