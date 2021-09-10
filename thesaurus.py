# 1. import matplotlib & pandas
from matplotlib import pyplot as plt
import pandas as pd

# 2. import data - neem pad van op je computer
thesaurus_cogent = pd.read_excel(r"#padnaardataset#\datasetTTT2.xlsx")
print(thesaurus_cogent)

# 3. select data from import

aantal_dmg = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Designmuseum Gent"].count()[0]
print(aantal_dmg)

aantal_hva = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Het Huis van Alijn"].count()[0]
aantal_stam = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "STAM"].count()[0]
aantal_im = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Industriemuseum"].count()[0]
aantal_archief = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Archief Gent"].count()[0]

# 4. piechart

slices = [aantal_im, aantal_archief, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices)
plt.show()

# 5. add label

labels = ['Industriemuseum', 'Archief Gent', 'STAM', 'Huis van Alijn', 'Designmuseum']
slices = [aantal_im, aantal_archief, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices, labels=labels)
plt.show()

# 6. add percentage

labels = ['Industriemuseum', 'Archief Gent', 'STAM', 'Huis van Alijn', 'Designmuseum']
slices = [aantal_im, aantal_archief, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices, labels=labels, autopct='%1.1f%%')
plt.show()

# 7. add colors

colors = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
labels = ['Industriemuseum', 'Archief Gent', 'STAM', 'Huis van Alijn', 'Designmuseum']
slices = [aantal_im, aantal_archief, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()

# 8. explode archief

colors = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
explode = [0,0.3,0,0,0]
labels = ['Industriemuseum', 'Archief Gent', 'STAM', 'Huis van Alijn', 'Designmuseum']
slices = [aantal_im, aantal_archief, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode)
plt.show()

# 9. angle draaien

colors = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
explode = [0,0.3,0,0,0]
labels = ['Industriemuseum', 'Archief Gent', 'STAM', 'Huis van Alijn', 'Designmuseum']
slices = [aantal_im, aantal_archief, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode, startangle=90)
plt.show()

# 10. schaduw toevoegen

colors = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
explode = [0,0.3,0,0,0]
labels = ['Industriemuseum', 'Archief Gent', 'STAM', 'Huis van Alijn', 'Designmuseum']
slices = [aantal_im, aantal_archief, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90)
plt.show()

# OEFENING Grafiek met aantallen: AAT - TGN - WIKIDATA - ONROEREND ERFGOED

# Data Selecteren
# voorbeeld voor AAT

aat = thesaurus_cogent[thesaurus_cogent["bron"].str.contains("aat", case=False, na=False)].count()[0]
print(aat)

# oefening - zoek resterende waarden en maak grafiek
