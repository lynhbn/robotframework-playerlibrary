*** Settings ***
Test Timeout       300
Resource        ./sample.resource

Suite Setup    Setup custom locator and timeout
Test Teardown    Start new browser session
Suite Teardown       Quit all browsers

*** Test Cases ***
TC_1_1 - Check correctness of screen first loading
    [Tags]     ui    automated
    Start Browser with url    https://dev.to/playwright     headless=False
    Button Should Be Enabled   id:user-follow-butt
    ${c}    get element     text:Follow
    number of element should be     text:Follow      1
    font size should be     //h1      30px
    get css property value    //h1    margin
    element should have     //div[@class="profile-header__details"]
    ...      Playwright supports all modern rendering engines including Chromium
    element should have these texts      //div[@class="profile-header__details"]
    ...      WebKit, and Firefox. Test on Windows, Linux, and macOS, locally or on CI,
    ...      headless or headed with native mobile emulation.
    element should not have      //div[@class="profile-header__details"]
    ...      Waterfox
    ${p}        get inner element    //div[@class="profile-header__details"]      //p
    element color should be    //h1     \#090909
    ${color}        get element color    //h1

TC_1_2 - Check correctness of screen first loading
    [Tags]     ui    automated
    Start Browser with url    https://dev.to/playwright     headless=False
    element should be shown    link:Create account
    element should not be shown   link:ABC
    element attribute should be        id:user-follow-butt   id      user-follow-butt
    element attribute should not be    id:user-follow-butt    id     user-follow-butt-wrong
    element attribute should not be    id:user-follow-butt    xd     user-follow-butt-wrong
    click button    class:site-logo__img
    page should have   Playwright supports all modern rendering engines including Chromium

TC_1_3 - Check correctness of screen first loading
    [Tags]     ui    automated
    start blank browser    browser=firefox     headless=False
    page should be blank
    go to url    https://dev.to/playwright
    ${url}    get current url
    go to url   https://app.your.rentals/sign-up/email
    textbox should be empty     //input[@data-test-id="inputEmail"]
    input into    //input[@data-test-id="inputEmail"]    sample@sample.com
    clear text     //input[@data-test-id="inputEmail"]
    textbox should be empty     //input[@data-test-id="inputEmail"]
    input into     //input[@data-test-id="inputEmail"]    sample_123@sample.com
    Clear Text Using Backspace     //input[@data-test-id="inputEmail"]
    textbox should be empty     //input[@data-test-id="inputEmail"]
    go to url   https://ultimateqa.com/complicated-page
    Placeholder should be     //input[@id="et_pb_contact_name_0"]    Name
    textbox should be correct    //input[@id="et_pb_contact_name_0"]    state=enabled   default=${EMPTY}
    reload whole page
    ${a}    get page source
    capture screenshot
    html title should be    Complicated Page - Ultimate QA
    page should have  How to deal with a large page that has many elements and divisions?
    page should not have   papapapap
    page should have element    //input[@id="et_pb_contact_name_0"]
    page should not have element     //input[@id="et_dddpb_contact_name_0"]
    page should be redirected to     https://ultimateqa.com/complicated-page
    scroll right
    scroll down
    scroll to element with additional alignment    //button[@name="et_builder_submit_button"]
    text should be visible      Section of Random Stuff
    text should not be visible   Section of Random Stuffsss
    texts should be visible   ${{ ["Section of Random Stuff","0 Comments"] }}

TC_1_4 - Check correctness of screen first loading
    [Tags]     ui    automated
    start blank browser     headless=False
    go to url   https://ultimateqa.com/complicated-page
    click      //button[@name="et_builder_submit_button"]
    double click     //button[@name="et_builder_submit_button"]
    open new window
    go to url   https://playwright.dev/python/community/welcome
    switch to previous page
    page should have      Please, fill in the following fields:
    sleep    1
    switch to latest page
    close current page
    sleep    1

