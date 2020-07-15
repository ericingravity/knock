# knock GUI
Simple GUI for [grongor/knock](https://github.com/grongor/knock) made with PyQt5 and python3 with ability to save and load knock configurations.

## Setup
You'll need PyQt5. To install it, do `pip install pyqt5`.

If you make any changes to the .ui file, you can generate a new python file using `python -m PyQt5.uic.pyuic -x knock_window.ui -o knock_window.py`.

If you'd like to make this a standalone program, I'd recommend using [pyinstaller](https://pypi.org/project/PyInstaller/).

## Screenshots
#### macOS
![macos_knockgui](https://user-images.githubusercontent.com/26295329/87505139-bcb49280-c62d-11ea-8491-803392f00ee6.png)
#### Windows
![win_knockgui](https://user-images.githubusercontent.com/26295329/87504909-4152e100-c62d-11ea-8402-83f4b60d3001.png)