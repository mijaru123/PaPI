from multiprocessing import Process, Value, Array


def f(arr,v):
    #arr.reverse()
    for i in range(len(arr)):
        arr[i] = -arr[i]
        v.value= v.value +1
        print(v.value)
        print(arr[:])


if __name__ == '__main__':
    a = Array('i', range(12))
    n = Value('i', 0)
    p1 = Process(target=f, args=(a,n))
    p2 = Process(target=f, args=(a,n))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(a[:])
    print(n.value)
