from threading import Thread
from time import sleep
import logging

class UsefullClass():
    def __init__(self, second_num) -> None:
        self.delay = second_num
    def __call__(self) -> None:
        sleep(self.delay)
        logging.debug('Wake up!')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    
    t2 = UsefullClass(2)
    thread = Thread(target=t2)
    thread_locking = Thread(target=t2)
    
    thread.start()
    print('Some stuff')
    print(thread.is_alive(), thread_locking.is_alive())
    thread_locking.start()
    thread.join()
    thread_locking.join()
    print(thread.is_alive(), thread_locking.is_alive())
    print('After all...')