TC_1_5 - Check correctness of screen first loading
    [Tags]     ui    automated
    start blank browser     headless=False
    go to url   https://ultimateqa.com/simple-html-elements-for-automation/
    select a radio option    //input[@name="gender"][@value="male"]
    radio button should be enabled    //input[@name="gender"][@value="male"]
    radio button should be checked     //input[@name="gender"][@value="male"]
    radio button should not be checked    //input[@name="gender"][@value="female"]
    get current radio button checking status    //input[@name="gender"][@value="male"]
    radio should be correct   //input[@name="gender"][@value="male"]    state=enabled   status=checked
    checkbox should be enabled    //input[@name="vehicle"][@value="Bike"]
    tick checkbox      //input[@name="vehicle"][@value="Bike"]
    untick checkbox    //input[@name="vehicle"][@value="Car"]
    checkbox should be checked       //input[@name="vehicle"][@value="Bike"]
    checkbox should not be checked    //input[@name="vehicle"][@value="Car"]
    get current checkbox checking status   //input[@name="vehicle"][@value="Bike"]
    checkbox should be correct   //input[@name="vehicle"][@value="Bike"]   state=enabled  status=checked
    dropdown should be enabled      //select
    select value   //select     Saab
    dropdown itemlist should be     //select    Volvo;Saab;Opel;Audi
    list item should be     //select    Volvo   Saab   Opel   Audi
    dropdown itemlist should contain     //select    Volvo
    dropdown itemlist should not contain     //select    Volvox
    dropdown current value should be      //select    Saab
    dropdown current value should not be    //select    Opel
    dropdown current value should contain    //select    Sa
    dropdown current value should not contain     //select    Vol
    ${x}    get current selected value   //select
    ${y}    get list values      //select
    get item list length   //select
    dropdown should be correct    //select    state=enabled  default=Saab   item_list=Volvo;Saab;Opel;Audi

TC_1_6 - Check correctness of screen first loading
    [Tags]     ui    automated
    start blank browser     headless=False
    go to url   https://ultimateqa.com/simple-html-elements-for-automation/
    element attribute should contain    //button[@id="button1"]    type    submit
    element attribute should not contain    //button[@id="button1"]    xxx    submit
    input into     //input[@id="et_pb_contact_name_0"]       dfgfghfg23534hgfhf
    get actual text       //input[@id="et_pb_contact_name_0"]
    get actual number     //input[@id="et_pb_contact_name_0"]
    get inner text       //h4/span
    element value should not be empty   //input[@id="et_pb_contact_name_0"]
    append text     //input[@id="et_pb_contact_name_0"]    5666666
    get element tag    //input[@id="et_pb_contact_name_0"]
    actual text should be    //input[@id="et_pb_contact_email_0"]    ${EMPTY}
    actual text should not be    //input[@id="et_pb_contact_email_0"]    CCC
    actual text should contain    //input[@id="et_pb_contact_name_0"]    5666666
    actual text should not contain    //input[@id="et_pb_contact_name_0"]   @@@
    Table column should have    //table[@id="htmlTableId"]    Title    Work    Salary
    Table row should have    //table[@id="htmlTableId"]    2
    ...      Software Development Engineer in Test	  Automation	 $150,000+
    Table cell value should be     //table[@id="htmlTableId"]
    ...    Automation Testing Architect	  Work    Automation

TC_1_7 - Check correctness of screen first loading
    [Tags]     ui    automated
    start blank browser     headless=False
    go to url   https://ultimateqa.com/simple-html-elements-for-automation/
    click and wait      //button[@id="button1"]     expected_item=//h1[text()="Push Higher Quality Software To Market Faster"]
    ...    expected_text=UltimateQA’s customized, efficient QA test
    ${f}    get all data of similar html elements    //h2
    start new browser session
    go to url    https://playwright.dev/python/docs/api/class-page#page-frame-locator

TC_1_8 - Check correctness of screen first loading
    [Tags]     ui    automated
    start blank browser   browser=firefox    headless=False
    go to url    https://www.w3schools.com/html/html_iframe.asp
    select iframe    //iframe[@title="W3Schools HTML Tutorial"]
    iframe should contain     HTML is the standard markup language
    iframe should not contain   HTML TutorialXX
    Click On Iframe     id:tnb-google-search-mobile-show
    input on iframe      //input[@id="tnb-google-search-input"]    abcdef
    unselect iframe
    page should have      An HTML iframe is used to display a web page within a web page.




