def vokon_zählen(wort):
    string=wort.lower()
    vokale = 0
    konsonanten = 0   
    for i in string:
        if i in ["a","e","i","o","u","ä","ü","ö"] and i.isalpha():
            vokale += 1
        elif i.isalpha() and i not in ["a","e","i","o","u","ö","ä","ü"]:
            konsonanten +=1
    print("Es gibt "+str( konsonanten )+" Konsonanten und "+str( vokale)+" Vokale.")
  
vokon_zählen("sfhhioqwdnqomadoscpakü")
