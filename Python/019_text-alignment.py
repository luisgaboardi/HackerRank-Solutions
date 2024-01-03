n = int(input())

h_block = 'H' * n
sp_block = ' ' * n
bd_line = h_block + (sp_block * 3) + h_block
ct_line = (h_block * 5)

# top triangle
for ii in range(1, n * 2 + 1, 2):
    print(("H" * ii).center(2 * n - 1, ' '))

# top body
for _ in range(n + 1):
    print(bd_line.center(n * 6 - 1, ' '))

# middle band
for _ in range(n // 2 + 1):
    print(ct_line.center(n * 6 - 1, ' '))

# bottom body
for _ in range(n + 1):
    print(bd_line.center(n * 6 - 1, ' '))

# bottom triangle
for ii in range(n * 2 - 1, 0, -2):
    print(("H" * ii).center(n * 10, ' '))