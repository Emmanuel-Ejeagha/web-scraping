#!/usr/bin/env python3

from selenium import webdriver

def get_driver():
    # Set options to make browsing easier
    setup = webdriver.ChromeOptions()
    setup.add_argument("disable-infobars")
    setup.add_argument("start-maximized")
    setup.add_argument("disable-dev-shm-usage")
    setup.add_argument("no-sandbox")
    setup.add_experimental_option("excludeSwitches",
                                  ["enable-automation"])
    setup.add_argument("disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=setup)
    driver.get("https://www.myjobmag.com/")
    return driver

def main():
    driver = get_driver()
    data = driver.find_element("xpath", '//*[@id="jobs-sec"]/div/div[1]/ul/li[4]/ul/li[2]/ul/li[1]/h2/a')
    print(data.text)  # Add this to see the result

if __name__ == "__main__":
    main()
