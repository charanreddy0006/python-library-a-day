import logging

# --- configure logging ---
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

# --- different logging levels ---
logging.debug("This is a debug message")

logging.info("Program started successfully")

logging.warning("This is a warning message")

logging.error("Something went wrong")

logging.critical("Critical issue occurred")

# --- mini example ---
num = 10

if num > 5:
    logging.info("Number is greater than 5")
else:
    logging.warning("Number is small")