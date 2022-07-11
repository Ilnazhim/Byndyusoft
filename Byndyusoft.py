from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.google.ru/"
browser = webdriver.Chrome()
browser.get(link)

try: 

    browser.find_element(By.CSS_SELECTOR, ".gLFyf.gsfi").send_keys("Byndyusoft\n")
    browser.find_element(By.XPATH, "//h3[normalize-space()='Byndyusoft']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    browser.find_element(By.CSS_SELECTOR, ".know-more .btn").click()
    assert browser.find_element(By.CSS_SELECTOR, ".popup-callback__footer-contacts a:nth-child(1)").text \
           == "8 800 775-15-21", "Phone is not found"
    assert browser.find_element(By.CSS_SELECTOR, ".popup-callback__footer-contacts a:nth-child(3)").text \
           == "sales@byndyusoft.com", "Email is not found"

finally:

    time.sleep(1)
    browser.quit()
