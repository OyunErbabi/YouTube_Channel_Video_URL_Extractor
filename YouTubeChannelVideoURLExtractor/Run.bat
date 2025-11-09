@echo off
title YouTube Video Extractor - Installer and Launcher
color 0A

echo ====================================================
echo    YouTube Channel Video URL Extractor
echo    One-Click Install and Run
echo ====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed
echo.

REM Check if requirements.txt exists, if not create it
if not exist requirements.txt (
    echo [INFO] Creating requirements.txt...
    (
        echo selenium
        echo webdriver-manager
    ) > requirements.txt
)

REM Check if extractor.py exists
if not exist extractor.py (
    color 0C
    echo [ERROR] extractor.py not found!
    echo Please make sure extractor.py is in the same folder.
    echo.
    pause
    exit /b 1
)

echo [INFO] Checking and installing required packages...
echo This may take a few minutes on first run...
echo.

REM Install/upgrade pip
python -m pip install --upgrade pip --quiet

REM Install required packages
python -m pip install -r requirements.txt --quiet

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] Failed to install required packages!
    echo.
    echo Trying alternative installation method...
    echo.
    
    REM Try installing packages one by one
    echo Installing selenium...
    python -m pip install selenium
    
    echo Installing webdriver-manager...
    python -m pip install webdriver-manager
    
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Installation failed. Please check your internet connection.
        pause
        exit /b 1
    )
)

echo.
echo [SUCCESS] All packages installed successfully!
echo.
echo ====================================================
echo    Launching YouTube Video Extractor...
echo ====================================================
echo.

REM Run the extractor
python extractor.py

REM Exit immediately after program closes
exit