@echo off
REM Set window title
title Flask Server

REM Call the SQL Server batch file in the background
start /min cmd /c call sqlServer.bat

REM Set The directory
cd /d "%~dp0"

REM Open Visual Studio Code
start /min cmd /c "code ."

REM Check if the virtual environment exists and activate it
if exist scripts\activate (
    echo Activating virtual environment...
    call scripts\activate
) else (
    echo Virtual environment not found.
)

REM Set Flask environment variable
set FLASK_ENV=development

REM Run the Flask app
echo Starting the Flask server...
python app.py

REM Pause the command prompt so it doesn't close immediately
pause
