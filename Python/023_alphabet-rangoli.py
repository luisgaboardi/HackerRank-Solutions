import string

def print_rangoli(size):
    alphabets = list(string.ascii_lowercase)
    trans = size - 1
    length = size * 2 - 1
    axis = range(0 - trans, length - trans)
    for y in axis:
        row = [alphabets[abs(x)+abs(y)] if abs(x)+abs(y) < size else '-' for x in axis]
        print('-'.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)