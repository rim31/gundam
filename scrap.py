import requests
import time
import os
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import webbrowser

SITE_URL = 'https://www.topachat.com'
# URL = 'https://www.topachat.com'
# URL = f'{SITE_URL}/pages/produits_cat_est_micro_puis_rubrique_est_wgfx_pcie_puis_ordre_est_P_puis_sens_est_ASC_puis_f_est_58-7624.html'
URL = f'{SITE_URL}/pages/produits_cat_est_micro_puis_rubrique_est_wgfx_pcie_puis_ordre_est_P_puis_sens_est_ASC_puis_f_est_58-11447,11445.html'


def openLink(link):
	webbrowser.open_new_tab(link)


toaster = ToastNotifier()

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

while True:
	job_elems = soup.find_all('section', class_='en-stock')
	for job_elem in job_elems:
		name_elem = job_elem.find('h3')
		price_elem = job_elem.find('div', class_='prod_px_euro v16')
		link_elem = job_elem.find('a')['href']
		if None in (name_elem, price_elem, link_elem):
			continue

		real_link = f"{SITE_URL}{link_elem}"
		print(name_elem.text.strip())
		print(real_link)
		print(price_elem.text.strip())
		print()

		toaster.show_toast(name_elem.text.strip(),
						price_elem.text.strip(), callback_on_click=lambda: openLink(real_link), threaded=True)
	time.sleep(10)
