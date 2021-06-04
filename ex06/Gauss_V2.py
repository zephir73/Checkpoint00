
hist = "Ok, bon laissez moi tout de même vous la raconter.\n\nLe petit Carl Friedrich Gauss était un peu dissipé en classe.\n\nLe maître agacé, par l'agitation de sa classe décida,\n\n de calmer sa classe à coup d'interrogation surprise.\n\nComme tout bon instituteur qui se respecte !\n\n"
hist2 ="Très écoutez attentivement la suite.\n\nL'instituteur posa le problème suivant :\n\nQue vaut la somme de tous les nombre de 1 à 100 ?\n\nL'instituteur pensant avoir un long moment de répit,\n\nentendit la petite voix de Carl dire timidement '5050...'\n\nStupéfait de l'exactitude du résultat, il lui donna une autre punition à accomplir...\n\nLa dernière ligne est purement fictive.\n"
hs = 0

quest1 = input("Bonjour, connaissez vous la légende du petit Gauss ?\n\nOui / Non\n\n")

if (quest1 == "Oui" or quest1 == "oui") :
  print (f"Super !\n\n{hist}")
  quest2 = input("Cela vous offusque ?\n\nOui / Non\n\n")

elif (quest1 == "Non" or quest1 == "non") :
  print (f"Google est vôtre ami, ou demandez à Igor.\n{hist}")
  quest2 = input("Cela vous offusque ?\n\nOui / Non\n\n")

else : 
  hs = 1
  print (f"Oui ou Non, c'etait plus simple comme choix de réponse ...\n\n{hist}")
  quest2 = input("Cela vous offusque ?\n\nOui / Non\n\n")

if (quest2 == "Oui" or quest2 == "oui") :
  print ("Mangez une pomme c\'est bon pour la santé ...\n\n" + "\x1b[6;31;40m" + "Elle est loin l\'époque ou l\'on pouvait mettre des fessées ..." + "\x1b[0m")

elif (quest2 == "Non" or quest2 == "non") :
  print (hist2)

else :
  if hs != 0 :
    print (f"Oui ou Non, c'etait plus simple comme choix de réponse ...\n\n")
    print ("C'est la deuxième fois que vous ne répondez pas.\n\n" + "\x1b[6;31;40m" +  "Vous me prenez pour un imbécile à répondre à côté de la plaque, au revoir !"  + "\x1b[0m")
  else : 
    print (f"Oui ou Non, c'etait plus simple comme choix de réponse ...\n\n")
    print (hist2)
