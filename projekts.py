nezinamieVardi = []
vardi = {
        "sfera" : ["sfer", "sfera", "svera", "sfeera", "lode", "lodes", "sphere", "spher", "lodei", "sphe", "bumba", "bumbas", "lodite", "lodites", "sph", "sferas", "sferai", "sferaj"],
        "trijsturis" : ["trijsturis", "trijstuuris", "trijstur", "trijstuur", "triangle", "3-sturis", "3sturis", "3-stuuris", "3stuuris", "3angle", "3-angle", "triangles", "3angle", "3angles", "3ang", "3str", "trissturis", "tristuris", 'trstr', "trjstr", 'trijstr' ],
        "kubs" : ["kubs", "cube", "kubiks", "kub", "kubi", "kubikiem", "kubiem", "kubikus", "kuba", "kubika", "kubu"],
        "konuss" : ['konuss', 'konus', 'kone', 'cone', 'konusa', 'konusam', 'konusiem'],
        "cilindrs" : ['cilindrs', 'cilindr', 'cilinder', 'cilindr', 'cilndr', 'cilindra', 'cilindram', 'cilindru', 'cilnd', 'cilin'],
        "kontrole" : ["#n"]
    }
citiVardi = { 
    "spv" : ["pilna", "pilnas", "pilno", "virsma", "virsmu", "virsmai", "laukums", "laukuma", "laukumam"]
}
tilpums = ["tilpums", "v", "tilp", "tilpum", "tlpm", "tilpumu"]
def garakaTeikumaVienkarsosana(vards1):
    visiburti = []
    istieBurti = []
    kurJamekle = ""
    vardi3 = []
    kurJamekle1 = ""
    a = 0
    teikums = ""
    for burts in vards1:
        visiburti.append(burts)
    while a < len(visiburti):
        if visiburti[a] == "Ā" or visiburti[a] == "ā":
            istieBurti.append("a")
        elif visiburti[a] == "Č" or visiburti[a] == "č":
            istieBurti.append("c")
        elif visiburti[a] == "ē" or visiburti[a] == "Ē":
            istieBurti.append("e")
        elif visiburti[a] == "Ģ" or visiburti[a] == "ģ":
            istieBurti.append("g")
        elif visiburti[a] == "Ī" or visiburti[a] == "ī":
            istieBurti.append("i")
        elif visiburti[a] == "Ķ" or visiburti[a] == "ķ":
            istieBurti.append("k")
        elif visiburti[a] == "Ļ" or visiburti[a] == "ļ":
            istieBurti.append("l")
        elif visiburti[a] == "Ņ" or visiburti[a] == "ņ":
            istieBurti.append("n")
        elif visiburti[a] == "Š" or visiburti[a] == "š":
            istieBurti.append("s")
        elif visiburti[a] == "Ū" or visiburti[a] == "ū":
            istieBurti.append("u")
        elif visiburti[a] == "Ž" or visiburti[a] == "ž":
            istieBurti.append("z")
        elif visiburti[a] == " ":
            for b in istieBurti:
                teikums += b
            vardi3.append(teikums.lower())
            teikums = ""
            istieBurti = []
        elif visiburti[a] == "." or visiburti[a] == "," or visiburti[a] == "!":
            pass
        else:
            istieBurti.append(visiburti[a])
        a += 1
    for b in istieBurti:
        teikums += b
    vardi3.append(teikums.lower())
    for n in vardi3:
        for i in vardi:
            for u in vardi[i]:
                if u == n:
                    kurJamekle = i
                    vardi3.remove(n)
    for n in vardi3:
        for i in citiVardi:
            for u in citiVardi[i]:
                if u == n:
                    kurJamekle1 = i
                    vardi3.remove(n)
    for n in vardi3:
        for i in tilpums:
            if n == i:
                kurJamekle1 = "tilpums"
    if kurJamekle == "sfera":
        if kurJamekle1 == "tilpums":
            sferaV()
        elif kurJamekle1 == "spv":
            sferaSPV()
    elif kurJamekle == "kubs":
        if kurJamekle1 == "tilpums":
            kubaV()
        elif kurJamekle1 == "spv":
            kubaSPV()
    elif kurJamekle == "konuss":
        if kurJamekle1 == "tilpums":
            konusaV()
        elif kurJamekle1 == "spv":
            konusaSPV()
    elif kurJamekle == "cilindrs":
        if kurJamekle1 == "tilpums":
            cilindraV()
        elif kurJamekle1 == "spv":
            cilindraSPV()
