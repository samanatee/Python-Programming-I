''' Created on May 20, 2018

@author: Samantha Hangsan

- Write a program that constructs a http request with search keywords that the
user provides and send a search query to the Google search engine.

- Parse the result of the search query and extract all the links in the
response which uses http

'''

import re
import urllib.request

class MyHTMLParser():

	def __init__ (self, url):
		self.url = url

	def link_collector(self, html):

		urls = re.findall('(?<=url\?q\=)http.+?(?=&amp;)', html)
		urls = list(set(urls))

		return urls


def search_on_google():

	# request object
	user_agent = 'Mozilla/5.0'
	headers = {'User-Agent': user_agent}

	search_query = input('Search Google by entering a keyword(s): ')
	value = {'q': search_query}

	url = 'http://www.google.com/search'
	data = urllib.parse.urlencode(value)

	url = url + '?' + data
	req = urllib.request.Request(url, None, headers)
	response = urllib.request.urlopen(req)
	html = response.read().decode()

	return url, html


def parse(url, query):

	http_links = MyHTMLParser(url)
	result = http_links.link_collector(query)

	return result


def print_urls(results):

	for url in results:

		print(url + '\n')


def main():

	url, query = search_on_google()
	results = parse(url, query)
	print_urls(results)


if __name__ == '__main__':
	main()
