from motorsykkel import motorsykkel

def hovedprogramm(merke, registreringsnummer, kilometerstand = 0):
    motorsykkel1 = motorsykkel(merke, registreringsnummer, kilometerstand)
    print(motorsykkel1.hentMerke())
    lengde = int(input('hvor langt skal du kjøre?'))
    motorsykkel1.kjor(lengde)
    print(motorsykkel1.hentKilometerstand())
    motorsykkel1.skrivUt()

hovedprogramm("Yamaha", "12345678")

