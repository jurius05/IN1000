
class motorsykkel:
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self.merke = merke
        self.registreringsnummer = registreringsnummer
        self.kilometerstand = kilometerstand

    def kjor(self, km):
        self.kilometerstand += km

    def hentKilometerstand(self):
        return self.kilometerstand
    
    def hentMerke(self):
        return self.merke
    
    def skrivUt(self):
        print(f"Motorsykkelens merke er {self.merke}, registreringsnummeret er {self.registreringsnummer} og kilometerstanden er {self.kilometerstand}.")