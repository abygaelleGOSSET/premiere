#Exo 2
velibs={"id":1210 , "typ":"éléctrique" ,"station":"Place d'Italie" ,"statut":"en panne"}
velibs["statut"]="En déplacement"
##"dispo" in velibs.values

#Exo 2bis
vélo1={"id":1210 , "typ":"éléctrique" ,"station":"Place d'Italie" ,"statut":"en panne"}
vélo2={"id":7596 , "typ":"classique" ,"station":"Gare" ,"statut":"dispo"}
vélo3={"id":5236 , "typ":"éléctrique" ,"station":"Boileau" ,"statut":"dispo"}

parc_velib=[]
parc_velib.append((vélo1,vélo2,vélo3))

def recherche_velo(parc):
    r=None
    for v in parc:
        if v["statut"]=="dispo":
            r+=v["station"]
    return r

print(recherche_velo(parc_velib))