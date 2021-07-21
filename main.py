from parse import parse_info
from scrape import scrape_info
from converter import convert_data
from notify import notifier

if __name__ == '__main__':
	try:
		args = parse_info()
		notifier('Scraping...', f'The scraper is now looking for "{args.search}" articles, please wait.', 'loading.ico')
		titles, prices, links, ratings = scrape_info(args.search)
		print(ratings)
		convert_data(titles, prices, links, ratings)
		notifier('Finished', f'The program has just finished. Take a look to the Excel file (scraped_data.xlsx).', 'finished.ico')
	except:
		notifier('Error', 'An error has occurred, the program has finished.', 'error.ico')



