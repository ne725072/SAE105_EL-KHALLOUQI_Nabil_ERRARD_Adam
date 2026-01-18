import csv
import pylab

maille = []
dates = []
conso_corrigee = []
semaines = []
annees = []
donnees = []

with open('Consommation.csv',newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=';')
    for row in reader:
        
        maille.append(row[0])
        dates.append(row[1])
        semaines.append(row[3])
        annees.append(row[4])
        donnees.append(row[5])
        conso_corrigee.append(row[6])

del maille[0]
del dates[0]
del semaines[0]
del annees[0]
del donnees[0]
del conso_corrigee[0]

i_supr = []

for i in range(len(conso_corrigee)):
    if 'NA' in conso_corrigee[i]:
       i_supr.append(i)
     
for i in range(len(i_supr)-1,-1,-1) :
    
    del conso_corrigee[i_supr[i]]
    del maille[i_supr[i]]
    del dates[i_supr[i]]
    del semaines[i_supr[i]]
    del annees[i_supr[i]]
    del donnees[i_supr[i]]
            
for i in range(len(conso_corrigee)):
        conso_corrigee[i] = conso_corrigee[i].replace(",",".")
        conso_corrigee[i] = float(conso_corrigee[i])


indice_quotidien = []
indice_hebdo = []

for i in range(len(maille)):
    if maille[i] == "jour":
        indice_quotidien.append(i)
    else:
        indice_hebdo.append(i)
        
        
conso_corrigee_quotidien = []

for i in indice_quotidien :
    conso_corrigee_quotidien.append(conso_corrigee[i])
    
conso_corrigee_hebdo = []

for i in indice_hebdo :
    conso_corrigee_hebdo.append(conso_corrigee[i])
            
indice_2025 = []
for i in range(len(dates)):
    if dates[i][0] == '2025':
        indice_2025.append(i)

for i in range(len(dates)):
    dates[i] = dates[i].split('-')

dates_2025_hebdo = []
conso_2025_hebdo = []

for i in range(len(dates)):
    if i in indice_hebdo and dates[i][0] == '2025':
        dates_2025_hebdo.append(dates[i])

for i in range(len(conso_corrigee_hebdo)):
    if dates[i][0] == '2025':
        conso_2025_hebdo.append(conso_corrigee_hebdo[i])

liste = []

for i in range(len(dates_2025_hebdo)):
    temp = int(dates_2025_hebdo[i][0] + dates_2025_hebdo[i][1] + dates_2025_hebdo[i][2])
    liste.append([temp, dates_2025_hebdo[i], conso_2025_hebdo[i]])

liste.sort()

dates_2025_hebdo_triee = []
conso_2025_hebdo_triee = []

for i in range(len(liste)):
    dates_2025_hebdo_triee.append(liste[i][1])
    conso_2025_hebdo_triee.append(liste[i][2])
    
for i in range(len(dates_2025_hebdo_triee)):
    dates_2025_hebdo_triee[i] = dates_2025_hebdo_triee[i][0] + '-' + dates_2025_hebdo_triee[i][1] + '-' + dates_2025_hebdo_triee[i][2] 

dates_hiver = []
conso_hiver = []

dates_ete = []
conso_ete = []

dates_automne = []
conso_automne = []

dates_printemps = []
conso_printemps = []

for i in range(len(dates_2025_hebdo_triee)):
    ele = dates_2025_hebdo_triee[i].split("-")
    for j in range(len(ele)):
        
        if ele[1] == "01" or ele[1] == "02" or ele[1] == "12":
            dates_hiver.append(dates_2025_hebdo_triee[i])
            conso_hiver.append(conso_2025_hebdo_triee[i])
            
        if ele[1] == "03" or ele[1] == "04" or ele[1] == "5":
            dates_printemps.append(dates_2025_hebdo_triee[i])
            conso_printemps.append(conso_2025_hebdo_triee[i])
            
        if ele[1] == '06' or ele[1] == '07' or ele[1] == '08':
            dates_ete.append(dates_2025_hebdo_triee[i])
            conso_ete.append(conso_2025_hebdo_triee[i])

        if ele[1] == '09' or ele[1] == '10' or ele[1] == '11':
            dates_automne.append(dates_2025_hebdo_triee[i])
            conso_automne.append(conso_2025_hebdo_triee[i])
            
