*** Settings ***
Test Timeout       300
Resource        ./sample.resource

Suite Setup       Start Browser Then Open Url    https://www.w3schools.com/     headless=True
Test Setup        Page Should Have        Learn to Code
Suite Teardown      Quit all browsers

*** Test Cases ***
TC_1_1 - Check correctness of screen first loading
    [Tags]     ui    automated
    Page Should Have    With the world's largest web developer site.

TC_1_2 - Check correctness navigating to Login screen
    [Tags]     ui    automated
    click    id:w3loginbtn
    Page Should Have     //span[text()="Log in"]