from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome('./chromedriver_linux',chrome_options=options)
driver.get('https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%EB%A7%9B%EC%A7%91')
driver.implicitly_wait(3)

url_list = []
urls = driver.find_elements_by_css_selector('.info_post > a')

for url in urls:
    url_list.append(url.get_attribute('href'))

url_list = list(set(url_list))
print(url_list)
print(len(url_list))
