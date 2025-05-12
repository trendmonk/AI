import threading
import time
import logging

class AgentSandbox:
    def __init__(self, agent_fn):
        self.agent_fn = agent_fn
        self.thread = None
        self.running = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
        logging.info("[SANDBOX] Agent simulation started.")

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        logging.info("[SANDBOX] Agent simulation stopped.")

    def run(self):
        logging.info("[SANDBOX] Running agent in isolation...")
        while self.running:
            try:
                output = self.agent_fn()
                print(f"[SANDBOX] Output: {output}")
            except Exception as e:
                logging.error(f"[SANDBOX] Error: {e}")
            time.sleep(2)

def dummy_agent():
    return {"score": round(random.uniform(60, 95), 2), "timestamp": time.time()}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sandbox = AgentSandbox(dummy_agent)
    sandbox.start()
    time.sleep(10)
    sandbox.stop()
