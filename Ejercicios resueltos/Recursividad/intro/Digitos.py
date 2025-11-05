# 1.

# a)

def cant(N):
    if N < 10: return 1
    return cant(N // 10) + 1

print(cant(194180))

# b)

def dig (N):
    if N < 10: return 1
    return dig (N // 10) + 1

def reversa_num(N):
    print(f'entro con {N}')
    if N < 10: return N
    else:
        a = N % 10
        l = dig(N)
        N = N // 10
        print(f'devuelvo{a}')
        return a * 10 ** (l - 1) + reversa_num(N)

print(reversa_num(321))

#c)

def sumatoria(n: int) -> int:
    if n < 2: return 1
    return sumatoria(n-1) + n

print(sumatoria(5))
