from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import re

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# url = "https://www.amazon.in/Voltas-Inverter-Copper-Adjustable-Anti-dust/dp/B0CWVDXYX1"
url = "https://www.amazon.in/Samsung-Adaptive-Real-Time-Interpreter-Battery/dp/B0D7M4G3NP"
# print(url)

driver.get(url)
time.sleep(5)

product = {}

name = driver.find_element(By.ID, "productTitle").text
product["name"] = name.split(",")[0].strip()
product["brand"] = driver.find_element(By.ID, "bylineInfo").text
product["price"] = driver.find_element(By.CSS_SELECTOR, "span.a-price-whole").text

ratingAndReviews = driver.find_element(By.ID, "averageCustomerReviews_feature_div").text
product["rating"] = ratingAndReviews.split('\n')[0]
product["rating_count"] = ratingAndReviews.split('\n')[1]

product["image_url"] = driver.find_element(By.ID, "landingImage").get_attribute("src")

# features = driver.find_elements(By.CSS_SELECTOR, "#feature-bullets ul li")
# product["description"] = " | ".join([f.text for f in features])

driver.quit()

print(json.dumps(product, indent=4, ensure_ascii=False))


