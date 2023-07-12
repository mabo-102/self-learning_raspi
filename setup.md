# RaspberryPiのセットアップ

## 【ダウンロードするもの】

- [Raspberry Imager(Win)](https://downloads.raspberrypi.org/imager/)
- [RaspberryPiのOS](https://www.raspberrypi.com/software/operating-systems/)

## 【必要な機材】

- パソコン
- 液晶モニタ
- USBキーボード
- USBマウス
- microSD (32GB以上でクラス10のものを推奨)
- microSDカード対応マルチカードリーダー／ライター
- HDMIアダプタ(miniHDMI→HDMI)
- HDMIケーブル
- USBアダプタ(microUSB→USBタイプAメス)
- USBハブ

## ■ OSインストール手順

1. イメージャーをインストールする
  - RasPi Zero: 32bit版
  - RasPi 3B+: 64bit版
1. microSDにOSを焼く
  1. 初期設定をする(ネットワーク、SSHなど)
1. RasPi起動
  1. SSHで接続確認
  1. ファイアウォール設定(お好みで)


- [公式：SSH設定](https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server)


### 公開鍵方式で SSH 接続

```sh:
>ssh-keygen -t ed25519 -f id_ed25519_raspi -C "your_email@example.com"
```

### アクセス権限の設定

- id_ed25519_raspi.pub をラズパイに転送
- .ssh フォルダに authorized_keys のファイル名で保存

```sh:
>chmod 600 .ssh/authorized_keys
>chmod 700 .ssh
```

### SSH設定

#### /etc/ssh/sshd‗config.d/sshd_mabo.conf

- ポート番号の変更
- rootでのログイン禁止
- パスワード認証の禁止
- 公開鍵認証の許可
  - 認証鍵ファイルの指定

```sh:
>vi sshd_mabo.conf
Port 55022

PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile   %h/.ssh/authorized_keys
:wq
```

### ファイアウォール設定

- 同一ネットワークからの SSH のみ許可

```sh:
>sudo apt list ufw
>sudo apt install ufw
>sudo ufw status
Status: inactive
>sudo ufw default deny
>sudo ufw allow from 192.168.xx.0/24 to any port 55022
>sudo ufw enable
>sudo reboot
```

### SSH接続確認

```sh:OK
>ssh -i id_ed25519_raspi mabo@192.168.xx.xx -p 55022
```

```sh:NG
>ssh  mabo@192.168.xx.xx -p 55022
mabo@192.168.100.200: Permission denied (publickey).
```

### SSH接続の設定(接続元)

#### mabo/.ssh/config

```sh:
Host raspi
    HostName 192.168.xx.xxx
    Port 55022
    User mabo
    IdentityFile ~/.ssh/id_ed25519_raspi
```

```sh:OK
>ssh raspi
```
