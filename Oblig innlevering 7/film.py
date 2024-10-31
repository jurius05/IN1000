class Film:
    def __init__(self, tittel, aar):
        self.tittel = tittel
        self.aar = aar
        self.skuespillere = {}

    def hent_tittel(self):
        return self.tittel

    def ny_skuespiller(self, navn, rolle):
    #Legger til skuespiller og rolle i dictionary, hvis skuespilleren allerede er registrert, printer den ut en feilmelding
        for skuespiller in self.skuespillere.keys():
            if navn == skuespiller:
                print("Skuespilleren er allerede registrert")
                return
        self.skuespillere[navn] = rolle
    
    def hent_skuespillere_navn(self):
    #Returnerer en liste over alle skuespillerne sine navn i filmen
        skuespillere_navn = []
        for skuespiller in self.skuespillere.keys():
            skuespillere_navn.append(skuespiller)
        return skuespillere_navn
    
    def skriv_ut_film(self):
    #Skriver ut alt om filmen
        print(f"Tittel: {self.tittel}")
        print(f"Produksjonsår: {self.aar}")
        print("Skuespillere:")
        for skuespiller in self.skuespillere.keys():
            print(f"{skuespiller}: {self.skuespillere[skuespiller]}")
        print('') #tom linje

    def sjekk_periode(self, år_1, år_2):
    #Sjekker om produksjonsåret til filmen er innenfor det gitte året
        if self.aar > år_1 and self.aar < år_2:
            return True
        else:
            return False
        
    def sjekk_tittel(self, tittel_start):
    #Sjekker om tittelen til filmen starter med det gitte tittel_start

        if len(tittel_start) == '':
            return True
        
        if len(tittel_start) > len(self.tittel):
            return False
        
        if self.tittel.startswith(tittel_start):
            return True
        else:
            return False
        
    def __str__(self):
        #Returnerer en streng som inneholder alt om filmen
        resultat = f"{self.tittel} ({self.aar})"

        resultat += "\nSkuespillere:"
        for skuespiller, rolle in self.skuespillere.items():
            resultat += f"\n{skuespiller}: {rolle}"
        return resultat

        