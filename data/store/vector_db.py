import numpy as np

class VectorDB:
    def __init__(self):
        self.db = {}

    def upsert(self, token, vector):
        self.db[token] = np.array(vector)
        print(f"[STORE] Upserted vector for: {token}")

    def similarity(self, token1, token2):
        v1 = self.db.get(token1)
        v2 = self.db.get(token2)
        if v1 is not None and v2 is not None:
            return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        return 0.0
