from loguru import logger

# Console logs
logger.debug("This is a debug message.")
logger.info("Application started.")
logger.success("Operation completed successfully!")
logger.warning("This is a warning.")
logger.error("An error occurred.")
logger.critical("Critical issue detected!")

# Save logs to a file
logger.add("app.log")

logger.info("This message is also saved to app.log")