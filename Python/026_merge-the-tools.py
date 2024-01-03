import textwrap


def merge_the_tools(string, k):
    subseq_list = textwrap.wrap(string, k)
    for subseq in subseq_list:
        u = ""
        for n in range(k):
            if subseq[n] not in u:
                u += subseq[n]
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)