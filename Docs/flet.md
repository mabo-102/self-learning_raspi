# Flet on Raspberry Pi 3B+

## Install

### flet

```sh:
python -m pip install --upgrade pip
python -m venv WbApp
cd WebApp
source bin/activate
```

### GStreamer

```sh:
sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

## HelloWorld

```py:app.py
import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

ft.app(target=main)
```

### flet run

```sh:
flet run app.py
```

## トラブルシューティング

### cannot open display

```sh:
(flet:1606): Gtk-WARNING **: 00:08:07.072: cannot open display

echo $DISPLAY

export DISPLAY=:0.0
echo $DISPLAY
:0.0
```

### gdk_window_get_state

```sh:
(flet:1618): Gdk-CRITICAL **: 00:08:49.490: gdk_window_get_state: assertion 'GDK_IS_WINDOW (window)' failed
```
