from numbers import Number

def naive_solution(array, sum: Number):
    for i in array:
        for x in array:
            if x + i == sum: return True

    return False

def main():
    result = naive_solution([1, 2, 3, 4, 5, 6], 7)
    print(result)

main()