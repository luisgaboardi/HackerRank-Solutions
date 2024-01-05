if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    num_commands = int(input())
    for _ in range(num_commands):
        command = input()
        cmd_parts = command.split()
        if cmd_parts[0] == 'pop':
            s.pop()
        elif cmd_parts[0] == 'remove' and int(cmd_parts[1]) in s:
            s.remove(int(cmd_parts[1]))
        elif cmd_parts[0] == 'discard':
            s.discard(int(cmd_parts[1]))
            
    print(sum(s))
    print(s)
