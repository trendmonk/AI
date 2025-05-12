import re

class TokenNormalizer:
    def __init__(self):
        self.pattern = re.compile(r"[^a-zA-Z0-9]")

    def normalize(self, name):
        return self.pattern.sub("", name).lower()

    def enrich_metadata(self, token_data):
        return {
            "symbol": self.normalize(token_data.get("symbol", "")),
            "name": token_data.get("name", "").title(),
            "market_cap": float(token_data.get("market_cap", 0)),
            "verified": bool(token_data.get("verified", False))
        }
