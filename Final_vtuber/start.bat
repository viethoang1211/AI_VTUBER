@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set VIRTUAL_ENV=./waifu

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(waifu) %PROMPT%

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%
set VIRTUAL_ENV_PROMPT=(waifu) 

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)

echo Installing dependencies...

call npm install ./character_ai/

@REM python -m ensurepip
@REM python -m pip install --upgrade pip
@REM python -m pip install pipwin 
@REM rem we have to use pipwin for installing pyaudio
@REM python -m pipwin install pyaudio 
@REM python -m pip install -r requirements.txt 
@REM python -m pip install SpeechRecognition
@REM python -m pip install pocketsphinx
@REM python -m pip install soundfile
@REM python -m pip install edge-tts
@REM python -m pip install sounddevice
@REM python -m pip install git+https://github.com/openai/whisper.git 

cls

python waifu/Src/runner.py

pause