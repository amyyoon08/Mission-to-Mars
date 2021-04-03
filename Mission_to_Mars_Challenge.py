#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[40]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[21]:


# Visit the mars nasa news site
url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[22]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[23]:


slide_elem.find('div', class_='content_title')


# In[24]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[25]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[26]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[27]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[28]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[32]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[39]:


df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.head()


# In[40]:


df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[41]:


df.to_html()


# In[18]:


browser.quit()


### D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

###  Hemispheres

# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
img_link = browser.find_by_css('a.product-item img')
                               
for i in range(len(img_link)):
    hemisphere = {}
    
    browser.find_by_css('a.product-item img')[i].click()
    
    img = browser.find_link_by_text('Sample').first
    
    hemisphere['img_url'] = img['href']


    hemisphere['title'] = browser.find_by_css('h2.title').text
  
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

