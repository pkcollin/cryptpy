#exchange_apis.py

from bittrex.bittrex import *

def digest_config(strat_config):
	strat_config = open(strat_config, "r")
	strat_text = strat_config.readlines()
	strat_attributes = {}
	for line in strat_text:
		if not line.startswith("#") and not line.strip() == (""):
			splitted_line = line.split("=")
			# First argument in the line is the key, and the second is the value
			strat_attributes[splitted_line[0]] = splitted_line[1].strip()
	return strat_attributes