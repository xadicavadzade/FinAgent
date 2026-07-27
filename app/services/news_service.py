from gnews import GNews


class NewsService:

    def __init__(self):
        self.google_news = GNews(language="en", country="US")

    def get_company_news(self, company: str, max_results: int = 5):
        try:
            news = self.google_news.get_news(company)

            return news[:max_results]

        except Exception as e:
            return {
                "error": str(e)
            }
        
    def get_latest_news(self):
        return self.google_news.get_news("Stock Market")

news_service = NewsService()