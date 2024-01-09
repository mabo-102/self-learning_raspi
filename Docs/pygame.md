# pygame

## install

```sh:
pip install pygame
```

### NotImplementedError

#### libSDL2-2.0.so.0

```sh:
???Error: モジュール無いよ
```

```sh:
$ sudo apt install libsdl2-2.0.0
```

#### libSDL2_ttf-2.0.so.0

```sh:
NotImplementedError: font module not available (ImportError: libSDL2_ttf-2.0.so.0: cannot open shared object file: No such file or directory)
```

```sh:
$ sudo apt install libsdl2-ttf-2.0-0
```

## Console Application

```sh:
pygame.error: video system not initialized

```

- [DummyVideoDriver](https://www.pygame.org/wiki/DummyVideoDriver)


### Joy-Con(L)

<details>
<summary>イベント</summary>
<div>

| 操作 | Event | 値 |
|:-:|:-:|:-:|
|◀|1539-JoyButtonDown, 1540-JoyButtonUp|0|
|▼|1539-JoyButtonDown, 1540-JoyButtonUp|1|
|▲|1539-JoyButtonDown, 1540-JoyButtonUp|2|
|▶|1539-JoyButtonDown, 1540-JoyButtonUp|3|
|SL|1539-JoyButtonDown, 1540-JoyButtonUp|4|
|SR|1539-JoyButtonDown, 1540-JoyButtonUp|5|
|－|1539-JoyButtonDown, 1540-JoyButtonUp|8|
|スティック|1539-JoyButtonDown, 1540-JoyButtonUp|10|
|〇|1539-JoyButtonDown, 1540-JoyButtonUp|13|
|L|1539-JoyButtonDown, 1540-JoyButtonUp|14|
|LZ|1539-JoyButtonDown, 1540-JoyButtonUp|15|
|スティック(中)|1538-JoyHatMotion|(0, 0)|
|スティック(左)|1538-JoyHatMotion|(0, -1)|
|スティック(下)|1538-JoyHatMotion|(1, 0)|
|スティック(上)|1538-JoyHatMotion|(-1, 0)|
|スティック(右)|1538-JoyHatMotion|(0, 1)|
|スティック(左上)|1538-JoyHatMotion|(-1, -1)|
|スティック(左下)|1538-JoyHatMotion|(1, -1)|
|スティック(右上)|1538-JoyHatMotion|(-1, 1)|
|スティック(右下)|1538-JoyHatMotion|(1, 1)|

</div>
</details>