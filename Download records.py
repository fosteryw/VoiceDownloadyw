import time
from selenium import webdriver

try:
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"

    browser = webdriver.Chrome(desired_capabilities=caps)

    browser.get('https://cloudpbx.rt.ru/domain/dashboard/')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="username"]').send_keys('***')
    browser.find_element_by_xpath('//*[@id="password"]').send_keys('***')
    browser.find_element_by_xpath('//*[@id="domain"]').send_keys('***')
    browser.find_element_by_xpath('//*[@id="login"]/button').click()
    time.sleep(6)

    with open('asswecan.txt') as file:
            list_urls = list(file)

    for url in list_urls:
            browser.get(url.replace('\n', ''))
            time.sleep(1)

except:
    import traceback
    print(traceback.format_exc())
finally:
    browser.close