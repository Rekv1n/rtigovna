def otvaranje_datoteke(datoteka):
    with open(datoteka) as fajl:
        info = fajl.read()
        return info

def obrada(podaci):
    r = dict()
    for linija in podaci[0:-1].split("\n"):
       drzava, sport, medalja, godina, grad = linija.split(",")
       if godina == unos[0:4]:
           if drzava not in r:
               r[drzava] = dict()
           if medalja not in r[drzava]:
               r[drzava][medalja] = 1
           else:
               r[drzava][medalja] += 1
           if 'Gold' not in r[drzava]:
               r[drzava]['Gold'] = 0
           elif 'Silver' not in r[drzava]:
               r[drzava]['Silver'] = 0
           elif 'Bronze' not in r[drzava]:
               r[drzava]['Bronze'] = 0

    return r

def obrada1(recnik):
    lista_drzava = []
    for k in recnik.keys():
        lista_drzava.append(k)
    return lista_drzava

def obrada2(recnik):
    lista_zlatnih_medalja = []
    for k in recnik.keys():
        for key in recnik[k].keys():
            if key == 'Gold':
                lista_zlatnih_medalja.append(recnik[k][key])
    return lista_zlatnih_medalja

def obrada3(recnik):
    lista_srebrnih_medalja = []
    for k in recnik.keys():
        for key in recnik[k].keys():
            if key == 'Silver':
                lista_srebrnih_medalja.append(recnik[k][key])
    return lista_srebrnih_medalja

def obrada4(recnik):
    lista_bronzanih_medalja = []
    for k in recnik.keys():
        for key in recnik[k].keys():
            if key == 'Bronze':
                lista_bronzanih_medalja.append(recnik[k][key])
    return lista_bronzanih_medalja

def izlaz(iz_dat, *liste):
    with open(iz_dat, "w") as iz:
        iz.write("Country Code,Gold,Silver,Bronze,Place\n")
        x = 1
        count_z = 0
        count_s = 0
        count_b = 0
        while x < (int(unos[-1]) + 1) :
            for i, j, k, t in zip(lista, lista1, lista2, lista3):
                z = max(lista1)
                if j == z:
                    count_z += 1
                    if count_z > 1:
                        s = max(lista2)
                        if k == s:
                            count_s += 1
                            if count_s > 1:
                                b = max(lista3)
                                if t == b:
                                    count_b += 1
                                    if count_b == 1:
                                        l1 = [i, j, k, t, x]
                                        iz.write("{},{},{},{},{}\n".format(l1[0], l1[1], l1[2], l1[3], l1[4]))
                                        lista.remove(i)
                                        lista1.remove(j)
                                        lista2.remove(k)
                                        lista3.remove(t)
                                        x += 1
                            if count_s == 1:
                                l2 = [i, j, k, t, x]
                                iz.write("{},{},{},{},{}\n".format(l2[0], l2[1], l2[2], l2[3], l2[4]))
                                lista.remove(i)
                                lista1.remove(j)
                                lista2.remove(k)
                                lista3.remove(t)
                                x += 1

                    if count_z == 1:
                        l3 = [i, j, k, t, x]
                        iz.write("{},{},{},{},{}\n".format(l3[0], l3[1], l3[2], l3[3], l3[4]))
                        lista.remove(i)
                        lista1.remove(j)
                        lista2.remove(k)
                        lista3.remove(t)
                        x += 1

unos = input("Unesite godinu i broj najboljih drzava: ")
try:
    ulazna_datoteka = "medals.csv"
    izlazna_datoteka = "countries_{}.csv".format(unos[0:4])
    p = otvaranje_datoteke(ulazna_datoteka)
    d = obrada(p)
    lista = obrada1(d)
    lista1 = obrada2(d)
    lista2 = obrada3(d)
    lista3 = obrada4(d)
    izlaz(izlazna_datoteka, lista, lista1, lista2, lista3)
except FileNotFoundError:
    print("DAT_GRESKA")


