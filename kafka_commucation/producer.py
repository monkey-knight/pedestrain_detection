from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka_commucation.msg import Split_Msgs


class TempProducer:

    def __init__(self, b_s, topicname):
        self.topic_name = topicname
        self.producer = KafkaProducer(bootstrap_servers=[b_s])

    # producer complete msgs
    def p_cpmsg(self, cpmsg, Msg_Name):
        Manager_Msg = Split_Msgs(cpmsg, Msg_Name)
        Will_Send_Msgs = Manager_Msg.getmsglist()

        for one_msg in Will_Send_Msgs:
            self.producer.send(self.topic_name, one_msg)

        self.producer.flush()


if __name__ == "__main__":
    TP = TempProducer('localhost:9092', 'test')
    f = open('pictures/6.png', 'rb')
    u = f.read()
    TP.p_cpmsg(u, '6.png')

'''
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

f = open('pictures/6.png', 'rb')
u = f.read()
piclen = len(u)
onelen = piclen//10
lastlen = onelen + piclen%10

future = ''
for i in range(9):
    print i
    tempu = u[i * onelen:(i+1) * onelen]
    future = producer.send('test', str(i))

tempu = u[9*onelen:]
#future = producer.send('test', tempu)

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    pass

producer.flush()

for i in range(10,15):
    print i
    producer.send('test', str(i))


producer.flush()
'''
