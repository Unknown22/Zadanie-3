"""
W czesci A zostaja wyswietlone wszystkie elementy, w ktorych wystepuja dwie takie same litery obok siebie.
W czesci B zostaja wyswietlone elementy pogrupowane wedlug dlugosci elementww
Listy mozna dowolnie edytowac

"""

list1 = ['orange', 'apple', 'banana']
list2 = ('carrot', 'potato', 'lettuce')
list3 = {'milk', 'sugar', 'butter', 'flour'}
list4 = []
list4.extend(list1)
list4.extend(list2)
list4.extend(list3)

#A part
print "Czesc A:"
for x in list4:
    letter = x[0]
    for y in x[1:]:
        if letter == y:
            print x
        letter = y

#B part
print "\nCzesc B:"
dict = {}
lista_pomocnicza = []

"""
W petli zastosowane rzutowania w celu wyswietlenia wartosci w slowniku w postaci krotki
"""
for x in list4:
    lenght = len(x)
    if (dict.has_key(lenght)):
         lista_pomocnicza = list(dict[lenght])
    lista_pomocnicza.append(x)
    dict[lenght] = tuple(lista_pomocnicza)
    lista_pomocnicza = []
print dict