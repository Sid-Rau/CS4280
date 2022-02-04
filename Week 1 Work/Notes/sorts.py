from random import shuffle 
def swap(x, j, k): 
    if j != k: 
        x[j], x[k] = x[k], x[j]

def is_in_order(x):
    for k in range(len(x) - 1):
        if x[k] > x[k+1]:
            return False
    return True

def bozo(x):
    while not is_in_order(x):
        shuffle(x)

def bubble(x):
    pointer = len(x)
    while pointer > 1:
        for k in range(pointer-1):
            if x[k] > x[k+1]:
                swap(x,k,k+1)
        pointer -= 1

def trickle(x):
    pointer = 1 
    while pointer < len(x): 
        for i in range(pointer, 0 ,-1):
            if x[i] < x[i -1]:
                swap(x,i,i-1)
        pointer += 1



    x = list(range(100))
    shuffle(x)
    print(x)
    trickle(x)
    print(x)