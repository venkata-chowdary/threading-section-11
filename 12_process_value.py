from multiprocessing import Process, Queue, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value +=1



if __name__=="__main__":
    counter=Value('i', 0)
    
    processes=[Process(target=increment,args=(counter, )) for _ in range(0,4)]
    
    for process in processes:
        process.start()
        
    for process in processes:
        process.join()
    print(counter.value)
    
    
#here each process will share the value, and increment that value
#so here the process are getting executed parallely
#lock ensures increments are safe

#Why get_lock() is critical
#Multiple processes can try to update the value at the same time
#counter.value += 1 is NOT atomic
# Without the lock → race condition