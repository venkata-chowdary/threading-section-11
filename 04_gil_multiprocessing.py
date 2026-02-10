from multiprocessing import Process
import time

def crunch_process():
    print("started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("ended the process...")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_process)
    p2 = Process(target=crunch_process)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(f"total time: {end - start}")
