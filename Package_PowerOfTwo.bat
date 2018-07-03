rem Build PowerOfTwo
call "PowerOfTwo_Build.bat"
cd ..

rem Copy files into place
rem When prompted to decide between file and dir, choose dir
xcopy /s /y .\PowerOfTwo\build\exe.win-amd64-3.6 .\PowerOfTwo_Standalone\
xcopy /s /y .\PowerOfTwo\PowerOfTwo_Extras .\PowerOfTwo_Standalone\

rem Remove leftovers
del .\PowerOfTwo_Standalone\results.txt

rem Package the utility
7z u .\Netrve_PowerOfTwo_Standalone.7z .\PowerOfTwo_Standalone\*