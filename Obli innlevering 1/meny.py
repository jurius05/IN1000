# Program 1: meny.py

# 1. Skriv ut menyen
print("Velkommen til vår restaurant! Her er menyen vår:")
print("Hovedretter:")
print("1. Biff")
print("2. Torsk")
print("3. Salat (vegetar)")

print("\nTilbehør:") #\n gir en ny linje slik at menyen blir mer oversiktlig
print("1. Gulrøtter (grønnsakstilbehør)")
print("2. Bearnaise (saustilbehør)")

# 2. Be brukeren om å velge hovedrett og tilbehør
hovedrett = input("\nVelg en hovedrett (skriv navnet på retten, f.eks. 'Biff'): ").lower() #.lower() gjør at brukeren kan skrive biff, Biff, BIFF osv.
tilbehor = input("Velg ett tilbehør (skriv navnet på tilbehøret, f.eks. 'Gulrøtter'): ").lower()

# 3. Gi tilbakemelding basert på valgene
if hovedrett != "salat" or tilbehor != "gulrøtter": #hvis hovedrett ikke er lik salat eller tilbehor ikke er lik gulrøtter
    print("Du spiser ikke nok grønnsaker!")
elif hovedrett == "salat" and tilbehor == "gulrøtter": #hvis hovedrett er lik salat og tilbehor er lik gulrøtter
    print("Du har valgt et vegetarmåltid.")
else:
    print(f"Du har valgt {hovedrett} med {tilbehor}.") #dersom ingen av if-setningene stemmer, print "Du har valgt {hovedrett} med {tilbehor}."