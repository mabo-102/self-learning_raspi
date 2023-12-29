# I2C

## I2Cの有効化

```sh:
sudo raspi-config

3 Interface Options    Configure connections to peripherals

I5 I2C           Enable/disable automatic loading of I2C kernel module
Would you like the ARM I2C interface to be enabled?
<Yes>

The ARM I2C interface is enabled
<OK>
```

## LCD接続

```sh:
   3V3  (1) : VDD
 GPIO2  (3) : SDA   
 GPIO3  (5) : SLC
 GPIO4  (7) : RST
 ```

## I2Cデバイスの確認

```sh:
i2cdetected -y 1

(HEMS) mabo@hems:~/Dev/HEMS $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- 3e -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```

## Python on pigpio

- Instractionテーブルの定義: Instraction.py
- [AE-AQM0802+PCA9515 LCD(8x2)](https://akizukidenshi.com/catalog/g/gK-11354/)用 Pythonサンプルコード: AQM0802.py