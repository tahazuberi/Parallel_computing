import threading
import time

balance = 100
lock = threading.Lock()

def deposit(amount):
    global balance
    with lock:
        balance += amount
        print(f"Deposited: {amount}, New Balance: {balance}")

def withdraw(amount):
    global balance
    with lock:
        balance -= amount
        print(f"Withdrawn: {amount}, New Balance: {balance}")

# Record the start time
start_time = time.time()

# Create threads for deposit and withdraw
t1 = threading.Thread(target=deposit, args=(50,))
t2 = threading.Thread(target=withdraw, args=(30,))

# Start the threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# Calculate the execution time
execution_time = time.time() - start_time
print(f"Execution Time: {execution_time:.4f} seconds")
