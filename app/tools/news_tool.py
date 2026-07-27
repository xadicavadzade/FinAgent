from langchain_core.tools import tool

from app.services.news_service import news_service

@tool
def news_tool(company: str) -> list:
    """
    Get the latest news about a company.

    Args:
        company: Company name (e.g. Apple, Tesla, Nvidia).
    """

    return news_service.get_company_news(company)