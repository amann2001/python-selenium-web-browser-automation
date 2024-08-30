import os
import zipfile
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    # Open Flipkart
driver.get("https://www.flipkart.com")

    # Close the login popup if it appears
WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    ).click()

    # Navigate to the search bar and type 'mobile'
search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("mobile")
search_box.send_keys(Keys.RETURN)

    # Scrape mobile data
mobiles = []
while True:  # Loop to scrape multiple pages
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_4rR01T']")))

        items = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
        prices = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")
        brands = driver.find_elements(By.XPATH, "//div[@class='_3KcT7X']")  # Adjust the XPath if needed

        for item, price, brand in zip(items, prices, brands):
            mobiles.append({
                "Model": item.text,
                "Price": price.text,
                "Brand": brand.text
            })
        # Go to the next page
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'_1LKTO3')]"))
            )
            next_button.click()
        except Exception as e:
            print(f"Next button not found or could not be clicked: {e}")
            break

try:
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()  # Clear any pre-filled text
        search_box.send_keys("mobile")
        search_box.send_keys(Keys.RETURN)
        print("Search for 'mobile' executed successfully")
except Exception as e:
        print(f"Failed to locate or interact with the search bar: {e}")
        driver.quit()
        exit()
    





    











