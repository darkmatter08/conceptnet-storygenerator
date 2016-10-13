#!/usr/bin/env python

import json
import urllib2
import argparse

DEBUG = 1

CONCEPTNET_PREFIX = 'http://conceptnet5.media.mit.edu/data/5.3/c/en/'

def download(item):
	# replace spaces with underscores
	item = item.replace(' ', '_')
	# to lower case
	item = item.lower()

	# read from website
	data = urllib2.urlopen(CONCEPTNET_PREFIX + item)
	result = json.load(data)

	# validate whether or not there is actually data in the retuned JSON
	if result['numFound'] == 0:
		raise NameError('No results on ConceptNet for: {}'.format(item))

	return result

if __name__ == '__main__':
	if 0: # valid inputs
		print download('bathroom_cabinet')
		print download('bathroom cabinet')
	if 0: # bad inputs
		print download('bathroomXXXcabinet') # bad input
		print download('FAKEALLFAKEALL')

	parser = argparse.ArgumentParser()
	parser.add_argument('item', help='The item to download from ConceptNet5')
	args = parser.parse_args()
	print download(args.item)
