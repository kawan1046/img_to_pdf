cd %~dp0
set target=img_to_pdf
call venv\Scripts\activate
pyinstaller %target%.py --onefile
rem --noconsole
move dist\%target%.exe %target%.exe
rmdir /s /q dist
rmdir /s /q build
del %target%.spec
pause