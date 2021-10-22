import logging

# Build and config the logger
logging.basicConfig(filename = "main.log",
                   format = "%(asctime)s %(message)s",
                   filemode = "w")

# set an object for the logger
new_logger = logging.getLogger()

# set threshold to debug
new_logger.setLevel(logging.DEBUG)

# Test Messages for that log
new_logger.debug("This is a Harmless debug message")
new_logger.info("Information message")
new_logger.warning("A warning message")
new_logger.error("This is an error message")
new_logger.critical("No Internet, Internet is down now")