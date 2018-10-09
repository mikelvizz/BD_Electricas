import csv
import json

csvfile = open('Consumo_facturado_2017_2018.csv', 'r')
jsonfile = open('file2.json', 'w')

fieldnames = ("CUPS","Fecha","Hora","Consumo_KWh","Metodo_Obtencion")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')