def cilindraV():
    radius = float(input("Ievadi cilindra pamata radiusu: "))
    h = float(input("Ievadi cilindra augstumu: "))
    pamataS = 3.14 * radius * radius
    v = pamataS * h
    print(f"Cilindra tilpums ir {v}")
    inputs()
def cilindraSPV():
    radius = float(input("Ievadi cilindra pamata radiusu: "))
    h = float(input("Ievadi cilindra augstumu: "))
    pamataS = 3.14 * radius * radius
    sv = 2 * 3.14 * radius * h
    spv = pamataS + pamataS + sv
    print(f"Cilindra pilnas virsmas laukums ir {spv}")
    inputs()
def cilindrs():
    radius = float(input("Ievadi cilindra pamata radiusu: "))
    h = float(input("Ievadi cilindra augstumu: "))
    pamataS = 3.14 * radius * radius
    sv = 2 * 3.14 * radius * h
    spv = pamataS + pamataS + sv
    v = pamataS * h
    print(f"Cilindra pilnas virsmas laukums ir {spv} bet tilpums ir {v}")
    inputs()
def konusaV():
    radius = float(input("Ievadi konusa pamata radiusu: "))
    h = float(input("Ievadi konusa augstumu: "))
    pamataS = 3.14 * radius * radius
    v = h * pamataS
    print(f"Konusa tilpums ir {v}")
    inputs()
def konusaSPV():
    radius = float(input("Ievadi konusa pamata radiusu: "))
    veidule = float(input("Ievadi konusa veidules garumu: "))
    pamataS = 3.14 * radius * radius
    sv = 3.14 * radius * veidule
    spv = sv + pamataS
    print(f"Konusa pilnas virsmas laukums ir {spv}")
    inputs()
def konus():
    radius = float(input("Ievadi konusa pamata radiusu: "))
    h = float(input("Ievadi konusa augstumu: "))
    veidule = float(input("Ievadi konusa veidules garumu"))
    pamataS = 3.14 * radius * radius
    sv = 3.14 * radius * veidule
    spv = sv + pamataS
    v = h * pamataS
    print(f"Konusa pilnas virsmas laukums ir {spv} bet tā tilpums ir {v}")
    inputs()
def kubaSPV():
    mala = float(input("Ievadi šķautnes, jeb malas garumu: "))
    spv = mala * mala * 6
    print(f"Kuba pilnas virsmas laukums ir {spv}")
    inputs()
def kubaV ():
    mala = float(input("Ievadi šķautnes, jeb malas garumu: "))
    v = mala * mala * mala
    print(f"Kuba tilpums ir {v}")
    inputs()
def sferaV ():
    radius = float(input("Ievadi sfēras rādiusu: "))
    v = 4 * 3.14 * radius * radius * radius / 3
    print(f"Sfēras tilpums ir {v}")
    inputs()
def sferaSPV ():
    radius = float(input("Ievadi sfēras rādiusu: "))
    spv = 4 * 3.14 * radius * radius
    print(f"Sfēras pilnas virsmas laukums ir {spv}")
    inputs()
def nezSaraksts():
    print(nezinamieVardi)
    inputs()
def meklesana(mainigais):
    for i in vardi:
        for u in vardi[i]:
            if u == mainigais:
                return i 
def sfera():
    radius = float(input("Ievadi sfēras rādiusu: "))
    spv = 4 * 3.14 * radius * radius
    v = 4 * 3.14 * radius * radius * radius / 3
    print(f"Sfēras pilnas virsmas laukums ir {spv} bet tilpums ir {v}")
    inputs()
def kubs():
    mala = float(input("Ievadi šķautnes, jeb malas garumu: "))
    v = mala * mala * mala
    spv = mala * mala * 6
    print(f"Kuba pilnas virsmas laukums ir {spv} bet tilpums ir {v}")
    inputs()
def trijsturis():
    h = float(input("Ievadi trijstūra augstumu: "))
    a = float(input("Ievadi trijstūra malas garumu: "))
    s = a * h / 2
    print(f"Trijstūra laukums ir {s}")
    inputs()
def cikVardiTeikuma(teikums):
    skaitlis = 0
    for i in teikums:
        if i == " ":
            skaitlis += 1 
    return skaitlis
