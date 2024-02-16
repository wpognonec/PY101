# pylint: disable-all
start = int(input("Start: "))
stop = int(input("Stop: ")) + 1

for odd in range(start,stop,2):
    print(odd)