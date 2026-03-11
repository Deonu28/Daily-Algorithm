import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    if N == i + sum(map(int, str(i))):
        print(i)
        break
else:
    print(0)
