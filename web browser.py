import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to  chromedriver
chrome_driver_path = r"C:\Users\dell\Desktop\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"

# service object for ChromeDriver
service_1 = Service(executable_path=chrome_driver_path)

# Initialize the Chrome driver using the service
driver = webdriver.Chrome(service=service_1)

# Navigate to Google
driver.get("https://www.google.com")
try:
    while True:
        pass
except KeyboardInterrupt:
    driver.quit()
#time.sleep(2*7200)
'''driver.quit '''   


    











