# 初期設定

## pigpio

- [pigpio](http://abyz.me.uk/rpi/pigpio/)

### インストール

- 最新のRasPi OSにはインストール済

```sh:
sudo apt install pigpio python3-pigpio
```

### 自動起動設定

```sh:
$ sudo systemctl enable pigpiod.service
$ sudo shutdown -r now

# リブート後の確認
$ sudo systemctl status pigpiod.service
```