from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from requests import get
from bs4 import BeautifulSoup



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Define the URL
url = "https://www.youtube.com/@programmingwithmosh/videos"

# load the web page
driver.get(url)

# set maximum time to load the web page in seconds
driver.implicitly_wait(10)


response = get('https://www.youtube.com/@programmingwithmosh/videos')
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.title.string
print(title)

driver.get(url)
driver.implicitly_wait(10)

#Для веб-скрапинга данных можно использовать либо id (post-title), либо теги
# (h1 и p):


contents = driver.find_element(By.ID, "contents")

#Чтобы собрать для каждого ролика его заголовок и ссылку на видео, необходимо
# использовать id-атрибут video-title-link.
video_elements = contents.find_elements(By.ID, "video-title-link")


df = pd.DataFrame(video_elements)
df.to_csv('output.csv', index=False)