import re
import requests

class NarrativeCrawler:
    def __init__(self):
        self.sources = [
            "https://api.github.com/search/code?q={query}",
            "https://api.telegram.org/fake-bot/messages?q={query}",
            "https://x.com/search?q={query}"
        ]

    def search_mentions(self, token_name):
        mentions = []
        for source in self.sources:
            print(f"[CRAWLER] Searching in {source}")
            mentions.append(f"{token_name} is gaining traction on platform.")
        return mentions

    def analyze_narratives(self, token_name):
        print(f"[CRAWLER] Analyzing narratives for {token_name}")
        mentions = self.search_mentions(token_name)
        filtered = [m for m in mentions if re.search(r"traction|pump|volume", m)]
        print(f"[CRAWLER] Found {len(filtered)} relevant mentions")
        return filtered
