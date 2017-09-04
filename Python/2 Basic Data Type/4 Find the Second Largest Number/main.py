if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list(arr)
    m = max(lista)
    
    while max(lista) == m:
        lista.remove(m)
    print(max(lista)) 