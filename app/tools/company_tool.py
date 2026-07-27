from app.services.company_services import company_service
from langchain_core.tools import tool


@tool
def company_tool(ticker: str) -> dict:
    """
    Get general information about a company.

    Args:
        ticker: Stock ticker.

    Returns:
        Company information.
    """
    return company_service.get_company_info(ticker)