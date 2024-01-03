def print_formatted(number):
    width = len(str(bin(number))[2:])
    for i in range(1, number+1):
        nums = [str(i), str(oct(i))[2:], str(hex(i))[2:].upper(), str(bin(i))[2:]]
        output = ' '.join(num.rjust(width, ' ') for num in nums)
        print(output)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)