*** Settings ***
Test Timeout       300
Resource        ./sample.resource

Suite Teardown       Quit all browsers

*** Test Cases ***
TC_1_1X - Check correctness of screen first loading
    [Tags]     ui    automated
    Start Browser with url    http://localhost:8080/     headless=False
    Page Should Have    Welcome to Eureka Navigator
    click    link:Settings
    page should have    Set the date and time manually
    Button Should Be Enabled   id:submitBtn

