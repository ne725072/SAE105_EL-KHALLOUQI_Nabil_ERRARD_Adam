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
    if conso_corrigee[i] == 'NA' :
       i_supr.append(i)
     
for i in range(len(i_supr)-1,1,-1) :
    
    del conso_corrigee[i_supr[i]]
    del maille[i_supr[i]]
    del dates[i_supr[i]]
    del semaines[i_supr[i]]
    del annees[i_supr[i]]
    del donnees[i_supr[i]]
               
               
for i in range(len(conso_corrigee)):
        conso_corrigee[i] = conso_corrigee[i].replace(",",".")
        conso_corrigee[i] = float(conso_corrigee[i])
        print(conso_corrigee[i])

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
    
for i in range(len(dates)):
    dates[i] = dates[i].split('-')
        
dates_2024 = []
dates_2025 = []     

for i in range(len(dates)):
    for j in dates[i]:
        if dates[i][0] == '2024':
            dates_2024.append(dates[i])
        if dates[i][0] == '2025':
            dates_2025.append(dates[i])




'''
pylab.figure()
pylab.plot()
pylab.plot()
pylab.legend()
pylab.show()
'''
