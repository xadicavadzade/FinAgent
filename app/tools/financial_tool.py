from langchain_core.tools import tool

from app.services.financial_service import financial_service


@tool
def financial_tool(ticker: str) -> dict:
    """
    Get key financial metrics for a company.

    Args:
        ticker: Stock ticker (e.g. AAPL, MSFT, NVDA)

    Returns:
        Financial metrics.
    """
    return financial_service.get_key_metrics(ticker)