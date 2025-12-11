import threading
import time

def worker():
    for i in range(5):
        print(f"Thread working: {i}")
        time.sleep(0.5)

t = threading.Thread(target=worker)
t.start()
t.join()

print("Thread finished")
