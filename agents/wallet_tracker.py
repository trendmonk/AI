import json

class WalletTracker:
    def __init__(self):
        self.wallet_profiles = {}

    def load_transactions(self, wallet_address):
        print(f"[TRACKER] Loading transactions for: {wallet_address}")
        return [{"tx_id": "abc123", "amount": 0.5, "profit": True}]

    def calculate_score(self, txs):
        wins = sum(1 for tx in txs if tx["profit"])
        return round(wins / len(txs), 2) if txs else 0

    def profile_wallet(self, wallet_address):
        txs = self.load_transactions(wallet_address)
        score = self.calculate_score(txs)
        self.wallet_profiles[wallet_address] = {"score": score}
        print(f"[TRACKER] {wallet_address} score: {score}")
