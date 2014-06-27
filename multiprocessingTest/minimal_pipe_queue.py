from multiprocessing import Process, Queue, Pipe

def f(q,c):
    q.put('Hello Queue')

    c.send('Hello Pipe')

    c.close()


if __name__ == '__main__':
    queue = Queue()
    pco, chco = Pipe()
    
    p1 = Process(target=f, args=(queue,chco))
    
    p1.start()

    print(pco.recv())

    print(queue.get())

    p1.join()
