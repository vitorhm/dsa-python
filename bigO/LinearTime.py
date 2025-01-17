import time

def find_nemo(l):
    start_time = time.time()
    for i in l:
        if i == "nemo":
            print("found nemo")
            break

    print("--- %s seconds ---" % (time.time() - start_time))

def main():
    l = []

    for i in range(10000000):
        l.append("tx")

    l.append("nemo")
    find_nemo(l)

main()