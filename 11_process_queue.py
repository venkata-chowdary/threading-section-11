from multiprocessing import Process, Queue, Value

def prepare_chai(queue):
    queue.put("masala chai is ready")

counter=Value('i', 0)

if __name__=="__main__":
    queue=Queue()

    p=Process(target=prepare_chai, args=(queue,))
    #here queue will be accessed by all the process along with that prepare_chai funtion
    p.start()
    p.join()

    print(queue.get())
