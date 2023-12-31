import requests

"""todo:
- bs4: https://www.crummy.com/software/BeautifulSoup/

  ```sh:
  pip install beautifulsoup4
  ```

- se: https://www.selenium.dev/ja/
  - Selenium is don't work on RasPi zero.

  Chromium WebDriver:
    https://www.chromium.org/Home

    ```sh:
    sudo apt-get update
    sudo apt-get install chromium-chromedriver
    ```

  GeckoDriver (Firefox):
    https://github.com/mozilla/geckodriver

    ```sh:
    sudo apt-get install firefox-geckodriver
    ```

  Microsoft Edge WebDriver:
    https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

  Safari WebDriver:
    https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari
"""

url = "https://www.nikkei.com/markets/worldidx/chart/nk225/"
tbl = 'class="cmnc-nikkei_stock"'

url2= "https://www.nikkei.com/markets/worldidx/"
cmn_tbl = 'class="cmn-table_style1"'

res = requests.get(url)
if res.status_code == 200:
    print("Nikkei status OK")
    kwd = 'class="economic_value_now a-fs26"'
    idx = res.text.find(kwd) + len(kwd)
    price = ""
    for n in res.text[idx+1:idx+11]:
        if n in ",.0123456789":
            price += n
    print(f"{price} 円")
