from sys import stdin
from collections import Counter
a = stdin.readline()
N = stdin.readline().split()
b = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
