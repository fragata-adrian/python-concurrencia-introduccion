import threading
import time
import logging

from tiempo import Contador

# Para que logging imprima más info sobre los threads
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir(secs):
    time.sleep(secs)


cont = Contador()

cont.iniciar()

lista = [] #crea una lista vacía

for i in range(10):
    #crear un thead
    t = threading.Thread(target=dormir, args=[1.5])
    #lanzarlo
    t.start()
    print("h",i+1)
    lista.append(t)

for thread in lista:
    print(thread)
    thread.join()

cont.finalizar()
cont.imprimir()