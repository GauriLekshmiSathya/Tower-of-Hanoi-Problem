n = int(input())
s = 'A'
a = 'B'
d = 'C'

def toh(n, s, a, d):
    if n == 1:
        print(f"Move disk from {s} to {d}")
        return
    toh(n-1, s, a, d)
    print(f"Move disk from {s} to {d}")
    toh(n-1, a, d, s)

toh(n, s, a, d)