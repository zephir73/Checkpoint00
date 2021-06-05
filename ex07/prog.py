
nbrInput = int(input ("Quel est votre nombre ? :\n"))

def gaus(nbr_input):
	nbr = 1
	nbrSomme = 1
	while (nbr < nbr_input) :
		nbr += 1
		nbrSomme += nbr

	print (f"Nous allons calculer la somme de tous les nombre de 1 jusqu'à {nbr_input}\nLe résultat est {nbrSomme}")

gaus(nbrInput)
