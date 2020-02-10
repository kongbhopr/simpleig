import time
import urllib.request
from PIL import Image

def recent_10_posts(username):
    url = "https://www.instagram.com/" + username + "/"
    browser = webdriver.Chrome('chromedriver',options=options)
    browser.get(url)
    post = 'https://www.instagram.com/p/'
    post_links = []
    while len(post_links) < 10:
        links = [a.get_attribute('href') for a in browser.find_elements_by_tag_name('a')]
        for link in links:
            if post in link and link not in post_links:
                post_links.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(scroll_down)
        time.sleep(10)
    else:
        return post_links[:10]


# ```
# get_recent_image_from_id(<instragram_id>)
# ```
# return list 10 ภาพล่าสุดบน instragram_id นั้น
# ```
def get_recent_image_from_id(instragram_id):
  url = "https://www.instagram.com/" + instragram_id + "/"
  browser = webdriver.Chrome('chromedriver',options=options)
  browser.get(url)
  post = 'https://www.instagram.com/p/'
  post_links = []
  while len(post_links) < 10:
    links = [a.get_attribute('href') for a in browser.find_elements_by_tag_name('a')]
    for link in links:
      if post in link and link not in post_links:
        post_links.append(link)

    scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
    browser.execute_script(scroll_down)
    time.sleep(5)
    
  topic_list = list()
  for each_link in  post_links:
    browser.get(each_link)
    #video
    xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/div[1]/img'
    try:
      preview_image = browser.find_element_by_xpath(xpath_preview_image)
    except:  
      xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/img'
      try: 
        preview_image = browser.find_element_by_xpath(xpath_preview_image)
      except:
        xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/div/div/img'
        try: 
          preview_image = browser.find_element_by_xpath(xpath_preview_image)
        except:
          try:
            xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/img'
            preview_image = browser.find_element_by_xpath(xpath_preview_image)
          except:
            preview_image = "-1"
    
    if preview_image != "-1":
      preview_image = preview_image.get_attribute("src")

    topic_list.append(preview_image)
    time.sleep(5)
    
  return topic_list[:10]


# ```
# get_recent_topic_from_id(<instragram_id>)
# ```
# return list ข้อความของ 10 โพสล่าสุด instragram_id นั้น
def get_recent_topic_from_id(instragram_id):
  url = "https://www.instagram.com/" + instragram_id + "/"
  browser = webdriver.Chrome('chromedriver',options=options)
  browser.get(url)
  post = 'https://www.instagram.com/p/'
  post_links = []
  while len(post_links) < 10:
    links = [a.get_attribute('href') for a in browser.find_elements_by_tag_name('a')]
    for link in links:
      if post in link and link not in post_links:
        post_links.append(link)
      
    scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
    browser.execute_script(scroll_down)
    time.sleep(5)
    
  topic_list = list()
  for each_link in  post_links:
    browser.get(each_link)
    xpath_comment = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/h1'
    try:
      comment = browser.find_element_by_xpath(xpath_comment).text
    except:  
      xpath_comment = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span'
      try:
        comment = browser.find_element_by_xpath(xpath_comment).text
      except:  
        comment = "cannot get this topic"
    
    topic_list.append(comment)
    time.sleep(5)
    
  return topic_list[:10]


# ```
# get_recent_post_from_id(<instragram_id>)
# ```
# return list ข้อมูล 10 post ล่าสุด ของ instragram_id นั้น
def get_recent_post_from_id(instragram_id):
  url = "https://www.instagram.com/" + instragram_id + "/"
  browser = webdriver.Chrome('chromedriver',options=options)
  browser.get(url)
  post = 'https://www.instagram.com/p/'
  post_links = []
  while len(post_links) < 10:
    links = [a.get_attribute('href') for a in browser.find_elements_by_tag_name('a')]
    for link in links:
      if post in link and link not in post_links:
        post_links.append(link)
      
    scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
    browser.execute_script(scroll_down)
    time.sleep(5)

  detail_list = list()
  for each_link in  post_links:
    browser.get(each_link)
    
    # like
    likes = 0
    try:
        xpath_likes = '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button/span'
        likes = browser.find_element_by_xpath(xpath_likes).text    
    except:
        xpath_likes = '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/span/span'
        likes = browser.find_element_by_xpath(xpath_likes).text

    # comment
    xpath_comment = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/h1'
    try:
      comment = browser.find_element_by_xpath(xpath_comment).text
    except:  
      xpath_comment = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span'
      try:
        comment = browser.find_element_by_xpath(xpath_comment).text
      except:  
        comment = "cannot get this topic"
    
    # date / age
    age = browser.find_element_by_css_selector('a time').text

    # image
    xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/div[1]/img'
    try:
      preview_image = browser.find_element_by_xpath(xpath_preview_image)
    except:  
      xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/img'
      try: 
        preview_image = browser.find_element_by_xpath(xpath_preview_image)
      except:
        xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/div/div/img'
        try: 
          preview_image = browser.find_element_by_xpath(xpath_preview_image)
        except:
          try:
            xpath_preview_image = '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/img'
            preview_image = browser.find_element_by_xpath(xpath_preview_image)
          except:
            preview_image = "-1"
    
    if preview_image != "-1":
      preview_image = preview_image.get_attribute("src")
    
    detail_list.append({
        "likes": likes,
        "comment": comment,
        "date": age,
        "preview_image": preview_image
    })

    time.sleep(5)
    
  return detail_list

    
# ```
# show_image_from_link(<link>)
# ```
def show_image_from_link(link):
  try: 
    image = Image.open(urllib.request.urlopen(link))
    display(image)
    
    return True
  except:
    return False
