if __name__ == '__main__':
    n,m = map(int, input().split())
    for i in range(n//2, 0, -1):
        print('---'*i+'.|.'*(n-i*2)+'---'*i)
    print('-'*((m-7)//2)+'WELCOME'+'-'*((m-7)//2))
    for i in range(1, n//2+1):
        print('---'*i+'.|.'*(n-i*2)+'---'*i)