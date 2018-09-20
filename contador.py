from oligo import iber
from elasticsearch import Elasticsearch
import datetime, json, requests, time


count = 0

for i in range(10):

## Conectarse al contador electronico y obtener los datos de consumo.
watt = iber.watthourmeter("mvizcay@gmail.com","2Dejulio")
icpstat = iber.icpstatus("mvizcay@gmail.com","2Dejulio")

##Crear timestamp para ver a que hora se produce ese consumo
TimeStamp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
#print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())+' '+str(watt)+' '+str(icpstat))

##Genero un JSON con el formato Timestamp / Direccion / Consumo
data = {'Timestamp' : TimeStamp , 'Direccion' : 'Sarasate 47, Bajo C' , 'Consumo' : watt}
json.dumps(data)

## Conexion con Elasticsearch
#reqs = requests.get('http://localhost:9200')
#print(reqs.content)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es.index(index='contador' , doc_type= 'lectura' , id =i, body={'Timestamp' : TimeStamp , 'Direccion' : 'Sarasate 47, Bajo C' , 'Consumo' : watt})
time.sleep(3)

