@echo off
cd /d %~dp0
set data_dir=../COVID-19
for %%i in (0 1 5 10 15 20) do python COVID-19.py %data_dir% ./Stage-%%i %%i

for /f "delims=1* delims= " %%t in ('date /T ') do set dt=%%t
for /f "delims=" %%t in ('time /T ') do set tm=%%t
git add .
git commit -m "%dt% %tm%"
git push