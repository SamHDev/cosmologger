import cosmologger

logger = cosmologger.Logger(debug=True)

logger.info("This a 'Info' Message")
logger.ok("This a 'Ok' Message")
logger.warn("This a 'Warn' Message")
logger.error("This a 'Error' Message")
logger.fatal("This a 'Fatal' Message")
logger.debug("This a 'Debug' Message")
logger("This a 'Debug' Message but Simpler")
logger.log("TEST", "This is a Custom Logging Output Type")

