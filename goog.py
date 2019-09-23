import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
driver = webdriver.Remote

# Google Steps
@when('visit url "{url}"')
def step(context, url):
    context.browser.get(url)
    

@when('I click on the button "{selector}"')
def step(context, selector,):
    context.browser.find_element_by_id(selector).click()
    time.sleep(10)
     

@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_id(selector)
    elem.send_keys(value)

    
@when('field with pw "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_id(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(10)
@when('I press "{selector}"')
def step(context, selector):
    context.browser.send_keys(selector)

@when('I search google "{value}"')
def step(context, value):
    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.send_keys(value)
    actions.send_keys(Keys.RETURN)
    #actions.click()
    actions.perform()
    time.sleep(5)

    #actions = webdriver.common.action_chains.ActionChains(driver)
    #actions.move_to_element_with_offset(200, reso, 258, 32).click()
    #time.sleep(10)

@when('I click browser "{selector}"')
def step(context, selector):
    context.browser.find_element_by_xpath(selector).click()
    time.sleep(20)    

@when('I click to search "{selector}"')
def step(context, selector):
    elem = context.browser.find_element_by_id(selector)
    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.move_to_element_with_offset(elem, 258, 32)
    actions.click()
    actions.perform()
    time.sleep(10)

@then('title becomes "{title}"')
def step(context, title):
    assert context.browser.title == title