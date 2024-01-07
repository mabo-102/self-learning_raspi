from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DEBUG = True
TARGET_URL = "https://www.rakuten-sec.co.jp/web/market/data/list.html"

def get_page_source(url):
    """
    Get the HTML page source of the given URL.

    :param url: The URL to get the page source from.
    :return: The HTML page source.

    Example:
    >>> get_page_source("https://www.example.com")
    '<html>...</html>'
    """
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(5)
    html = driver.page_source
    driver.quit()
    return html

def extract_data_from_table(table_element, target_stocks, header_skip=True):
    """
    Extract data from the given table element.

    :param table_element: The table element to extract data from.
    :param target_stocks: List of stocks to extract information for.
    :param header_skip: Whether to skip the header row (default is True).

    Example:
    >>> extract_data_from_table(table_element, ["Stock1", "Stock2"])
    Stock1:
    現在値: 100
    前日比: +5
    前日比率: 5%
    更新日時: 2024-01-07 12:00:00

    Stock2:
    現在値: 50
    前日比: -2
    前日比率: -4%
    更新日時: 2024-01-07 12:30:00
    """
    rows = table_element.find_all('tr')[1:] if header_skip else table_element.find_all('tr')
    
    for row in rows:
        name = row.th.a.text.strip()
        
        if name in target_stocks:
            columns = row.find_all('td')
            values = [col.text.strip() for col in columns]
            
            print(f"{name}:")
            for header, value in zip(["現在値", "前日比", "前日比率", "更新日時"], values):
                print(f"{header}: {value}")
            print("\n")

def process_data(data_type, stocks, soup):
    """
    Process data of a specific type (e.g., tInd, tFx).

    :param data_type: The type of data to process.
    :param stocks: List of stocks to extract information for.
    :param soup: BeautifulSoup object for parsing HTML.

    Example:
    >>> process_data('tInd', ["Stock1", "Stock2"], soup)
    === tInd情報 ===
    Stock1:
    現在値: 100
    前日比: +5
    前日比率: 5%
    更新日時: 2024-01-07 12:00:00

    Stock2:
    現在値: 50
    前日比: -2
    前日比率: -4%
    更新日時: 2024-01-07 12:30:00

    >>> process_data('tFx', ["Currency1", "Currency2"], soup)
    === tFx情報 ===
    Currency1:
    現在値: 1.20
    前日比: +0.05
    前日比率: 4%
    更新日時: 2024-01-07 13:00:00

    Currency2:
    現在値: 0.90
    前日比: -0.02
    前日比率: -2%
    更新日時: 2024-01-07 13:30:00
    """
    element = soup.find('div', id=data_type)
    table = element.find('table', class_='tbl-data-01')
    
    print(f"=== {data_type}情報 ===")
    extract_data_from_table(table, stocks)

def main():
    html = get_page_source(TARGET_URL)
    soup = BeautifulSoup(html, 'html.parser')

    process_data('tInd', ["TOPIX", "NYダウ"], soup)
    process_data('tFx', ["米ドル/円"], soup)

if __name__ == "__main__":
    main()