#--------------------------------------------------------------------------------------------------------------------------------------------------------

dates_février_2025 = []
conso_février_2025 =[]

for i in range(len(dates)):
    if i in indice_quotidien and dates[i][0] == '2025' and dates[i][1] == '02':
        dates_février_2025.append(dates[i])
        conso_février_2025.append(conso_corrigee[i])

liste = []

for i in range(len(dates_février_2025)):
    tri_valeurs = int(dates_février_2025[i][0] + dates_février_2025[i][1] + dates_février_2025[i][2])
    liste.append([tri_valeurs, dates_février_2025[i], conso_février_2025[i]])
    
liste.sort()

dates_février_2025_triee = []
conso_février_2025_triee = []

for i in range(len(liste)):
    dates_février_2025_triee.append(liste[i][1])
    conso_février_2025_triee.append(liste[i][2])
    
for i in range(len(dates_février_2025_triee)):
    dates_février_2025_triee[i] = dates_février_2025_triee[i][0] + '-' + dates_février_2025_triee[i][1] + '-' + dates_février_2025_triee[i][2]
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------    
    
dates_avril_2025 = []
conso_avril_2025 =[]

for i in range(len(dates)):
    if i in indice_quotidien and dates[i][0] == '2025' and dates[i][1] == '04':
        dates_avril_2025.append(dates[i])
        conso_avril_2025.append(conso_corrigee[i])

liste = []

for i in range(len(dates_avril_2025)):
    tri_valeurs = int(dates_avril_2025[i][0] + dates_avril_2025[i][1] + dates_avril_2025[i][2])
    liste.append([tri_valeurs, dates_avril_2025[i], conso_avril_2025[i]])
    
liste.sort()

dates_avril_2025_triee = []
conso_avril_2025_triee = []

for i in range(len(liste)):
    dates_avril_2025_triee.append(liste[i][1])
    conso_avril_2025_triee.append(liste[i][2])
    
for i in range(len(dates_avril_2025_triee)):
    dates_avril_2025_triee[i] = dates_avril_2025_triee[i][0] + '-' + dates_avril_2025_triee[i][1] + '-' + dates_avril_2025_triee[i][2]
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------    

dates_octobre_2025 = []
conso_octobre_2025 =[]

for i in range(len(dates)):
    if i in indice_quotidien and dates[i][0] == '2025' and dates[i][1] == '10':
        dates_octobre_2025.append(dates[i])
        conso_octobre_2025.append(conso_corrigee[i])

liste = []

for i in range(len(dates_octobre_2025)):
    tri_valeurs = int(dates_octobre_2025[i][0] + dates_octobre_2025[i][1] + dates_octobre_2025[i][2])
    liste.append([tri_valeurs, dates_octobre_2025[i], conso_octobre_2025[i]])
    
liste.sort()

dates_octobre_2025_triee = []
conso_octobre_2025_triee = []

for i in range(len(liste)):
    dates_octobre_2025_triee.append(liste[i][1])
    conso_octobre_2025_triee.append(liste[i][2])
    
for i in range(len(dates_octobre_2025_triee)):
    dates_octobre_2025_triee[i] = dates_octobre_2025_triee[i][0] + '-' + dates_octobre_2025_triee[i][1] + '-' + dates_octobre_2025_triee[i][2]

#--------------------------------------------------------------------------------------------------------------------------------------------------------

dates_juillet_2025 = []
conso_juillet_2025 =[]

for i in range(len(dates)):
    if i in indice_quotidien and dates[i][0] == '2025' and dates[i][1] == '07':
        dates_juillet_2025.append(dates[i])
        conso_juillet_2025.append(conso_corrigee[i])

liste = []

