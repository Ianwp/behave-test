# Google Feature
Feature: Google Search Functionality
    Scenario: can find search results in Live
        When visit url "https://live.browserstack.com"
        When I click on the button "accept-cookie-notification"
        When field with name "user_email_login" is given "juma2343@gmail.com"
        When field with pw "user_password" is given "southpar1"
        When I click on the button "user_submit"
        When I click on the button "skip-local-installation"
        When I click browser "//*[@id='rf-browsers']/div/div[2]/div[4]/ul/li[4]/a"
        #When I press "Keys.RETURN"
        When I click to search "dockLocation"
        When I search google "browserstack"
        Then title becomes "Dashboard"

    

    
