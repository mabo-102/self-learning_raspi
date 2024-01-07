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
