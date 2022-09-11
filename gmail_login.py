#!/usr/bin/env python3
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
username = "labuzogroup"
password = "dummy_password"

if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get('https://accounts.google.com/')
    sleep(1)
    print("#1 USING USERNAME")
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    sleep(3)
    print("#2 USING PASSWORD")
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    print("#3 EXPECTING 2FA APPROVAL (10secs)")
    sleep(10)
    print("#4 REDIR TO GMAIL")
    driver.get('https://gmail.com/')
    sleep(10)
    print("#5 CLOSING")
