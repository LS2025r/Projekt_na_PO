#W tym kodzie jak np wipisze 5 - liczba jaka pierwiastkujem, a 136 - liczba miejsc po przecinku
# to wypisze mi 15-17 miejsc po przecinku, poniewaz float
#moze tylko pzrechowywac 15-17 liczb po przecinku


MAKSYMALNA_LICZBA_POWTORZEN = 1000


def pierwiastek(liczba, miejsca):
    if liczba < 0:
        raise ValueError("Liczba ujemna nie ma pierwiastka")
    if miejsca < 0:
        raise ValueError("Liczba miejsc po przecinku nie może być ujemna")
    if liczba == 0:
        return 0.0

    dokladnosc = 10 ** (-miejsca)
    b = 1
    a = liczba / b

    for _ in range(MAKSYMALNA_LICZBA_POWTORZEN):
        if abs(a - b) < dokladnosc:
            break
        b = (a + b) / 2
        a = liczba / b

    return (a + b) / 2

def testy():
    print("Testy funkcji pierwiastek:")
    print("Przyklad z zadania")
    assert round(pierwiastek(4, 2), 2) == 2.0

    assert round(pierwiastek(2, 5), 5) == 1.41421
    assert round(pierwiastek(2, 3), 3) == 1.414
    assert round(pierwiastek(9, 4), 4) == 3.0

    print("Testy z zero i jeden:")
    assert pierwiastek(0,3) == 0.0
    assert round(pierwiastek(1,3), 3) == 1.0
    assert round(pierwiastek(10,0), 0) == 3.0
    assert round(pierwiastek(10**30, 2), 2) == 10 ** 15

    # def oblicz_z_t(t_liczba, t_miejsca):
    #     liczba = int(t_liczba)
    #     miejsca = int(t_miejsca)
    #     return round(pierwiastek(liczba, miejsca), miejsca)

    for liczaba in range(0, 300):
        for miejsce in range(0,7):
            błąd = abs(pierwiastek(liczaba, miejsce) - (liczaba ** 0.5))
            assert błąd < 10 ** (-miejsce) ,(liczaba, miejsce)

    for liczaba, miejsce in [(-4,2), (4,-1)]:
        try:
            pierwiastek(liczaba, miejsce)
            assert False, "błąd"
        except ValueError:
            pass

    print("Wsyztstkie testy koniec i tyle")


def main():
    try:
        coswpisujemy = input().strip()
        if coswpisujemy == "test":
            testy()
            return
        liczba =int(coswpisujemy)
        miejsca = int(input().strip())
        print(round(pierwiastek(liczba, miejsca), miejsca))
    except (ValueError, EOFError) as błąd:
        print(f"Błąd: {błąd}")


main()