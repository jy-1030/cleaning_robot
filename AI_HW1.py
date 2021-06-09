import random

print("The program is to simulate a cleaning robot.",end = "\n")
print("There will be m * n map when you type in.",end = "\n")

def init():
    # Create an map m*n
    print("Please input the first number M:")
    m = int(input())
    print("Then, input the second number N:")
    n = int(input())
    Map = [[0 for i in range(n)] for j in range(m)]

    # Initial garbages
    print("Please input how many garbages are (-1 will be random)")
    garbage_count = int(input())
    if garbage_count == -1:
        garbage_count = random.randint(1,m*n-1)
    else:
        while garbage_count > m*n or garbage_count < 0:
            print("There is too many garbages, please re-input:")
            garbage_count = int(input())
            if garbage_count == -1:
                garbage_count = random.randint(1,m*n)

    # Fill in garbages
    while garbage_count > 0:
        x = random.randint(0,m-1)
        y = random.randint(0,n-1)
        if Map[x][y] == 1:
            continue
        else:
            Map[x][y] = 1
        garbage_count -= 1
    return Map

def countGarbage(Map):
    garbage = 0
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j] == 1:
                garbage += 1
    return garbage

def clean(x,y,Map,garbage):
    if garbage == 0:
        return
    if Map[x][y] == 1:
        print("There is a garbage in [",x,",",y,"]\nCleaning...")
        Map[x][y] = 0
        print("Success!,there are",garbage-1,"left")
        return
    else:
        print("There is no garbage in [",x,",",y,"]")
        return

def menu():
    print("If you want to initial the map, press 'i'")
    print("If you want to quit, press 'q'")
    return

def cleanMenu():
    Map = init()
    print("If you want to clean automatically, press 'a' (notice: every computer has their own recursive deep,press ctrl+c to terminate)")
    print("If you want to clean by yourself, press 'm'")
    return Map

def Auto(m,n,x,y,Map,Record):
    garbage = int(countGarbage(Map))
    if x >= m or y >= n or x < 0 or y < 0:
        return
    if Record[x][y] == True:
        return
    Record[x][y] = True
    clean(x,y,Map,garbage)
    Auto(m,n,x+1,y,Map,Record)
    Auto(m,n,x,y+1,Map,Record)
    Auto(m,n,x-1,y,Map,Record)
    Auto(m,n,x,y-1,Map,Record)

def Manual(Map,Record):
    while countGarbage(Map) > 0:
        # User input
        print("input x (between 0 ~",len(Map)-1,") :")
        x = int(input())
        if x >= len(Map) or x < 0:
            print("Illegal")
            continue
        print("input y (between 0 ~",len(Map[0])-1,") :")
        y = int(input())
        if y >= len(Map[0]) or y < 0:
            print("Illegal")
            continue
        # Record it and not to go the same time
        if Record[x][y] == True:
            print("You have already clean it!")
            continue
        Record[x][y] = True
        # Record
        if Map[x][y] == 1:
            Map[x][y] = 0
            print("There is a garbage,and it's clear.",countGarbage(Map),"left.")
        else:
            print("There is no garbage,please input another position")

def action(c,Map):
    m = len(Map)
    n = len(Map[0])
    Record = [[0 for i in range(n)] for j in range(m)]
    if c == 'a':
        a = random.randint(0,m-1)
        b = random.randint(0,n-1)
        print("Initial position:",a,b)
        Auto(m,n,a,b,Map,Record)
    elif c == 'm':
        Manual(Map,Record)
    print("The environment is clear!")

if __name__ == '__main__':
    menu()
    counter = 0
    while True:
        if counter != 0:
            menu()
        c = input()[0].lower()
        if c == 'q':
            break
        if c != 'i':
            print("please input it again:")
            continue
        Map = cleanMenu()
        c = input()[0].lower()
        action(c,Map)
        counter += 1



