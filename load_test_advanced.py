import requests
import threading
import time

# Update with your Worker Node Public IP
url = "http://13.219.226.22:30008"

def send_requests():
    print(f"Thread started for {url}")
    while True:
        try:
            # Short timeout to keep the loop moving fast
            requests.get(url, timeout=1)
        except Exception:
            pass

# Create 20 concurrent threads to generate high CPU load
threads = []
for i in range(20):
    t = threading.Thread(target=send_requests)
    t.daemon = True # Allows script to exit on Ctrl+C
    threads.append(t)
    t.start()

print("Load test running with 20 threads. Press Ctrl+C to stop.")

# Keep the main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nLoad test stopped.")
