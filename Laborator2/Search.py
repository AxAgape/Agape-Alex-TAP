list=[]
numar_elemente=input("Introdu numarul de elemente ale sirului ")
numar_elemente=int(numar_elemente)
for i in range(int(numar_elemente)):
    element=input("Introdu elementul ")
    list.append(element)
y = int(0)


cautare_numar=input("Introdu numarul pe care vrei sa il cauti ")

def find_array(list,numar_elemente):
    for i in range (numar_elemente):
        if (list[i]==cautare_numar):
            global y
            y=1
#            print("Numarul cautat se afla pe pozitia: ",i)
#            print (y)
#            return y
            break

find_array(list,numar_elemente)

if (y==1):
#    print ("Ok are valoarea: ", y)
    print("Lista sortata este ", list, " iar pozitia este ", list[i-1])
else:
#    print ("Ok are valoarea: ", y)
    print("Nu am gasit numarul")


## Cautare binara
def cautare_binara(list, cautare_numar, numar_elemente):

    global low
    global high
    low = 0
    high = numar_elemente - 1

    while (low <= high):
      
        middle = (low + high) // 2
       
        if (list[middle] == cautare_numar):
            return middle
        elif (list[middle] < cautare_numar):
            low = middle + 1
        else:
            high = middle - 1

    return -1
    

cautare_numar=input("Introdu numarul pe care vrei sa il cauti: ")
print("Numarul pe care il cauti se gaseste pe pozitia ", cautare_binara(list, cautare_numar, numar_elemente)+1)

