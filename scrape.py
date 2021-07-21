from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

from parse import parse_info

titles = []
prices = [] #Hacer scraper que scrapee mensajes de twitch y segun que mensajes ejecutar comandos en tu pc jaja un saludo tremendo bot
links = []
ratings = []
page = 0

def scrape_info(url):
	global page

	driver = webdriver.Chrome(r'C:\chromedriver.exe')
	driver.get('https://www.amazon.com/s?k=' + str(url))
	driver.minimize_window()
	for j in range(100):
		try:
			num_pages = driver.find_element_by_xpath(
				'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[' + str(j) +']/span/div/div/ul/li[6]').text

		except:
			continue
	
	while page <= int(num_pages):
		page += 1
		
		driver.get('https://www.amazon.es/s?k=' + str(url) + '&page=' + str(page))
		if page == 1:
			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'sp-cc-accept')))
				cookies_btn = driver.find_element_by_id('sp-cc-accept').click()
			except:
				return

		for x in range(60):
			try:
				WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
					'//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[' + str(x) + ']/div/span/div/div/div[2]/div[1]/h2/a')))
				article = driver.find_element_by_xpath(
					'//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[' + str(x) + ']/div/span/div/div/div[2]/div[1]/h2/a')
				link = article.get_attribute('href')
				links.append(link)
				article.click()
			except:
				continue
			try:
				WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'productTitle')))
				title = driver.find_element_by_id('productTitle')
				titles.append(title.text)
			except:
				continue
			try:
				WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'priceblock_ourprice')))
				price = driver.find_element_by_id('priceblock_ourprice')
				prices.append(price.text)
			except:
				try:
					WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'priceblock_saleprice')))
					price = driver.find_element_by_id('priceblock_saleprice')
					prices.append(price.text)
				except:
					try:
						WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'priceblock_dealprice')))
						price = driver.find_element_by_id('priceblock_dealprice')
						prices.append(price.text)
					except:
						print('Price not avaible')
						if len(titles) > 1:
							del titles[-1]
							del links[-1]
							del ratings[-1]
			try:
				WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reviewsMedley"]/div/div[1]/div[2]/div[1]/div/div[2]/div/span/span')))
				rating = driver.find_element_by_xpath('//*[@id="reviewsMedley"]/div/div[1]/div[2]/div[1]/div/div[2]/div/span/span').text
			except:
				rating = 'Not avaible'
			finally:
				ratings.append(rating)
			
			driver.back()


	print(len(titles), len(prices), len(ratings))

	return titles, prices, links, ratings