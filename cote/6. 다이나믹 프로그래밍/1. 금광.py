import numpy as np

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = np.array([a]).reshape(n, m)
    print(a)