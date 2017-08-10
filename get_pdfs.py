from bs4 import BeautifulSoup
import urllib
import re
import os

def download_file(download_url):
    response = urllib.request.urlopen(download_url)
    file = open("download/" + download_url.split("/")[-1], 'wb')
    file.write(response.read())
    file.close()
    print("Completed downloading " + download_url.split("/")[-1])


if __name__ == "__main__":
	if not os.path.exists("download"):
		os.makedirs("download")

	base = "http://www.idot.illinois.gov/doing-business/procurements/engineering-architectural-professional-services/Consultants-Resources/type-size-and-location-drawings"
	
	html_page = urllib.request.urlopen(base)
	soup = BeautifulSoup(html_page)
	for link in soup.findAll('a'):
		if link.get('href') is not None:
			if link.get('href').endswith(".pdf"):
				url = link.get('href')
				url = urllib.parse.urljoin(base, url)
				print(url)
				download_file(url)

