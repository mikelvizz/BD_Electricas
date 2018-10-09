from elasticsearch import Elasticsearch
import datetime, json, requests, time

## Conexion con Elasticsearch
reqs = requests.get('http://localhost:9200')
print(reqs.content)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es.index(index='contador' , doc_type= 'lectura' , id =i, body={'Timestamp' : TimeStamp , 'Direccion' : 'Sarasate 47, Bajo C' , 'Consumo' : watt})
