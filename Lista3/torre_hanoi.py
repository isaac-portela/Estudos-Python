"""
    - Isaac Portela da Silva
    - 20192004900
"""
def torre_hanoi(N):
    if N == 1:
        return 1
    return 2 * torre_hanoi(N-1) + 1
    
teste = 0
while True:
    n = int(input())

    if n == 0:
        break

    teste += 1
    qntd_mov = torre_hanoi(n)
    print("Teste", teste)
    print(qntd_mov)
    print()
