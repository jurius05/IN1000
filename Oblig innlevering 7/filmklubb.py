from film import Film

class Filmklubb:
    def __init__(self):
        self._filmer = []

    def les_filmer_fra_fil(self, filnavn: str):
        with open(filnavn, 'r', encoding='utf-8') as fil:

            for linje in fil:
                linje = linje.strip() #fjerner whitespace på sidene av en streng

                data = linje.split(';') #deler opp strengen i en liste med deler

                film = Film(data[0],int(data[1]))

                self._filmer.append(film)
    
    def skriv_ut_alle_filmer(self):
        for film in self._filmer:
            film.skriv_ut_film()
        
    def registrer_film(self, tittel: str, aar: int):
        film = Film(tittel, aar)
        self._filmer.append(film)

    def finn_film_tittel(self, tittel: str):
        for film in self._filmer:
            if film.tittel.startswith(tittel):
                return film
        return None

    def legg_til_skuespillere(self, tittel: str, navn: str, rolle: str):
        film = self.finn_film_tittel(tittel) #finner filmobjektet med gitt tittel
        if film:
            film.ny_skuespiller(navn, rolle) #legger til skuespiller med gitt navn og rolle
        else:
            print("Film ikke funnet")

    def finn_film_periode(self, år_1: int, år_2: int):
        filmer_i_periode = []
        for film in self._filmer:
            if film.aar > år_1 and film.aar < år_2:
                filmer_i_periode.append(film)
        return filmer_i_periode
    



 
  