def vienkarsiBurti (teikums):
    visiburti = []
    istieBurti = []
    a = 0
    gatavais = ""
    gatavais1 = ""
    for burts in teikums:
        visiburti.append(burts)
    while a < len(visiburti):
        if visiburti[a] == "Ā" or visiburti[a] == "ā":
            istieBurti.append("a")
        elif visiburti[a] == "Č" or visiburti[a] == "č":
            istieBurti.append("c")
        elif visiburti[a] == "ē" or visiburti[a] == "Ē":
            istieBurti.append("e")
        elif visiburti[a] == "Ģ" or visiburti[a] == "ģ":
            istieBurti.append("g")
        elif visiburti[a] == "Ī" or visiburti[a] == "ī":
            istieBurti.append("i")
        elif visiburti[a] == "Ķ" or visiburti[a] == "ķ":
            istieBurti.append("k")
        elif visiburti[a] == "Ļ" or visiburti[a] == "ļ":
            istieBurti.append("l")
        elif visiburti[a] == "Ņ" or visiburti[a] == "ņ":
            istieBurti.append("n")
        elif visiburti[a] == "Š" or visiburti[a] == "š":
            istieBurti.append("s")
        elif visiburti[a] == "Ū" or visiburti[a] == "ū":
            istieBurti.append("u")
        elif visiburti[a] == "Ž" or visiburti[a] == "ž":
            istieBurti.append("z")
        elif visiburti[a] == " " or visiburti[a] == ".":
            pass
        else:
            istieBurti.append(visiburti[a])
        a += 1
    for u in istieBurti:
        gatavais += u
    gatavais1 = gatavais.lower()
    return gatavais1
def inputs():
    jamekle = ""
    koDaris = input("\n  ")
    if cikVardiTeikuma(koDaris) == 0:
        jamekle = vienkarsiBurti(koDaris)
        if meklesana(jamekle) == "sfera":
            sfera()
        elif meklesana(jamekle) == "trijsturis":
            trijsturis()
        elif meklesana(jamekle) == "kubs":
            kubs()
        elif meklesana(jamekle) == "kontrole":
            nezSaraksts()
        elif meklesana(jamekle) == "konuss":
            konus()
        elif meklesana(jamekle) == "cilindrs":
            cilindrs()
        else:
            nezinamieVardi.append(koDaris)
            irAtrasts = False
            if irAtrasts == False:
                for i in vardi:
                    if irAtrasts == False:
                        for j in vardi[i]:
                            if vaiDomaji1(koDaris, j) == True:
                                print(f"Vai tu gadījumā nedomāji {i}?")
                                irAtrasts = True
                                inputs()
                                break
            if irAtrasts == False:
                print(f"Formula priekš {koDaris} netika atrasta :(")
                inputs()
    elif cikVardiTeikuma(koDaris) == 1 or cikVardiTeikuma(koDaris) > 1:
        garakaTeikumaVienkarsosana(koDaris)
        inputs()
def vaiDomaji1(a, b):
    ierakstitaisVards = []
    panemtaisVards = []
    for burti in a:
        ierakstitaisVards.append(burti)
    for ariburti in b:
        panemtaisVards.append(ariburti)
    vardaGarums = len(ierakstitaisVards) - 2
    vardaGarums1 = 0
    for m in ierakstitaisVards:
        for n in panemtaisVards:
            if n == m:
                vardaGarums1 += 1
    if vardaGarums == vardaGarums1 or vardaGarums1 > vardaGarums:
        mainigais1 = 0
        mainigais2 = 0
        parbaude = False
        if parbaude == False:
            mainigais = 0
            mainigais_G = 0
            for g in panemtaisVards:
                mainigais = kursNummursArraja(panemtaisVards, g) + 1
                mainigais_G = kursNummursArraja(panemtaisVards, g)
                if len(ierakstitaisVards) < len(panemtaisVards):
                    if mainigais == len(ierakstitaisVards):
                        parbaude = True
                        break
                if len(panemtaisVards) < len(ierakstitaisVards):
                    mainigais2 += 1
                if parbaude == True:
                    break
                if parbaude == False:
                    if mainigais < len(ierakstitaisVards):
                        if ierakstitaisVards[mainigais_G] == panemtaisVards[mainigais_G] or ierakstitaisVards[mainigais] == panemtaisVards[mainigais_G]:
                            mainigais1 += 1
                        if mainigais1 == len(panemtaisVards) or mainigais1 > len(panemtaisVards) or mainigais1 == len(panemtaisVards) - d25procenti(panemtaisVards):
                            return True
                        else: 
                            pass
def kursNummursArraja(arrais, vajadzigaisElements):
    cipars = 0 
    cipars1 = 0
    for elementi in arrais:
        cipars += 1
        cipars1 = cipars - 1
        if elementi == vajadzigaisElements:
            cipars1 = cipars - 1
            return cipars1
def d25procenti(a):
    vardaGarums = len(a)
    desmitProcenti = vardaGarums / 10
    return int(desmitProcenti * 2.5)
inputs()
