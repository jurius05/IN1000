#Oppgave 1, denne filen svarer på alle del punktene i oppgave 1.
#det vil si en funksjon som summerer to tal sammen, og en funksjon som teller antall bokstav i en angitt tekst.

def sum_to_numbers(a, b):
    return a + b

tall_1 = sum_to_numbers(1,2)
tall_2 = sum_to_numbers(3,4)
print(tall_1,)
print(tall_2)

def tell_forekomst(text,min_bokstav):
    antall = 0
    for i in text:
        if i == min_bokstav:
            antall += 1
    
    return antall

min_text = "Hei"
min_bokstav = "E"
min_text_1 = tell_forekomst(min_text, min_bokstav)
print(f"I teksten '{min_text}' finnes det {min_text_1} {min_bokstav}-er")

