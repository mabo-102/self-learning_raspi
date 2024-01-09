# Bluetooth

## 仕様策定

- Bluetooth SIG: [https://www.bluetooth.com/](https://www.bluetooth.com/)


## 設定ファイル

1. **/etc/bluetooth/xxx.conf:**
   - **main.conf:** Bluetoothデーモン (`bluetoothd`) の動作に関する様々な設定が含まれています。
   セキュリティ設定やデフォルトのBluetoothデバイス名などが変更可能です。
   - **input.conf:** Bluetooth入力デバイスの動作をカスタマイズするために使用されます。
   - **network.conf:** ネットワーク関連のBluetoothサービスに関する設定を行います。

2. **/lib/systemd/system/bluetooth.service:**
   - Bluetoothデーモンのsystemdユニットファイルが含まれています。
   サービスの実行方法や依存関係、権限などが定義されています。

### Bluetooth ツール

#### btmon

- Bluetoothのトレースモニタリングを行うためのコマンドラインツール

```sh:
$ sudo btmon -w /Dev/HEMS/log/btmon.log
```

#### bluetoothctl

```sh:
$ bluetoothctl
[bluetooth]# scan on
Failed to start discovery: org.bluez.Error.InProgress
[NEW] Device A4:38:CC:XX:XX:XX Joy-Con (L)
[NEW] Device A4:38:CC:YY:YY:YY Joy-Con (R)
```

```sh:
[bluetooth]# pair <MAC Address>
Attempting to pair with A4:38:CC:XX:XX:XX
[CHG] Device A4:38:CC:XX:XX:XX Connected: yes
[CHG] Device A4:38:CC:XX:XX:XX Modalias: usb:v057Ep2006xxxxx
[CHG] Device A4:38:CC:XX:XX:XX UUIDs: 00001000-0000-1000-8000-0080xxxxxxxx
[CHG] Device A4:38:CC:XX:XX:XX ServicesResolved: yes
[CHG] Device A4:38:CC:XX:XX:XX Paired: yes
Pairing successful
```

```sh:
[bluetooth]# paired-devices
Device A4:38:CC:XX:XX:XX Joy-Con (L)
```

```sh:
[bluetooth]# trust <MAC Address>
[CHG] Device A4:38:CC:XX:XX:XX Trusted: yes
Changing A4:38:CC:XX:XX:XX trust succeeded
```

```sh:
[bluetooth]# connect <MAC Address>
Attempting to connect to A4:38:CC:XX:XX:XX
[CHG] Device A4:38:CC:XX:XX:XX Connected: yes
Connection successful
[CHG] Device A4:38:CC:XX:XX:XX ServicesResolved: yes
```

```sh:
[Joy-Con (L)]# info A4:38:CC:XX:XX:XX
Device A4:38:CC:XX:XX:XX (public)
        Name: Joy-Con (L)
        Alias: Joy-Con (L)
        Class: 0x00002508
        Icon: input-gaming
        Paired: yes
        Trusted: yes
        Blocked: no
        Connected: yes
        WakeAllowed: no
        LegacyPairing: no
        UUID: Service Discovery Serve.. (00001000-0000-1000-8000-0080xxxxxxxx)
        UUID: Human Interface Device... (00001124-0000-1000-8000-0080xxxxxxxx)
        UUID: PnP Information           (00001200-0000-1000-8000-0080xxxxxxxx)
        Modalias: usb:v057Ep2006xxxxx
```
