import time
from selenium import webdriver

openChrome = webdriver.Chrome(
    executable_path="c:\Program Files (x86)\Google\Chrome\chromedriver.exe")

openChrome.maximize_window()

openChrome.get("https://discordapp.com/login")
time.sleep(3)

email = "Your email"
password = "Your password"

usernameField = openChrome.find_element_by_css_selector("[type=email]")
usernameField.send_keys(email)
time.sleep(1)
usernameField = openChrome.find_element_by_css_selector("[type=password]")
usernameField.send_keys(password)
time.sleep(1)

loginButoon = openChrome.find_element_by_css_selector("[type=submit]")
loginButoon.click()

print("Done!")
