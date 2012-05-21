
# PYTHONPATH=src python examples/basic.py

import tornado.ioloop as ioloop
from tornado.smtp.client import SMTPClient

def send_test():
    client = SMTPClient('localhost', 25)
    body = "Subject: Testing\n\nJust a test"
    client.send('foo@example.com', ['recipient@example.com'], body, callback=sent_test)

def sent_test(success, error_msg=None):
    if success:
        print "Sent OK"
    else:
        print "Failed to send : " + str(error_msg)
    ioloop.IOLoop.instance().stop()

send_test()
ioloop.IOLoop.instance().start()

