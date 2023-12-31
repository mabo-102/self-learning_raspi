import requests
import re


class Scraper:
    def __init__(self) -> None:
        self.target_url = None
        self.res = None


    def target(self, url) -> None:
        self.target_url = url


    def scraping(self):
        self.res = requests.get(self.target_url)
    

    def search(self, word):
        return re.search(word, self.res.text)


if __name__ == "__main__":
    nikkei = Scraper()
    nikkei.target("https://www.nikkei.com/markets/worldidx/chart/nk225/")
    nikkei.scraping()

    if nikkei.res.status_code == 200:
        print("Nikkei status OK")

        m = nikkei.search('class="economic_value_now a-fs26"')
        idx = m.end()
        print(f'{nikkei.res.text[idx+1:idx+10]} 円')

        m = nikkei.search('class="economic_value_time a-fs14"')
        idx = m.end()
        print(f'{nikkei.res.text[idx+2:idx+12]}')

        m = nikkei.search('class="economic_balance_value a-fs18"')
        idx = m.end()
        print(f'{nikkei.res.text[idx+1:idx+7]}')

        m = nikkei.search('class="economic_balance_percent a-fs18"')
        idx = m.end()
        print(f'{nikkei.res.text[idx+2:idx+8]}')
