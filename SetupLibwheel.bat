@echo off
set inSource=%1
set source=%inSource%

IF "%source%" == "" (
	set source=.
)

echo SetupPath Source: %source%

set mypath=%cd%
cd %source%

rd /S /Q \build
rd /S /Q \wheel

python.exe setup.py bdist_wheel -d wheel

cd wheel

FOR %%G IN (*.whl) do (pip.exe install --upgrade "%%G")
