
# W tym kodzie jak np. wpisze 5 - liczba jaka pierwiastkujemy, a 136 - liczba miejsc po przecinku,
# to wypisze mi dokladnie tyle miejsc ile chce (nawet 136 czy 1000), poniewaz liczymy na int (//),
# a int w Pythonie nie ma limitu cyfr (w przeciwienstwie do float, ktory ma tylko 15-17).
# Na koncu zwracamy wynik jako tekst (str), zeby Python nie ucial cyfr po przecinku.
 
MAKSYMALNA_LICZBA_POWTORZEN = 1000
 
 
def pierwiastek(liczba, miejsca):
    if liczba < 0:
        raise ValueError("Liczba ujemna nie ma pierwiastka")
    if miejsca < 0:
        raise ValueError("Liczba miejsc po przecinku nie może być ujemna")
    if liczba == 0:
        return "0.0"
 
    liczba_przesunieta = liczba * 10 ** (2 * miejsca)
    b = liczba_przesunieta
    a = (b + liczba_przesunieta // b) // 2
 
    while a < b:
        b = a
        a = (b + liczba_przesunieta // b) // 2
    if miejsca == 0:
        return str(b) + ".0"
 
    wynik = str(b).zfill(miejsca + 1) #zfill dopisuje z lewej storny zera aby teskst mial swoja dlugos :))))))))))))
    tekst = wynik[:-miejsca] + "." + wynik[-miejsca:]
    tekst = tekst.rstrip("0")
    if tekst.endswith("."):
        tekst += "0"
    return tekst
 
def testy():
    print("Testy funkcji pierwiastek:")
    print("Przyklad z zadania")
    assert round(float(pierwiastek(4, 2)), 2) == 2.0
 
    assert round(float(pierwiastek(2, 5)), 5) == 1.41421
    assert round(float(pierwiastek(2, 3)), 3) == 1.414
    assert round(float(pierwiastek(9, 4)), 4) == 3.0
 
    print("Testy z zero i jeden:")
    assert float(pierwiastek(0,3)) == 0.0
    assert round(float(pierwiastek(1,3)), 3) == 1.0
    assert round(float(pierwiastek(10,0)), 0) == 3.0
    assert round(float(pierwiastek(10**30, 2)), 2) == 10 ** 15
 
    # def oblicz_z_t(t_liczba, t_miejsca):
    #     liczba = int(t_liczba)
    #     miejsca = int(t_miejsca)
    #     return round(float(pierwiastek(liczba, miejsca)), miejsca)
 
    for liczaba in range(0, 300):
        for miejsce in range(0,7):
            błąd = abs(float(pierwiastek(liczaba, miejsce)) - (liczaba ** 0.5)) # zwarac wartosc bewzlfedna zamienia -0.0002 np na 0.0002 czyli +
            assert błąd < 10 ** (-miejsce) ,(liczaba, miejsce)
 
    for liczaba, miejsce in [(-4,2), (4,-1)]:
        try:
            float(pierwiastek(liczaba, miejsce))
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
 
        liczba = int(coswpisujemy)
        miejsca = int(input().strip())
 
        print(pierwiastek(liczba, miejsca))
 
    except (ValueError, EOFError) as błąd:
        print(f"Błąd: {błąd}")
 
 
main()
 