import re
import feedparser

google_rss = 'https://news.google.com/rss?hl=en-CA&gl=CA&ceid=CA:en'
cbc_rss = 'https://www.cbc.ca/cmlink/rss-canada'
ctv_rss = 'https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009'
reddit_rss = 'https://www.reddit.com/r/worldnews/.rss'


def parse_news(trend) -> []:
    """Parse rss feeds for news relating to a specififc trend

    ref: http://gewhere.github.io/feedparser-python
    """
    rss_query_rss = f"https://www.reddit.com/subreddits/search.rss?q={trend}"

    rssfeed_links = [google_rss, cbc_rss, ctv_rss, reddit_rss, rss_query_rss]
    regex = ""

    for letter in trend:
        if (letter == " "):
            regex = regex + "|"
        else:
            regex = regex + letter

    regex = re.compile(regex)

    results = []

    for link in rssfeed_links:
        d = feedparser.parse(link)

        # read one RSS entry at a time
        for entry in d.entries:
            search_results = {}
            try:
                title = re.search(regex, entry.title)
                summary = re.search(regex, entry.summary)
                matched_link = re.search(regex, entry.link)
            except:
                pass
            if ((title != None) | (summary != None) | (matched_link != None)):
                search_results["title"] = entry.title
                search_results["summary"] = entry.title
                search_results["link"] = entry.link
                search_results["from"] = link
                results.append(search_results)

    return results