for i in range(len(dates_juillet_2025)):
    tri_valeurs = int(dates_juillet_2025[i][0] + dates_juillet_2025[i][1] + dates_juillet_2025[i][2])
    liste.append([tri_valeurs, dates_juillet_2025[i], conso_juillet_2025[i]])
    
liste.sort()

dates_juillet_2025_triee = []
conso_juillet_2025_triee = []

for i in range(len(liste)):
    dates_juillet_2025_triee.append(liste[i][1])
    conso_juillet_2025_triee.append(liste[i][2])
    
for i in range(len(dates_juillet_2025_triee)):
    dates_juillet_2025_triee[i] = dates_juillet_2025_triee[i][0] + '-' + dates_juillet_2025_triee[i][1] + '-' + dates_juillet_2025_triee[i][2]
    
    
'''
pylab.figure()
pylab.plot(dates_2025_hebdo_triee, conso_2025_hebdo_triee, label = 'Consommation hebdomadaire 2025')
pylab.xticks(dates_2025_hebdo_triee[::4], rotation=45)
pylab.legend()
pylab.show()


pylab.figure()
pylab.plot(dates_hiver, conso_hiver, label='Hiver', color='blue')
pylab.plot(dates_printemps, conso_printemps, label='Printemps', color='green')
pylab.plot(dates_ete, conso_ete, label='Été', color='orange')
pylab.plot(dates_automne, conso_automne, label='Automne', color='brown')
pylab.legend()
pylab.xticks(dates_2025_hebdo_triee[::4], rotation=45)
pylab.xlabel("Date")
pylab.ylabel("Consommation corrigée")
pylab.title("Consommation hebdomadaire 2025 par saison")
pylab.show()
'''

#------------------------------------------------------------------------------------------------------------------------------------------

'''
pylab.figure()
pylab.plot(dates_février_2025_triee, conso_février_2025_triee, label = 'Consommation février 2025')
pylab.xticks(dates_février_2025_triee[::4], rotation=45)
pylab.legend()
pylab.show()
'''

#------------------------------------------------------------------------------------------------------------------------------------------

'''
pylab.figure()
pylab.plot(dates_avril_2025_triee, conso_avril_2025_triee, label = 'Consommation avril 2025')
pylab.xticks(dates_avril_2025_triee[::4], rotation=45)
pylab.legend()
pylab.show()
'''

#------------------------------------------------------------------------------------------------------------------------------------------

'''
pylab.figure()
pylab.plot(dates_octobre_2025_triee, conso_octobre_2025_triee, label = 'Consommation octobre 2025')
pylab.xticks(dates_octobre_2025_triee[::4], rotation=45)
pylab.legend()
pylab.show()
'''

#------------------------------------------------------------------------------------------------------------------------------------------

'''
pylab.figure()
pylab.plot(dates_juillet_2025_triee, conso_juillet_2025_triee, label = 'Consommation juillet 2025')
pylab.xticks(dates_juillet_2025_triee[::4], rotation=45)
pylab.legend()
pylab.show()
'''

#------------------------------------------------------------------------------------------------------------------------------------------

jours = []
for i in range(1,29):
    jours.append(i)
    
conso_28_février = conso_février_2025_triee[0:28]
conso_28_avril = conso_avril_2025_triee[0:28]    
conso_28_juillet = conso_juillet_2025_triee[0:28]    
conso_28_octobre = conso_octobre_2025_triee[0:28]

'''
pylab.figure()
pylab.plot(jours, conso_28_février, label='Février (hiver)')
pylab.plot(jours, conso_28_avril, label='Avril (printemps)')
pylab.plot(jours, conso_28_juillet, label='Juillet (été)')
pylab.plot(jours, conso_28_octobre, label='Octobre (automne)')
pylab.xlabel("Jour du mois (1 à 28)")
pylab.ylabel("Consommation corrigée")
pylab.title("Comparaison : un mois par saison (jours 1 à 28)")
pylab.legend()
pylab.show()
'''

#------------------------------------------------------------------------------------------------------------------------------------------