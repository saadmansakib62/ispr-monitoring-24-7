@echo off
title ISPR News Monitoring System Launcher
echo ==========================================================
echo   ISPR NEWS MONITORING SYSTEM - WINDOWS LAUNCHER
echo ==========================================================
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Python detected. Installing dependencies and starting C2 Server...
    pip install -q -r requirements.txt
    start "" "http://127.0.0.1:5000"
    python app.py
) else (
    echo Launching standalone ISPR Web Application...
    start msedge --app="file:///%~dp0index.html" --window-size=1420,880 2>nul || start chrome --app="file:///%~dp0index.html" --window-size=1420,880 2>nul || start "" "%~dp0index.html"
)