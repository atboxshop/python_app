# Need install RabbitMQ before using this code
import pika, sys, os
def main():
    credentials = pika.PlainCredentials('user1', 'user')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='atlaptop',virtual_host='testvhost',credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='Hello World', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)