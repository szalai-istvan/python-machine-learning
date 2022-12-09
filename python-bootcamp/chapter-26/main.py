from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chromeDriverPath = 'C:\\Users\\szala\\OneDrive\\Asztali gép\\Python\\python-machine-learning\\python-bootcamp\\chapter-26\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromeDriverPath)


driver.get('https://orteil.dashnet.org/cookieclicker/')
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'langSelect-EN')))

button = driver.find_element(By.ID, 'langSelect-EN')
button.click()

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'bigCookie')))
button = driver.find_element(By.ID, 'bigCookie')

for _ in range(100_000):
    button.click()

