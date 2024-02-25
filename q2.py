from random import randint
def turtle():
    return randint(2,6)
def rabbit():
    return randint(4,8)
tur = 0 
rab = 0
for i in range(12):
    i += 1
    if i == 5 or i == 10:
        tur += turtle()
        tur += turtle()
        print(f"Round {i}")
        print("-"*tur, end= " ")
        print(f"Turtle ({tur})")
        print("-"*rab, end= " ")
        print(f"Rabit ({rab})")
    else:
        tur += turtle()
        rab += rabbit()
        print(f"Round {i}")
        print("-"*tur, end= " ")
        print(f"Turtle ({tur})")
        print("-"*rab, end= " ")
        print(f"Rabit ({rab})")
if tur > rab:
    print("Turtle wins!")
elif rab > tur:
    print("Rabbit wins!")
elif rab == tur:
    print("It's a tie.")
    
