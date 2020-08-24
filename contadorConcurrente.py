import threading

THREADS = 2
MAX_COUNT = 1000000

counter = 0

mutex = threading.Lock()

'''
-Con semaforos contador-

semaforo = threading.Semaphore(2)

semaforo.acquire()
semaforo.acquire()
...
semaforo.release()
'''

def cuenta():
    global counter

    for i in range(int(MAX_COUNT/THREADS)):
        #Opcion 1
        #mutex.acquire()
        counter += 1
        #mutex.release()

        #Opcion 2
        #mutex.acquire()
        #try:
        #    counter += 1
        #finally:
        #    mutex.release()
        
        #Opcion 3
        #with mutex:
        #    counter += 1



threads = []

for i in range(THREADS):
    t = threading.Thread(target=cuenta)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Valor del contador: {counter}")

