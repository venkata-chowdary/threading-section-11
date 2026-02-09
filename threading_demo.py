import threading
import time


def take_order():
    for i in range(1,4):
        print(f"Taking order {i}")
        time.sleep(2)
        
        
def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(5)
        
#creating threads

order_td=threading.Thread(target=take_order)
brew_td=threading.Thread(target=brew_chai)

    
order_td.start()
brew_td.start()    

#wait for both threads to complete
order_td.join()
brew_td.join()


print("All orders are taken and chai is brewed")