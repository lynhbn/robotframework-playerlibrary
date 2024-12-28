*** Settings ***
Test Timeout       300
Resource        ./sample.resource


*** Variables ***
${post_body}      {
...               "name": "Apple MacBook Pro 16",
...               "data": {
...                  "year": 2019,
...                  "price": 1849.99,
...                  "CPU model": "Intel Core i9",
...                  "Hard disk size": "1 TB"
...               }
...            }

${patch_body}
...    {
...       "name": "Apple MacBook Pro 16 (Updated Name)"
...    }

${put_body}
...    {
...       "name": "Apple MacBook Pro 16",
...       "data": {
...          "year": 2019,
...          "price": 2049.99,
...          "CPU model": "Intel Core i9",
...          "Hard disk size": "1 TB",
...          "color": "silver"
...       }
...    }

${URL}     https://api.restful-api.dev/objects

*** Test Cases ***
TC_1_2 - Sample Rest API test case
    [Tags]     api    automated
    ${sample_header}    Create Header
    start api session
    ${resp}     rest post    ${URL}     ${sample_header}     ${post_body}
    rest patch    https://api.restful-api.dev/objects/${resp}[id]     ${sample_header}    ${patch_body}
    rest put      https://api.restful-api.dev/objects/${resp}[id]     ${sample_header}    ${put_body}
    rest delete   https://api.restful-api.dev/objects/${resp}[id]     ${sample_header}
    rest get      https://api.restful-api.dev/objects                 ${sample_header}
    Rest Dispose