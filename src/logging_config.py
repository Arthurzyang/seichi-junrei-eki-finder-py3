import logging
import os

def configureLogging():
    logDir = "../Logs"
    if not os.path.exists(logDir):
        os.makedirs(logDir)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(logDir, "station_query_example.log"), encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)