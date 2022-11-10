from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.wikipedia.org")
assert 'Wikipedia' in driver.title
element = driver.find_element(By.ID, 'www-wikipedia-org')
assert element.tag_name == 'body'
english_link = driver.find_element(By.ID, 'js-link-box-en')
english_link.click()
assert driver.current_url == 'https://en.wikipedia.org/wiki/Main_Page'
assert driver.title == 'Wikipedia, the free encyclopedia'
search_box = driver.find_element(By.CSS_SELECTOR, 'input[type=search]')
search_box.click()
search_box.send_keys('Dog')
search_box.send_keys(Keys.ENTER)
# print(driver.title)
assert 'Dog - Search results - Wikipedia' in driver.title

