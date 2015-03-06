# datastax-kafka-python

This is a very simple demo which shows how to process messages from Kafka and insert them into Cassandra/DSE.


1. Setup the keyspace and table in Cassandra/DSE - please download if you don't have one already installed. Also you will need to add the python driver from - https://github.com/datastax/python-driver

```cql

CREATE KEYSPACE test WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': '1'
};

USE test;

CREATE TABLE simple (
  id text,
  message text,
  PRIMARY KEY ((id))
);

```
2. Download Kafka and install 

1. Download the Kafka binaries from Kafka download page

2. Unzip the kafka tar file by executing 
```
tar -xzf kafka_<version>.tgz. 
```
3. Go to the install direcory 
```
cd kafka_<version>
```
4. Next start the Zookeeper server by executing following command
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

5. Start the Kafka server by executing following command in new window.
```
bin/kafka-server-start.sh config/server.properties
```
3. Start the Producer Process by running 


```
python Producer.py
```

4. Start the Consumer Process by running 
```
python Consumer.py
```

NOTE - I have tested this using python version 2.7.9 on Mac OS Yosemite. 

The consumer will read the messages from the producer queue and insert them to Cassandra.

