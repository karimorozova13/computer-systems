from threading import Thread
from time import sleep
import logging

def example_work(params):
    sleep(params)
    logging.debug("Wake up!")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    logging.debug('Start program')
    threads = []
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]

    logging.debug('End program')
