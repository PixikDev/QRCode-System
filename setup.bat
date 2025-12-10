@echo off
echo Установка зависимостей..
py -m venv venv
call venv\Scripts\activate
pip install qrcode[pil]
echo.
echo Зависимости установлены!
echo python main.py
pause