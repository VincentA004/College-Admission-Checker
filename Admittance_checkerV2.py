import playwright
from playwright.sync_api import sync_playwright
import time


def main():
    Austin()
    
def Austin():
    url = 'https://utdirect.utexas.edu/apps/adm/mystatus/statuscheck/admission/00/'
    username = input("enter username: ")
    password = input('enter password: ')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.locator('//*[@id="username"]').fill(username)
        page.locator('//*[@id="password"]').fill(password)
        page.locator('//*[@id="login-button"]/input').click()
        time.sleep(10)
        
main()