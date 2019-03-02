import twitter_trends
import news_parser

trends = twitter_trends.get_twitter_trends()

results = []

for trend in trends:
    news = news_parser.parse_news(trend.lower())

    if (news):
        print(f"\n{trend} \n=========\n")
        for new in news:
            print(f'{new["title"]} link: {new["link"]}')
