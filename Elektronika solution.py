#//Program za resavanje tebele iz elektronike na VISERU\\
#By Nosferatu#################################666########

print("Izabrati zadatu vrednost Ui(V)\n12V 17V 24V\n")
while(1):
    zad_v = str(input())
    if zad_v == "12" or zad_v == "17" or zad_v == "24":
        break
    else:
        print("Los unos!Ponovo!")
print("Uneti 10 brojeva za PTC zatim 10 za NTC Izmerenih vrednosti U0(V)." +
      "\nDecimalni brojevi se pisu npr:5.80\nInput moraju biti brojevi!!")
brojac = 1
lista_IPTC = []
lista_UtPTC = []
lista_RtPTC = []
while(brojac < 11):
    print(str(brojac) + ":", end = " ")
    broj = str(input())
    brojac = brojac + 1
    Ut = float(zad_v) - float(broj)
    Rt = Ut / float(broj)
    lista_IPTC.append(str(broj))
    lista_UtPTC.append(str(Ut))
    lista_RtPTC.append(str(Rt))
    print("I(mA) PTC:" + str(broj))
    print("Ut(V) PTC:" + str(Ut))
    print("Rt(Ω) PTC:" + str(Rt))
    
lista_INTC = []
lista_UtNTC = []
lista_RtNTC = []
brojac = 1
print("Sada uneti NTC vrednosti.")
while(brojac < 11):
    print(str(brojac) + ":", end = " ")
    broj = str(input())
    brojac = brojac + 1
    Ut = float(zad_v) - float(broj)
    Rt = Ut / float(broj)
    lista_INTC.append(str(broj))
    lista_UtNTC.append(str(Ut))
    lista_RtNTC.append(str(Rt))
    print("I(mA) NTC:" + str(broj))
    print("Ut(V) NTC:" + str(Ut))
    print("Rt(Ω) NTC:" + str(Rt))
print("----------------Rezultati---------------------------")
print("I(mA)\nPTC za zadatu vrednost od " + str(zad_v) + ":")
brojac = 1
for i in (lista_IPTC):
    print(str(brojac) + ":" + i)
    brojac = brojac + 1
print("-----------------------------")    
print("Ut(V)\nPTC" + str(zad_v) + ":")
brojac = 1
for i in (lista_UtPTC):
    print(str(brojac) + ":" + i)
    brojac = brojac + 1
print("-----------------------------")     
print("Rt(Ω)\nPTC" + str(zad_v) + ":")
brojac = 1
for i in (lista_RtPTC):
    print(str(brojac) + ":" + i)
    brojac = brojac + 1
print("-----------------------------")     
print("I(mA)\nNTC" + str(zad_v) + ":")
brojac = 1
for i in (lista_INTC):
    print(str(brojac) + ":" + i)
    brojac = brojac + 1
print("-----------------------------")     
print("Ut(V)\nNTC" + str(zad_v) + ":")
brojac = 1
for i in (lista_UtNTC):
    print(str(brojac) + ":" + i)
    brojac = brojac + 1
print("-----------------------------")     
print("Rt(Ω)\nNTC" + str(zad_v) + ":")
brojac = 1
for i in (lista_RtNTC):
    print(str(brojac) + ":" + i)
    brojac = brojac + 1
print("-----------------------------------------------------")    
print("Iznad su sva resenja za tu odradjenu zadatu vrednost!") 
kraj = input("Pritisni ENTER za EXIT :)")    

      
