from film import Film

def test_film():
    # __init__
    film_1 = Film("The Matrix", 1999)
    film_2 = Film("The Imitation Game", 2014)
    print("Oppretter to filmer")
    print(f"Film 1: {film_1.hent_tittel()}, Film 2: {film_2.hent_tittel()}")

    # hent_tittel
    print("Skriver ut titler på to filmer")
    print(film_1.hent_tittel())
    print(film_2.hent_tittel())
    print('')

    # ny_skuespiller
    print("Legger til to skuespillere")
    film_1.ny_skuespiller("Keanu Reeves", "Neo")
    film_1.ny_skuespiller("Carrie-Anne Moss", "Trinity")
    print(film_1.skriv_ut_film())
    print()

    # Prøv å legge inn en av skuespillerne igjen, med en ny rolle
    print("Tester ulovlig innlegging av skuespiller")
    film_1.ny_skuespiller("Keanu Reeves", "Thomas Anderson")
    print(film_1.skriv_ut_film())
    print('')

    # skriv_ut_film
    print("Skriver ut all info om to filmer:")
    print(film_1.skriv_ut_film())
    print(film_2.skriv_ut_film())
    print('')

    # hent_alle_skuespiller_navn
    print("Henter og skriver ut alle skuespillernavn for en film:")
    print(film_1.hent_skuespillere_navn())
    print('')

    # sjekk_periode
    print("Sjekker at en film er i oppgitt periode")
    print(film_1.sjekk_periode(1990, 2000))  # Skal gi True
    print('')

    print("Sjekker at en film ikke kan være produsert før og etter samme år")
    print(film_2.sjekk_periode(2014, 2014))  # Skal gi False
    print('')

    # sjekk_tittel
    print("Sjekker om starten på en films tittel kjennes igjen")
    print(film_1.sjekk_tittel("The"))  # Skal gi True
    print(film_2.sjekk_tittel("Game"))  # Skal gi False
    print('')
    print('hallo')

    # __str__
    # Skriv ut film-objekt med print
    print("Skriver ut en film med print (test av __str__)")
    print(film_1)
    print()

test_film()