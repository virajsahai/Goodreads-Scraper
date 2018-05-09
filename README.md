# Goodreads-Scraper
This python script scrapes Goodreads for a variety of information. I don't claim ownership of any of the data at Goodreads and don't endorse the use of this program for commercial purposes. Please check with Goodreads regarding these concerns.

## Instructions for use-

### 1. Get dependencies
	- The scraper uses BeautifulSoup.Use 'pip install beautifulsoup4' to get it.

### 2. How it works-
	- Put list of ISBNs in 'isbn.txt'. Make sure each ISBN starts on a new line.
	- Run scraperv3.py.
	- Results will be placed in a .csv file called 'scraped_csv.csv'
	NOTE: Currently, the csv file is always over-written and not appended. Make sure to save previous data.

