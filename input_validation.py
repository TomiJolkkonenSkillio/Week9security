import re

def validoi_nimi(nimi):
    return nimi.isalpha() # pitaa olla aakkosia

def validoi_ika(ika):
    return ika.isdigit() and 1 <= int(ika) <= 120 # nro valilta 1-120

def validoi_meili(meili):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', meili)) # regex-check ja valissa miukumauku

def validoi_puhnro(puhnro):
    return bool(re.match(r'^\+?[0-9]{7,15}$', puhnro)) # regex, vain numeroita, voi alkaa plussalla

def validoi_osoite(osoite):
    return len(osoite.strip()) > 0 # ei saa olla tyhja

def validi_syote(kayttajasyote, validointifunktio, virheilmoitus):
    while True:
        syote = input(kayttajasyote).strip()
        if validointifunktio(syote):
            return syote
        print(virheilmoitus)

if __name__ == "__main__":
    nimi = validi_syote("Anna nimi: ", validoi_nimi, "Vaara nimi, kayta vain aakkosia.")
    ika = validi_syote("Anna ika: ", validoi_ika, "Vaara ika, numero voi olla valilta 1-120.")
    meili = validi_syote("Anna meili: ",validoi_meili, "vaara meiliformaatti.")
    puhnro = validi_syote("Anna puhelin: ", validoi_puhnro, "vaara puh.nro, kayta vain numeroita, voit aloittaa +:lla.")
    osoite = validi_syote("Anna osoitteesi: ", validoi_osoite, "Osoite ei saa olla tyhja.")
    
    print("\nKayttajan tiedot:")
    print(f"Nimi: {nimi}")
    print(f"Ika: {ika}")
    print(f"Meili: {meili}")
    print(f"Puh.nro: {puhnro}")
    print(f"Osoite: {osoite}")
