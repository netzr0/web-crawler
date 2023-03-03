import os

import requests

from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def crawl (url):

	reqs = requests.get(url, headers=headers)	soup = bs(reqs.text, 'html.parser')

	

	data=soup.find_all("title")

	print("Title of page:")

	print(20*"=")

	for title in data:

		print(title.string,"\n")

		

	data=soup.find_all("a", href=True)

	print ("Links found:")

	print(20*"=")

	for link in data:

		if "https" in link.get(("href")):

			print(link.get_text("href"))

			print(link.get('href'))

			print('---')

crawl(input("Please enter URL;"))
