@echo off

if not exist "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ubAutoRedar.exe" (
	copy "%~p0\ubAutoRedar.exe" "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" 
	copy "%~p0\ubAutoRedar.exe" "C:\Documents and Settings\%USERNAME%\Start Menu\Programs\Startup" 
	copy "%~p0\ubAutoRedar.exe" "C:\Documents and Settings\All Users\Start Menu\Programs\Startup"
)