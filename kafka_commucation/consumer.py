from kafka import KafkaConsumer
from kafka_commucation.msg import Merge_Msgs


class TempConsumer:
    def __init__(self, group_id, b_s, topic_name):
        self.group_id = group_id
        self.topic_name = topic_name
        self.consumer = KafkaConsumer(topic_name,
                                      bootstrap_servers=[b_s],
                                      auto_offset_reset='earliest')

        self.Manager_Msg = Merge_Msgs()

    def getonemsg(self):
        try:
            index = 0
            for message in self.consumer:
                index += 1
                print(index, len(message.value))
                if self.Manager_Msg.putmsg(message.value):
                    return self.Manager_Msg.getcpmsg()
        except KeyboardInterrupt:
            print("Catch Keyboard interrupt")


if __name__ == "__main__":
    TC = TempConsumer('my-group', 'localhost:9092', 'test')
    onemsg = TC.getonemsg()
    f = open('pictures/2.png', 'wb')
    f.write(onemsg)
    f.close()
'''
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('test',
                         #group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest')

try:
    index = 0
    lastmsg = ""
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        #                                     message.offset, message.key,
        #                                      message.value))


        print message.value
        index += 1
        if index == 3:
            break
    
        print 'index: ',index

        index += 1
        lastmsg += message.value

        if index == 10:
            f = open('pictures/2.png', 'wb')
            f.write(lastmsg)
            f.close()
        

    for message in consumer:
        print 33333333,message.value

except KeyboardInterrupt, e:
    print "Catch Keyboard interrupt"
'''
