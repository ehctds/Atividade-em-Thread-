from random import randint
from threading import Thread
import time
tamanho= 1000000
v = [randint(0,tamanho) for i in range(tamanho)]

x = 500000
v1= lambda v, x: [v[i:i+x] for i in range(0, len(v), x)]

output=v1(v, x)
#print(output[1])
#print('A lista final é:', output)


def tarefa1():
    time.sleep(5) #comando utilizado apenas para teste
    maxvalue= max(output[0])
    print(f"O maior valor da primeira metade é {maxvalue}") 
t1 = Thread(target= tarefa1)
def tarefa2():
    time.sleep(5)
    maxvalue2 = max(output[1])
    print(f"O maior valor da segunda metade é {maxvalue2} ") 
t2 = Thread(target= tarefa2)
t1.start() 
t2.start()
t1.join()