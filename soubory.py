def vytvor_soubor(jmeno_souboru, hlavicka):
  with open(jmeno_souboru, mode="w") as file:
    jmeno, prijmeni, vek = hlavicka
    text = f"{jmeno},{prijmeni},{vek}" + "\n"
    file.writelines(text)

def zapis_do_souboru(jmeno_souboru, zapisuji):
  with open(jmeno_souboru, mode="a") as file:
    jmeno, prijmeni, vek = zapisuji
    text = f"{jmeno},{prijmeni},{vek}" + "\n"
    file.writelines(text)

def nahraj_csv_soubor(jmeno_souboru):
  with open(jmeno_souboru, mode="r") as file:
    data = file.readlines()
  return data

def pracuji_se_soubory():
    mode = input("Co chces dela? (Zapisovat -> z) nebo (Pracovat s daty -> p)").lower()

    if mode == "z":
        vytvorit = input("Chce vytvorit soubor(y) nebo uz existuje(e)").lower()
        if vytvorit == "y":
            jmeno_souboru = input("Zadej jmeno souboru i s .csv")
            vytvor_soubor(jmeno_souboru, hlavicka=["jmeno", "prijmeni", "vek"])
            print(f"Vytvoril jsem soubor{jmeno_souboru}")

        elif vytvorit == "e":
            jmeno_souboru = "ucitele.csv"  # Todo dodelat input.
            list_pro_zapis = zadej_informace()
            zapis_do_souboru(jmeno_souboru, list_pro_zapis)
            print(f"Zapsal jsem {list_pro_zapis}")
        else:
            print("Neco se nepovedo")
    elif mode == "p":
        jmeno_souboru = "ucitele.csv"  # Todo dodelat input.
        data = nahraj_csv_soubor(jmeno_souboru)
        for radek in data:
            print(radek)

    else:
        print("Neco se nepovedo")

if __name__ == "__main__":
    print("Tohle je hlavni skript")