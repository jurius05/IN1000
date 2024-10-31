# 1. Ber brukeren om å svare "ja" eller "nei" på om de vil ha en brus
svar = input("Har du lyst på en brus? (ja/nei): ").lower()

# 2. If-setning for å gjøre en beslutning basert på brukerens svar
if svar == "ja": #hvis input er lik "ja"
    print("Her har du en brus!") #print "Her har du en brus!"
elif svar == "nei": #hvis input er lik "nei"
    print("Den er grei.") #print "Den er grei."
else:
    print("Det forsto jeg ikke helt.")