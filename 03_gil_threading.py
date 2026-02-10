import threading
import time

count=0
def brew_chai():
    print(f"{threading.current_thread().name} started brewing process...")
    global count
    
    for _ in range(100_000_000):
        count+=1
    
    print(f"{threading.current_thread().name} finished brewing...")
    
t1=threading.Thread(target=brew_chai, name="barista-1")
t2=threading.Thread(target=brew_chai, name="barista-2")

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end=time.time()
print(f"total time taken: {end - start}")