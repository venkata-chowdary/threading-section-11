import threading
import requests
import time

def download(url):
    print(f"starting download from {url}")
    response = requests.get(url)
    print(f"finished downloading from {url} with status code {response.status_code}")
    
    
urls=[
    "https://www.httpbin.org/image/jpeg",
    "https://www.httpbin.org/image/png",
    "https://www.httpbin.org/image/svg",
]


start=time.time()
threads=[]

for url in urls:
    t=threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end=time.time()

print(f"total time taken: {end-start}")