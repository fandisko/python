x = int (input("Dati numarul x:"))
s = 0
p = 0
i = 0
sp = 0
si = 0
nrp = 0
nrn = x
while x != 0:
    s = s + x % 10
    if  x % 10 // 2 == 0 :
        p = p + 1
    else:
        i = i + 1
    if x % 10 % 2==0 :
        sp = sp + x % 10
    else:
        si = si + x % 10
    nrp = nrp * 10 + x % 10
    x = x // 10
print("Suma cifrelor este: ", s)
print("Avem ", p, "numere pare!")
print ("Avem ",i, "numere impare!")
print("Suma numerelor pare este:", sp)
print("Suma numerelor impare este:", si)
if nrn == nrp :
    print("Numarul este palindrom!")
else:
    print("Numarul nu este palindrom!")
