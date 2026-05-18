import threading
import time

# --- task function ---
def print_numbers():
    
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

def print_letters():

    for letter in ["A", "B", "C", "D", "E"]:
        print("Letter:", letter)
        time.sleep(1)

# --- create threads ---
thread1 = threading.Thread(target=print_numbers)

thread2 = threading.Thread(target=print_letters)

# --- start threads ---
thread1.start()
thread2.start()

# --- wait for threads to finish ---
thread1.join()
thread2.join()

print("\nBoth threads completed")