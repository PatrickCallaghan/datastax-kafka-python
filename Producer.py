from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime
from time import sleep
 
kafka =  KafkaClient("localhost:9092")
 
producer = SimpleProducer(kafka)
 
 
while True:
	message = "<xml><messagetype>email</messagetype><time>" + str(datetime.now().time()) + "</time></xml>";
	producer.send_messages("cassandratest", message )
	print message
	sleep(50/1000)

