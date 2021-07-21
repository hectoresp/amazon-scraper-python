import xlsxwriter

def convert_data(titles, prices, links, ratings):
	row = 1
	workbook = xlsxwriter.Workbook('scraped_data.xlsx')

	worksheet = workbook.add_worksheet()

	worksheet.write('A1', 'Title')
	worksheet.write('B1', 'Price')
	worksheet.write('C1', 'Rating')
	worksheet.write('D1', 'Link')

	for title in titles:
		worksheet.write(row, 0, title)
		row += 1
	else:
		row = 1
	for price in prices:
		
		price = price.replace(' €', '').replace('.', '').replace(',', '.')
		cell_format = workbook.add_format()
		if 0.00 < float(price) < 300.00:
			cell_format.set_bg_color('green')
		if 300.00 < float(price) < 600.00:
			cell_format.set_bg_color('yellow')
		if 600.00 < float(price):
			cell_format.set_bg_color('red')
		
		worksheet.write(row, 1, str(price) + ' €', cell_format)

		row += 1

	else:
		row = 1

	for link in links:
		worksheet.write(row, 3, link)
		row += 1

	else:
		row = 1

	for rating in ratings:
		if rating != 'Not avaible':
			rating = rating.replace('de', '/').replace(',', '.').replace(' ', '')
			is_good = rating.split('/')
			is_good[0] = float(is_good[0])
			cell_format_2 = workbook.add_format()
			if 2 > is_good[0] > 0:
				cell_format_2.set_bg_color('red')
			if 4 > is_good[0] > 3:
				cell_format_2.set_bg_color('yellow')
			else:
				cell_format_2.set_bg_color('green')
			worksheet.write(row, 2, rating, cell_format_2)
		else:
			worksheet.write(row, 2, rating)
		row += 1
	else:
		row = 1

	workbook.close()