def silnia_rekurencja(n: int) -> int:
    if n < 0:
        raise ValueError("Nope")
    if n == 0:
        return 1
    return n * silnia_rekurencja(n - 1)


def silnia_iteracja(n: int) -> int:
    if n < 0:
        raise ValueError("Nope")
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik


def nwd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def if_first(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def fibonacci(n: int) -> list[int]:
    if n < 1:
        raise ValueError("Nope")
    if n == 1:
        return [0]
    ciag = [0, 1]
    for _ in range(2, n):
        ciag.append(ciag[-1] + ciag[-2])
    return ciag


def porowniania_silni(n: int) -> None:
    rek = silnia_rekurencja(n)
    ite = silnia_iteracja(n)
    zgodnosc = "Yey" if rek == ite else "Nope"
    print(f"silnia({n}): rekurencja={rek}, iteracja={ite} --> {zgodnosc}")


if __name__ == "__main__":
    print("Porównianie")
    for value in range(6):
        porowniania_silni(value)
    print("nwd")
    pary = [(48, 18), (100, 75), (7, 13), (0, 5)]
    for a, b in pary:
        print(f"nwd({a}, {b}) = {nwd(a, b)}")
    print("Liczby pierwsze")
    pierwsze = [n for n in range(1, 31) if if_first(n)]
    print(pierwsze)
    print("Fibonacci")
    for lenght in [1, 5, 10]:
        print(f"fibonacci({lenght}) = {fibonacci(lenght)}")
