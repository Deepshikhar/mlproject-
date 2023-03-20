# Use logger to log every execution to keep track of everu execution in txt files

import logging
import os 
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) # Even there is folder/file keep on appending the files inside that 

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# to set the log 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
     
)

# if __name__=="__main__":
#     logging.info("Logging has started")