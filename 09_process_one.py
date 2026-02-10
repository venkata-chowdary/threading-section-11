import threading
import time



def cpu_heavy():
    print(f"crunching some numbers...")
    total=0
    
    for i in range(10**8):
        total+=i
    
    print(f"DONE: {total}")
    
start = time.time()

threads = [threading.Thread(target=cpu_heavy) for _ in range(4)]
for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()
    

end=time.time()

print(f"total time taken: {end-start}")