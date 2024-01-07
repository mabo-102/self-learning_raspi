# Selenium

- [Selenium](https://www.selenium.dev/ja/)

## WebDriver
- [WebDriver - Google Chrome](https://chromedriver.chromium.org/downloads)
  - [Stable Win64版](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip)

### unzip

```txt:
project/
├── chromedriver/
│   └── chromedriver.exe
└── Example/
    └── example_selenium.py
```

## Selenium

```sh:
pip install selenium
```

```python:
from selenium import webdriver

def google_search(string):
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.jp/")
    driver.implicitly_wait(1)
    search_box = driver.find_element("name", "q")
    search_box.send_keys(string)
    search_box.submit()
    driver.implicitly_wait(3)
    html = driver.page_source
    driver.quit()

    return html

if __name__ == "__main__":
    html = google_search("selenium")
    print(html)
```
