from selenium import webdriver
from konlpy.tag import Mecab
from konlpy.utils import pprint

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome('./chromedriver_linux',chrome_options=options)
driver.get('https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%EB%A7%9B%EC%A7%91')
driver.implicitly_wait(3)

url_list = []
urls = driver.find_elements_by_xpath('//*[contains(@class,"desc_inner")]')

for url in urls:
    url_list.append(url.get_attribute('href'))

url_list = list(set(url_list))
#print(url_list)
#print(len(url_list))

driver.get(url_list[0])
driver.implicitly_wait(3)

real_url = driver.find_element_by_xpath('//frame').get_attribute('src')
#print(real_url)
driver.get(real_url)
driver.implicitly_wait(3)

text_list = []

texts = driver.find_elements_by_xpath('//*[contains(@class,"se_textarea")]')


if len(texts) < 1:
    print('why cannot select')

for text in texts:
    raw_text = text.text
    text_list.append(raw_text)

# print(text_list)

dom_string = ''.join(text_list)

mecab = Mecab()
pprint(mecab.pos(dom_string))