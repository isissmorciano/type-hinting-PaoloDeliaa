import random 
#ESERCIZIO 1
def descrizione(nome: str, eta: int) -> str: 
    return f"{nome} ha {eta} anni."


#ESERCIZIO 2
def numero_casuale() -> int: 
    return random.randint(0, 99)

#ESERCIZIO 3
def descrizione_eta_casuale(nome: str) -> str: 
    eta = numero_casuale()
    return "{} ha {} anni." .format(nome, eta)


#ESERCIZIO 4
def  descrizione_casuale() -> str:
    nomi= ["Trent", "Phil", "Enry", "Catia", "Nicola" ]
    nome = random.choice(nomi)
    eta = numero_casuale()
    return descrizione(nome, eta)

print(descrizione("Trent", 23)) 
print(numero_casuale())
print(descrizione_eta_casuale("Trent")) 
print(descrizione_casuale())




