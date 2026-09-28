# Threading
# Implementation
from time import sleep, time
import threading

start = time()

def task(id):
    print(f"Sleeping...{id}")
    sleep(1)
    print(f"Woke up...{id}")

threads = [threading.Thread(target=task, args=[i]) for i in range(10)]
for t in threads:
    t.start()

for t in threads:
    t.join()

end = time()
print(f"Main Thread duration: {end - start} sec")

# Thread Synchronization

import threading

balance = 200
lock = threading.lock()

def deposit(amount, times, lock):
    global balance
    for _ in range(times):
        lock.aquire()
        balance += amount
        lock.release()

def withdraw(amount, times, lock):
    global balance
    for _ in range(times):
        lock.acquire()
        balance -= amount
        lock.release()

deposit_thread = threading.Thread(target=deposit, args=[1, 10000, lock])
withdraw_thread = threading.Thread(target=withdraw, args=[1, 10000, lock])

deposit_thread.start()
withdraw_thread.start()
deposit_thread.join()
withdraw_thread.join()

print(balance)