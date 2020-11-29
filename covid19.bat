@echo off
cd /d %~dp0
python covid19.py ../COVID-19 ./Stage-0 0
python covid19.py ../COVID-19 ./Stage-10 10
python covid19.py ../COVID-19 ./Stage-15 15
python covid19.py ../COVID-19 ./Stage-20 20

for /f "delims=" %%t in ('date /T ') do set dt=%%t
for /f "delims=" %%t in ('time /T ') do set tm=%%t

git add .
git commit -m "%dt% %tm%"
git push