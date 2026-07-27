from app.services.market_service import market_service
from app.services.news_service import news_service


class DashboardService:

    def get_dashboard(self):
        return {
            "market_overview": market_service.get_market_overview(),
            "latest_news": news_service.get_latest_news(),

        }


dashboard_service = DashboardService()