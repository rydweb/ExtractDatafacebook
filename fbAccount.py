import csv
import operator

f=open("pseudo_facebook.csv","r")
#lire CSV et délimiter par virgule
lecteur=csv.DictReader(f,delimiter=',')

#récupérer le nombre de like
compteurlikes=0
for ligne in lecteur:
    if(int(ligne["mobile_likes"])>0):
        compteurlikes+=1
print("le nombre de personne qui font le like  est :",str(compteurlikes))

#b.	Qui a reÃ§u le maximum de Â« like Â» (entre le web like et mobile likes)?
f.seek(0)
lecteur=csv.DictReader(f,delimiter=',')
max_likes_received=0
listemax=[]
for ligne in lecteur:
    if(int(ligne["likes_received"])>max_likes_received):
        max_likes_received=int(ligne["likes_received"])
        listemax=[]
        listemax.append(ligne["userid"])
    elif(int(ligne["likes_received"])==max_likes_received):
        listemax.append(ligne["userid"])
print("les personnes qui ont reçu le max de likes",listemax)

#récupérer l,utilisateur plus d,amies
f.seek(0)
lecteur=csv.DictReader(f,delimiter=',')
max_nbre_amis=0
liste_max_amis=[]
for ligne in lecteur:
    if(int(ligne["friend_count"])>max_nbre_amis):
        max_nbre_amis=int(ligne["friend_count"])
        listemax=[]
        listemax.append(ligne["userid"])
    elif(int(ligne["friend_count"])==max_nbre_amis):
        listemax.append(ligne["userid"])
print("les personnes qui ont beaucoups d'amis",listemax)

# personne qui a eu le minimu d'amis
f.seek(0)
lecteur=csv.DictReader(f,delimiter=',')
for i, ligne in enumerate(lecteur):
    if i == 0:
        min_amis = int(ligne["friend_count"])
        continue
    if min_amis > int(ligne["friend_count"]):
        min_amis=int(ligne["friend_count"])


#les utilisateurs de facebook par le nombre d"acroissants de likes
f.seek(0)
lecteur=csv.DictReader(f,delimiter=',')

d={}
for ligne in lecteur:
    d[ligne["userid"]]=int(ligne["likes_received"])
dtrie= sorted(d.items(), key=operator.itemgetter(1),reverse=True)
print(dtrie)

# qui utilisent  le facebook
f.seek(0)
lecteur=csv.DictReader(f,delimiter=',')

d={"femmes":0,"Hommes":0}
for ligne in lecteur:
    if(ligne["gender"] in d):
        d[ligne["gender"]]+=1
print(d)

# le maximum de like
f.seek(0)
lecteur=csv.DictReader(f,delimiter=',')
d={"Nombre Max de Like pour femmes":0,"Nombre Max de Like pour hommes":0}
for ligne in lecteur:
    if(ligne["gender"] in d):
        d[ligne["gender"]] += int(ligne["likes_received"])
print(d)


#occupation la plus fréquente des personnes qui utilisent le facebook
f.seek(0)
lecteur=csv.DictReader(f,delimiter=',')
d={}
for ligne in lecteur:
    if(ligne["tenure"] not in d):
        d[ligne["tenure"]]=1
    else:
        d[ligne["tenure"]]+=1
dtrie= sorted(d.items(), key=operator.itemgetter(1),reverse=True)


print(dtrie[0])
f.close()
