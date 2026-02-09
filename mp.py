from multiprocessing import Process
import time


def brew_chai(name):
    print(f"starting to brew chai for {name}")
    time.sleep(10)
    print(f"finished breqing chai for {name}")
    
if __name__=="__main__":
    # chai_makers=["Alice","Bob","Charlie"]
    
    chai_makers=[Process(target=brew_chai, args=(f"Chain maker #{i+1}", )) for i in range(3)]  
    
    #start all processes
    for p in chai_makers:
        p.start()
    #wait for all processes to complete
    
    for p in chai_makers:
        p.join()