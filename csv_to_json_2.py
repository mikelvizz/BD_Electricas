import csv
import json

# Open the CSV
f = open('/Volumes/Macintosh HD/Users/malik/PycharmProjects/BD_Electricas/Consumo_facturado_2017_2018.csv', 'rU')
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader(f, fieldnames=("CUPS", "Fecha", "Hora", "Consumo_kWh", "Metodo_obtencion"))
# Parse the CSV into JSON
out = json.dumps([row for row in reader])
print("JSON parsed!")
# Save the JSON
f = open('/Volumes/Macintosh HD/Users/malik/PycharmProjects/BD_Electricas/parsed.json', 'w')
f.write(out)
print("JSON saved!")