# utils/logger.py
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name=None, log_file='app.log', level=logging.INFO):
    """
    Set up a logger with a rotating file handler and console output.
    
    Args:
        name (str): Logger name. Use None for root logger.
        log_file (str): Path to the log file.
        level (int): Logging level, e.g. logging.INFO, logging.DEBUG.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent adding multiple handlers if this function is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()
    
    # Create formatter
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    
    # Console handler for output to stdout
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Create logs directory if not exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Rotating file handler (max 5 MB per file, keep 3 backups)
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
