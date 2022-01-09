import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://test-for-coronavirus.service.gov.uk/order-lateral-flow-kits'

driver.get(url)
time.sleep(5)

print("Sorry" in driver.page_source)

driver.close()