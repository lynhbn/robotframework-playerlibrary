import re

def extract_keywords(file_path):
    keyword_pattern = re.compile(r'@keyword\("([^"]+)"\)')
    keyword_pattern_2 = re.compile(r'@keyword\(\'([^"]+)\'\)')
    keywords = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = keyword_pattern_2.findall(line)
            if matches:
                keywords.extend(matches)

    return keywords

files = ["./api_handler.py",
"./base_context.py",
"./browser_handler.py",
"./button_handler.py",
"./checkbox_handler.py",
"./config.py",
"./custom_locator.py",
"./datepicker_handler.py",
"./dropdown_handler.py",
"./element_handler.py",
"./iframe_handler.py",
"./method_extractor.py",
"./page_handler.py",
"./table_handler.py",
"./textbox_handler.py"]

kws = []

if __name__ == "__main__":
    for file in files:
        kws += extract_keywords(file)
    for kw in kws:
        print(kw)