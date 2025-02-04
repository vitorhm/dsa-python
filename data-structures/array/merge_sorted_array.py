def merge(array1, array2):
    merged = []
    i1 = 0
    i2 = 0
    n1 = array1[0]
    n2 = array2[0]

    while n1 is not None or n2 is not None:
        if (n2 is None) or (n1 is not None and n1 < n2):
            merged.append(n1)
            i1 += 1
            n1 = None
            if i1 < len(array1):
                n1 = array1[i1]

        else:
            merged.append(n2)
            i2 += 1
            n2 = None
            if i2 < len(array2):
                n2 = array2[i2]

    return merged

def main():
    array1 = [0, 1, 4, 6]
    array2 = [2, 3, 5, 7]

    merged = merge(array1, array2)
    print(merged)

main()