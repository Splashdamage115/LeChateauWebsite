@echo off
REM Set window title
title SQL Server

cd /d "C:\Program Files\MariaDB 11.6\bin"
mysql -u root --password=Password

REM Pause the command prompt so it doesn't close immediately
pause