from numbers import Number

def naive_solution(array, expected_sum: int):
    for i in array:
        for x in array:
            if x + i == expected_sum:
                print(f'found [{i},{x}]')
                return True

    return False

def better_solution(array, expected_sum: int):
    numbers = set()

    for i in array:
        if i in numbers:
            print(f'found [{expected_sum - i},{i}]')
            return True

        numbers.add(expected_sum - i)

def main():
    result = naive_solution([1, 2, 3, 4, 5, 6], 7)
    print(result)

    result = better_solution([1, 2, 3, 4, 5, 6], 8)
    print(result)

main()