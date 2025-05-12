import time
import requests

class PumpfunStream:
    def __init__(self):
        self.endpoint = "https://pump.fun/api/mints/recent"
        self.last_seen = set()

    def fetch(self):
        try:
            res = requests.get(self.endpoint)
            if res.status_code == 200:
                return res.json()
        except Exception as e:
            print(f"[INGEST] Error: {e}")
        return []

    def stream(self):
        print("[INGEST] Starting real-time stream...")
        while True:
            tokens = self.fetch()
            for token in tokens:
                if token['mint'] not in self.last_seen:
                    print(f"[NEW MINT] {token['symbol']} ({token['mint']})")
                    self.last_seen.add(token['mint'])
            time.sleep(6)
