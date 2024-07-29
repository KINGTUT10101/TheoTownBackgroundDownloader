@ECHO OFF

py backgroundDownloader.py %USERPROFILE%\Pictures\TheoTown_Gallery

IF ERRORLEVEL 1 (
    ECHO ================
    ECHO NOTE: An error has occured. Please contact the developer of this script for help.
    PAUSE
)