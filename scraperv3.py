###Written by Viraj Sahai (github.com/virajsahai).
###Available to use under the GNU PLv3 under the condition that these comments will not be removed.
###The author doesn't support any commercial use of this software.


import urllib2
from bs4 import BeautifulSoup
from multiprocessing import Pool
from time import sleep

isbn_list = open("isbn.txt","r").read().split('\n')

def get_data(url):

    ###variable to store data
    scraped_data = []
    
    ###get page
    page = urllib2.urlopen(url)
    sleep(0.25)
    
    ###parse
    soup = BeautifulSoup(page, 'html.parser')
    
    ###get data
    book_title = soup.find('h1', attrs={'class': 'bookTitle'}).text.strip()
    author = soup.find('span', attrs={'itemprop':'name'}).text.strip()
    language = soup.find('div', attrs={'itemprop':'inLanguage'}).text.strip()
    details = soup.find('div', attrs={'id':'details'}).text.split('\n')
    binding = details[1].split(',')[0].strip()
    num_pages = details[1].split(',')[1].strip()
    publisher = details[5].strip()[3:]
    genre = soup.find('a', attrs={'class':'actionLinkLite bookPageGenreLink'}).text.strip()
    goodreads_rating = soup.find('span', attrs={'class':'value rating'}).text.strip()
    description = soup.find('div', attrs={'id':'description'})
    description = description.text.split('</span>')[0].split('\n')
    if description[-2] == '...more':
        description = description[2]
    else:
        description = description[1]
    description = "".join(description.split(","))
    img_link = soup.find('meta', attrs={'name':'twitter:image'})['content']

    ###put data
    scraped_data.extend([book_title,author,language,binding,num_pages,publisher,genre,goodreads_rating,description,img_link])

    ###return scraped data
    return ','.join(scraped_data)


# Run following code when the program starts
if __name__ == '__main__':

    ###init url list
    url_list = []

    for i in isbn_list:
        url_list.append('https://www.goodreads.com/book/isbn/'+i)

    ###change pool number here for faster speed but it will put system resources under pressure.
    p = Pool(10)
    data = p.map(get_data, url_list)

    ###write to csv here  
    with open('scraped_csv.csv', 'wb') as f:
        f.write(("\n".join(data)).encode('ascii','ignore')) #??? UTF or ASCII ???# File is currently written as ASCII.
