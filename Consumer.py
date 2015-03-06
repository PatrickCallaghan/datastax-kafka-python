from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
import datetime
import time

cluster = Cluster()
session = cluster.connect('test')

user_insert_stmt = session.prepare("insert into simple (id, message) values (?,?)");
 
kafka = KafkaClient("localhost:9092")
 
print("After connecting to kafka")
 
consumer = SimpleConsumer(kafka, "test-group", "cassandratest")
 
def insert(message):
	print (message.message.value)
	
	return session.execute(user_insert_stmt, [str(datetime.datetime.now()), message.message.value])
 
for message in consumer:
	insert (message)
    
 
