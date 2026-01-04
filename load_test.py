import threading
import requests
import time

# Replace with your actual NodePort URL
URL = "http://13.219.226.22:30008/metrics"

def send_requests():
    while True:
        try:
            requests.get(URL)
        except:
            pass

# Create 50 threads to flood the server with requests
threads = []
print("Starting Load Test... Watch your dashboard!")
for i in range(50):
    t = threading.Thread(target=send_requests)
    t.daemon = True
    threads.append(t)
    t.start()

# Keep the main thread alive
while True:
    time.sleep(1)
