#!/usr/bin/env python

import json
from cnet_downloader import download
from objects import objs

class Structure:
	START = 'start'
	END = 'end'
	EDGES = 'edges'
	REL = 'rel'

class Prefix:
	OBJ = '/c/en/'
	REL = '/r/'

BLANK = ''

def get_relationships(obj):
	print 'Getting ConceptNet Object Entry for: {}'.format(obj)
	try:
		result = download(obj)
	except NameError as e:
		print e, '\n'
		raise e
	# look for these seemingly important relations (sorted by frequency of relationship across ConceptNet)
	relations = ['IsA', 'AtLocation', 'PartOf', 'HasA', 'SimilarTo', 'ObstructedBy', 'LocatedNear']
	for edge in result[Structure.EDGES]:
		if (Prefix.OBJ not in edge[Structure.START]
			or Prefix.OBJ not in edge[Structure.END]):
			break # non english words case
		sta = edge[Structure.START].replace(Prefix.OBJ, BLANK)
		end = edge[Structure.END].replace(Prefix.OBJ, BLANK)
		rel = edge[Structure.REL].replace(Prefix.REL, BLANK)
		print sta, rel, end
	print '\n'
	

def main():
	allobjs = []
	misses = []
	# obj = objs['Furniture'][0]
	for category, category_objs in objs.iteritems():
		print '=='*10, '\n', 'Starting Category: {}'.format(category)
		for obj in category_objs:
			try:
				allobjs.append(obj)
				get_relationships(obj)
			except NameError:
				misses.append(obj)
	print 'Could not find relationships for {} of {} objects ({:04.2f}%):'.format(
			len(misses), len(allobjs), (len(misses)*100.0)/len(allobjs))
	print misses

	if 0:
		with open('conceptnet_atlocation.json') as file:
			result = json.load(file)

if __name__ == '__main__':
	main()