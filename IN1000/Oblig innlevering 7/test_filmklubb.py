from film import Film
from filmklubb import Filmklubb

def testprogram():

    # __init__
    filmklubb = Filmklubb()
    print("oppretter Filmklubb-objekt")

    # les_filmer_fra_fil
    filmklubb.les_filmer_fra_fil('filmer.txt')
    print("Leser filmer fra fil")
    print()

    # skriv_ut_alle_filmer
    filmklubb.skriv_ut_alle_filmer()
    print()

    # registrer_film
    print("Registrerer ny film")
    tittel = input("Tittel: ")
    aar = int(input("Produksjonsår: "))
    filmklubb.registrer_film(tittel, aar)
    print()

    # finn_film_tittel
    print("Leter etter film med en usannsynlig tittel")
    print(filmklubb.finn_film_tittel("sikkert ikke en film"))
    print()

    print("Leter etter film med (start på) tittel 'Hidden '")
    print(filmklubb.finn_film_tittel("Hidden "))
    print()

    # legg_til_skuespillere
    print("Legg til skuespillere for en film" )
    filmklubb.legg_til_skuespillere("Hidden ", "Al harrison", "Kevin costner")
    filmklubb.legg_til_skuespillere("Hidden ", "John glenn", "Glen")
    filmklubb.skriv_ut_alle_filmer()
    print()

    # finn_film_periode
    # Kall på metoden med argumentene etter=2000 og før=2024
    print("Leter ett filmer produsert etter 2000 og før 2024:")
    for film in filmklubb.finn_film_periode(2000, 2024):
        print(film.hent_tittel())
    print()

    # Kall på finn_film_periode med argumentene etter=2020 og før=2020
    print("Leter etter filmer produsert etter 2020 og før 2020:")
    for film in filmklubb.finn_film_periode(2020, 2020):
        print(film.hent_tittel())
    print()


    # SKriv ut all info om alle filmer og sjekk at resultatet er som forventet
    print("Skriver ut all info om alle filmer:")
    filmklubb.skriv_ut_alle_filmer()
    print()
    # <fyll ut>

testprogram()

from film import Film
from filmklubb import filmklubb


