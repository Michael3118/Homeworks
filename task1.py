import threading

class CounterThread(threading.Thread):
    # Shared variables
    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(self.rounds):
            self.counter += 1

# Create two instances of the CounterThread
thread1 = CounterThread()
thread2 = CounterThread()

# Start the threads
thread1.start()
thread2.start()

# Join the threads
thread1.join()
thread2.join()

# Check the result
result = CounterThread.counter
print(f"Final counter value: {result}")
