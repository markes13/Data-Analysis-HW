
# encoding: utf-8

# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import lxml
import requests
import pymongo

def scrape():

    mars_data = {}

    # # Step 1 - Scraping

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define database and collection
    db = client.mars_db
    collection = db.articles

    # # 1.a. NASA Mars News

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')

    # Retrieve the parent divs for all articles
    results = soup.find_all('div', class_='slide')

    for result in results:
        news_title = result.find('div', class_='content_title').a.text
        news_p = result.find('div', class_='rollover_description_inner').text

    mars_data['latest_news_title'] = news_title
    mars_data['latest_news_article_p'] = news_p

    # # 1.b. JPL Mars Space Images - Featured Image

    executable_path = {'executable_path': '/usr/local/Cellar/chromedriver/2.37/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # use bs to get featured image URL
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_url = soup.find('img', class_='thumb')
    featured_url = 'https://www.jpl.nasa.gov' + image_url['src']
    
    mars_data['featured_img'] = featured_url

    # # 1.c. Mars Weather

    # reset url variable to Mars report twitter account
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    # use bs to get most recent Mars weather tweet
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # assign most recent tweet to mars_weather variable
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    mars_data["weather_tweet"] = mars_weather

    # # 1.d. Mars Facts

    # import pandas to scrape table from next url
    import pandas as pd

    # reset url variable to Mars facts webpage
    url = 'https://space-facts.com/mars/'

    # set table variable to html table element
    tables = pd.read_html(url)

    # pull tables[0] and assign to df variable
    df = tables[0]
    df = df.rename(columns={'0': 'Description', '1': 'Value'})

    # pd.to_html on df variable
    html_table = df.to_html(header=None, index=False)

    mars_data["html_table"] = html_table

    # # 1.e. Mars Hemispheres

    # reset url variable to Mars report twitter account
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # use bs to get full resolution images of Mars's hemisphere
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # create empty dict to store title and url string
    hemisphere_image_urls = []

    results = soup.find_all('div', class_='item')

    # tell browser to cycle through results and click links 
    # to get enhanced image url, append title and url to dict in list
    for result in results:
        link = result.find('h3').text
        title = link.replace(' Enhanced', '')
        browser.click_link_by_partial_text(link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        result2 = soup.find('img', class_='wide-image')
        url = 'https://astrogeology.usgs.gov/' + result2["src"]
        hemisphere_image_urls.append({"title":title, "img_url":url})
        browser.back()

    mars_data['hemisphere_imgs'] = hemisphere_image_urls

    return mars_data
