#Es wird definiert was gerrechnet wird
def uhrzeit_minuten_addieren(stunden, minuten, summand):
#Während-Schleifen werden eingeführt, damit Stundenanzahlen über 24, in 1 oder mehr tage umgewandelt werden.
    while minuten+summand>=60:
        minuten=minuten-60
        stunden=stunden+1
    while stunden>=24:
        stunden=stunden-24
#Das resultat wird gedruckt
    print(str(stunden) +":" + str(minuten+summand))
 
 #Beispiele von Berrechnungsaufgaben
uhrzeit_minuten_addieren(17, 32, 8) # 17:32 + 8 Min = 17:40
uhrzeit_minuten_addieren(19, 7, 63) # 19:07 + 63 Min = 20:10
uhrzeit_minuten_addieren(16, 10, 1111) # 16:10 + 1111 Min = 10:41
