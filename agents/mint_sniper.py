import requests
import time

class MintSniper:
    def __init__(self):
        self.tracked_tokens = set()

    def fetch_new_mints(self):
        url = "https://pump.fun/api/mints/recent"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return []

    def analyze_and_flag(self, token):
        print(f"[SNIPER] Analyzing new token: {token['name']} ({token['symbol']})")
        if token['liquidity'] > 5 and token['creator_verified']:
            print(f"🚀 Potential snipe: {token['symbol']}")

    def run(self):
        while True:
            tokens = self.fetch_new_mints()
            for token in tokens:
                if token['mint'] not in self.tracked_tokens:
                    self.tracked_tokens.add(token['mint'])
                    self.analyze_and_flag(token)
            time.sleep(5)
