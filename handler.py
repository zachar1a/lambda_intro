from lambda_intro import common
from logzero import logger


@common.newrelic_wrapper
def lambda_handler(event=None, context = None):
	return event

	raise NotImplementedError
