from timeit import repeat

list = []
for i in range(100000):
    list.append("nemo")

print(list[0])