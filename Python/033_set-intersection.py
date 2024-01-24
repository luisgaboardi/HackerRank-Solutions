if __name__ == '__main__':
    _, n1 = input(), input().strip().split()
    _, n2 = input(), input().strip().split()
    print(len(set(n1).intersection(n2)))