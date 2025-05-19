# robotframework-playerlibrary
Light-weight GUI/API automation testing library written in Python only using Playwright. No need to install any NodeJS stuff.

**Installation:**
```
pip install robotframework-playerlibrary
```

**Import the library:**
```
*** Settings ***
Library           PlayerLibrary    assertion_timeout=10000    
```
_assertion_timeout_: Customize the timeout for each assertion in milliseconds

**Example keyword:**
```
*** Keywords ***
Login into the system using provided account
    Input Into    id:login-email       sample-test@abc.com
    Input Into    id:login-password    yourpassword
    Click    //button[contains(.,"Sign In")]
    Page Should Have    Welcome Back!

```

**Example locators:**

Locators can be a xpath: `//button[@id="login""]`

Can be a prefix: `id:login` `class:yellow` `text:Log in`

Full list of supported prefixes:
- _BUILT_IN_: `id`, `text`, `data-test-id`, `data-testid`, `data-test`
- _ATTRIBUTE_: `placeholder`, `name`, `class`, `value`, `title`
- _HYPERLINK_: `link`
- _XPATH_: `xpath://`, `//`

**Example UI scenario:**
```
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
```
**Example API scenario:**
```
TC_001 - Sample Rest API test case
    [Tags]     api    
    ${sample_header}    Create Header
    start api session
    ${resp}     rest post    ${URL}     ${sample_header}     ${post_body}
    rest patch    https://api.restful-api.dev/objects/${resp}[id]     ${sample_header}    ${patch_body}
    rest put      https://api.restful-api.dev/objects/${resp}[id]     ${sample_header}    ${put_body}
    rest delete   https://api.restful-api.dev/objects/${resp}[id]     ${sample_header}
    rest get      https://api.restful-api.dev/objects                 ${sample_header}
    Rest Dispose
```

**Keyword documentation at** https://lynhbn.github.io/robotframework-playerlibrary/index.html


