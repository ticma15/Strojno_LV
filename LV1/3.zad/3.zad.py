lst = []

lstCheck = 0
suma = 0

while lstCheck == 0:
    broj = input()
    if (broj.isdigit() or broj == "Done"):
        lst.append(broj)
        if (broj.isdigit()):
            suma += int(broj)

    lstCheck = lst.count("Done")

lst.pop(-1)

print("Lista: ", sorted(lst))
print("Najveci broj: ", max(lst))
print("Najmanji broj: ", min(lst))
print("Uneseno brojeva: ", len(lst))
print("Prosjecna vrijednost unesenih brojeva: ", suma/len(lst))