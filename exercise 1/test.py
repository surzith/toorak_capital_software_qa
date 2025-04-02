from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(3)

# Extract product name and price
product_name = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]").text
product_price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]").text

with open("product_details.txt", "w") as file:
    file.write(f"Product Name: {product_name}\n")
    file.write(f"Product Price: {product_price}\n")

driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
time.sleep(2)

cart_product_name = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text
cart_product_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']").text

with open("product_details.txt", "r") as file:
    saved_data = file.readlines()
    saved_name = saved_data[0].strip().split(": ")[1]
    saved_price = saved_data[1].strip().split(": ")[1]

if saved_name == cart_product_name and saved_price == cart_product_price:
    print("Product details match successfully!")
else:
    print("Product details do NOT match!")

driver.quit()