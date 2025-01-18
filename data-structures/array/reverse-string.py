import string

def reverse(_str: string):
    new = ""
    for i in range(len(_str) - 1, -1, -1):
        new += _str[i]

    return new

def main():
    print(reverse("rotiV"))

main()