import argparse

def parse_info():
	parser = argparse.ArgumentParser(description =
		'''
		Scrape any amazon search
		''')
	parser.add_argument('-s', '--search', required = True, metavar = '', action = 'store',
		help = '''
		What you want to scrape. Eg: Smartphones.
		''')

	return parser.parse_args()



