# スクレイピング

## requests によるスクレイピング

### requests のインストール

```python
> pip install requests
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
Collecting charset-normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.3.2-cp311-cp311-win_amd64.whl.metadata (34 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.6-py3-none-any.whl.metadata (9.9 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Downloading urllib3-2.1.0-py3-none-any.whl.metadata (6.4 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2023.11.17-py3-none-any.whl.metadata (2.2 kB)
Downloading requests-2.31.0-py3-none-any.whl (62 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 1.7 MB/s eta 0:00:00
:
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2023.11.17 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.1.0
```

```python
> pip list
Package            Version
------------------ ----------
certifi            2023.11.17
charset-normalizer 3.3.2
idna               3.6
pip                23.3.1
requests           2.31.0
setuptools         69.0.2
urllib3            2.1.0
```

### 日経新聞のサイトから日経平均株価を取得する

```python
import requests

url = "https://www.nikkei.com/markets/worldidx/chart/nk225/"
res = requests.get(url)
if res.status_code == 200:
    print("Status OK")
    kwd = 'class="economic_value_now a-fs26"'
    idx = res.text.find(kwd) + len(kwd)
    price = ""
    for n in res.text[idx+1:idx+11]:
        if n in ",.0123456789":
            price += n
    print(f"{price} 円")
else:
    print("Status NG")
```