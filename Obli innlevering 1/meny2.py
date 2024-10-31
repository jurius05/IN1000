# Program 2: meny2.py

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

# 3. Gi tilbakemelding basert på en annen logikk
vegetarrett = hovedrett == "salat" #hvis hovedrett er lik salat
gronnsakstilbehor = tilbehor == "gulrøtter" #hvis tilbehor er lik gulrøtter

if vegetarrett and gronnsakstilbehor: #hvis vegetarrett og gronnsakstilbehor blir valgt
    print("Du har valgt et vegetarmåltid.")
elif not vegetarrett and not gronnsakstilbehor: #hvis ingen av valgene blir valgt
    print("Du spiser ikke nok grønnsaker!")
else:
    print(f"Du har valgt {hovedrett} med {tilbehor}.")