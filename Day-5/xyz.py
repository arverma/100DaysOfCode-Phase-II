# Create an in-memory pub-sub library
# Requirements:
# 1.There can be multiple queues maintained by the library.
# 2.Each queue must support multiple producers and consumers.
#
# 3.Each message has a maximum retention period (configured per queue) beyond which it should not reside in memory.
# 4.A message can be published with a TTL to a queue. Any message with expired TTL should not be consumed by any
# consumer and should not reside in the memory as well. 5.Consumers should be able to reset its offset value to
# start/end of the queue. In Memory Queue: Pub/Sub: ---------------------------------------- P1 --> 	|  1  |  2  |
# 3  |  4  |  5  |     |       ---> consumer 1 ----------------------------------------        ---> consumer 2 --->
# consumer 3 Key Points: One Producer produces to the single queue, but consumer can be multiple Ordering: P1--> 1,
# 2, 3 C1 --> 1, 2, 3 C2 --> 1, 2, 3 C3 --> 1, 2, 3 Consumer Offset Reset: start, end Eliminations: Max time based
# elimnation: 1hour [will be deleted from the queue automatically] Message can come with it's own TTL [time to live]:
# M1 --> ttl    : 60sec M2 --> ttl    : 300 sec M3 --> No ttl : till max retention period

import time


class Node:
    def __init__(self, message):
        self.head = message
        self.next = None


def traverse_topic(topics, topic_name):
    temp = topics.get(topic_name)
    while temp.next:
        print(temp.head)
        temp = temp.next
    print(temp.head)


def publish_message(topics, topic_name, message, ttl, start_time):
    """
    {
        ""topic_1" : a -> b -> c
    }
    """
    head = topics.get(topic_name)
    if head is None: #
        topics[topic_name] = Node((message, start_time, ttl))
    else:
        new_node = Node((message, start_time, ttl))
        while head.next:
            head = head.next
        head.next = new_node
    return topics


def consume_message(topics, topic_name, c_name, consumers):
    message_head = topics.get(topic_name)
    offset = consumers.get(c_name)
    if offset is None:  # Means new consumer
        consumers[c_name] = message_head  # set offset to the 0
        start_from = message_head
    else:
        start_from = offset

    # message_details = message_head.head
    # print("time", datetime.datetime.now() - message_details[2])

    while start_from.next:
        message_details = start_from.head
        print("time", time.time() - message_details[2])
        if time.time() - message_details[2] <= message_details[1]:
            print("Consumed for consumer {}: {}".format(c_name, message_head.head))
        start_from = start_from.next
    consumers[c_name] = start_from
    return consumers


def ttl_func(topics):
    for topic in topics:
        message_head = topics.get(topic)
        if message_head:
            message_details = message_head.head
            if time.time() - message_details[2] > message_details[1]:
                message_head = message_head.next

        while message_head.next:
            message_details = message_head.next.head
            if time.time() - message_details[2] > message_details[1]:
                message_head.next = message_head.next.next
            else:
                message_head = message_head.next
    return topics


if __name__ == '__main__':
    ttl = 10  # In sec
    topics = publish_message({}, "topic_1", "m1", ttl, time.time())
    topics = publish_message(topics, "topic_1", "m2", ttl, time.time())
    traverse_topic(topics, "topic_1")

    consumers = consume_message(topics, "topic_1", "c1", {})
    print(consumers)

    ttl_func(topics)

    topics = publish_message(topics, "topic_2", "m3", ttl, time.time())
    traverse_topic(topics, "topic_1")
    traverse_topic(topics, "topic_2")
    print(topics)
