liczby = [1,2,3,4,5]

# 1. Znajdź sumę wszystkich elementów
suma = 0
for i in liczby:
    suma += i
print(suma)
print(sum(liczby))

# 2. Znajdowanie minimalnego lub maksymalnego elementu na liście
maks = liczby[0]
mins = liczby[0]

for liczba in liczby:
    if liczba > maks:
        maks = liczba
    if liczba < mins:
        mins = liczba
print('Maks:', maks)
print('Min:', mins)

print('Maks: ', max(liczby))
print('Min:', min(liczby))

# 3. Sortowanie listy rosnąco
numers = [9,2,4,6,2,1,7,4,6,9,3,6]
print(sorted(numers))
