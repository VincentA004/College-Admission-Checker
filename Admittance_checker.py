import datetime as dt
import time
import pyautogui as py
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main():
    Austin()
    
    
def Austin():
    url = "https://utdirect.utexas.edu/apps/adm/mystatus/statuscheck/admission/00/"
    if __name__ == "__main__":
        username = input("enter username: ")
        password = input('enter password: ')
        options = webdriver.ChromeOptions()
        driver = uc.Chrome(version_main = 103 ,options = options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(1)
        u = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="username"]')))
        u.send_keys(username)
        
        p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
        p.send_keys(password)
        
        xpath = '//*[@id="login-button"]/input'
        a = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,xpath)))
        a.click()
        time.sleep(10)
        
    
    
    
    
        
main()
