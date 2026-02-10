from multiprocessing import Process
import time

def cpu_heavy():
    print(f"crunching some numbers...")
    total=0
    
    for i in range(10**8):
        total+=i
    print(f"DONE: {total}")


if __name__=="__main__":
    start = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(4)]
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
    
    end=time.time()

    print(f"total time taken: {end-start}")