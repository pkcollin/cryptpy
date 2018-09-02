#runStrat.py

import click
import sys
from exchange_apis import *


@click.command()
@click.option('--strat-config', help='The configuration file with information for the strategy')
@click.option('--prod', default = True, help = 'Whether or not thins is using live money')
def run_strat(strat_config, prod):
	'''
	Goes into the strategy configuration file
	And takes in exchange information
	And command information
	And exexutes the strategy
	Password and username information stored on a NON
	git file - found in the strategy config file
	'''
	strat_attributes = digest_config(strat_config)
	'''
	Dictonary of Attributes can be:
	Exchange
	username
	password
	command
	'''
	exchanges = []
	for exchange in strat_attributes['exchanges']:
		# ex = Exchange(exchange.)
		# exchanges.append(ex)
		pass

# def digest_config(strat_config):
# 	strat_config = open(strat_config, "r")
# 	strat_text = strat_config.readlines()
# 	strat_attributes = {}
# 	for line in strat_text:
# 		if not line.startswith("#") and not line.strip() == (""):
# 			splitted_line = line.split("=")
# 			# First argument in the line is the key, and the second is the value
# 			strat_attributes[splitted_line[0]] = splitted_line[1].strip()
# 	return strat_attributes

def main():
	run_strat()

if __name__ == '__main__':
    main()
