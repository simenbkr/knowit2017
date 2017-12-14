mem = {}
def extfib(n):
    if n in mem: return mem[n]
    if n <= 3: return [1, 2, 4][n-1]
    mem[n] = extfib(n-1) + extfib(n-2) + extfib(n-3)
    return mem[n]

print extfib(30)
