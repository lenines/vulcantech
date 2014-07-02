from bs4 import BeautifulSoup
import urllib

def get_soup(url):
	page=urllib.urlopen(url).read()
	soup=BeautifulSoup(page)
	return soup

def get_li(soup):
	categoryLink=soup.findAll('li',{'class':'catlink'})
	return categoryLink

def get_h1(soup):
	title=soup.find('h1').next_element
	return categoryLink

def get_details(soup):
	details=soup.findAll('div',{'class':'content'})
	return ' '.join(str(e) for e in details[0])
def get_categories_names(categories):
    cat={}
    for category in categories:
    	cat[category.find('a').get('href')]=category.find('a').next_element
    return cat

