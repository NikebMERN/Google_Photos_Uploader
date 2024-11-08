import logging

def setup_logger(log_file='logs/upload.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

# Initialize logger
logger = setup_logger()
