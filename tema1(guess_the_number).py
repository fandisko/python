import random
generated = random.randint(0,100)
print (generated)
guess = int(input("Ghiceste numarul generat de pc intre 1 si 100:"))
while generated!=guess:
    if guess<generated:
        guess = int(input ("Caut un numar mai mare!:"))
    else:
        guess=int (input ("Caut un numar mai mic!"))
print ("Corect!")