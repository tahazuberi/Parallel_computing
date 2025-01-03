import threading
import time

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)

def thread_function(n, thread_id):
    start_time = time.time()
    print(f"Thread {thread_id} started.")
    
    result = calc_fibonacci(n)  # Calculate Fibonacci of n
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Thread {thread_id} finished. Fibonacci({n}) = {result}. Execution time: {execution_time:.4f} seconds.")

threads = []
n = 20  # Fibonacci number to calculate

# Record the start time for the total execution
total_start_time = time.time()

for i in range(4):  # 7 threads
    t = threading.Thread(target=thread_function, args=(n, i+1))
    threads.append(t)
    
    print(f"Starting thread {i + 1}")
    t.start()

for t in threads:
    t.join()  # Wait for all threads to complete

# Record the end time for the total execution
total_end_time = time.time()

# Calculate the total execution time
total_execution_time = total_end_time - total_start_time

print(f"All threads completed. Total execution time: {total_execution_time:.4f} seconds.")
