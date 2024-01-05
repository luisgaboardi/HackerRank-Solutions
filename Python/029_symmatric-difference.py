if __name__ == '__main__':
    m = int(input())
    m_set = set(map(int, input().split()))

    n = int(input())
    n_set = set(map(int,input().split()))

    intersec = m_set.intersection(n_set)
    for i in sorted(n_set.difference(intersec).union(m_set.difference(intersec))):
        print(i)