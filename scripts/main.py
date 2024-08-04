import logger
import platform

log = logger.get_logger(f'{platform.node()}')
log.info('Something went wrong')
