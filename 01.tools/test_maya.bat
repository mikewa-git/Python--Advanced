@echo off

:: --- maya version ---
set "MAYA_VERSION=2022"

:: --- set the directory of maya ---
set "TEST_DIR=C:/Program Files/Autodesk/Maya%MAYA_VERSION%"

:: --- set the path ---
set "PATH=%TEST_DIR%/bin;%PATH%

:: --- starting maya ---
start "" "%test_dir%/bin/maya.exe