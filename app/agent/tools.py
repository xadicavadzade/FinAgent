from app.tools.market_data_tool import market_tool
from app.tools.company_tool import company_tool
from app.tools.stock_tool import stock_price_tool
from app.tools.financial_tool import financial_tool
from app.tools.news_tool import news_tool




TOOLS = [
    stock_price_tool,
    company_tool,
    financial_tool,
    news_tool,
    market_tool,
]