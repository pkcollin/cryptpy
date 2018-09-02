#!/usr/bin/env python
# exchange.py

import click
from exchange_apis import *


class Exchange(object):
	def __init__(self, config_file):
		print "Config initialization of exchange object not implemented yet"

	def __init__(self, exchange_name, username, password):
		self.exchange_name = exchange_name
		self.username = username
		self.password = password

	def __init__(self, exchange_name, apikey, apisecret):
		self.exchange_name = exchange_name
		self.apikey = apikey
		self.apisecret = apisecret

	def __init__(self, exchange_name, prod):
		self.exchange_name = exchange_name
		if prod == True:
			self.apikey = apikey
			self.apisecret = apisecret
		else:
			print "not prod?"

def get_api_key(exchange_name, prod):

