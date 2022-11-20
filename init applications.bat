@Echo Off
cd /D "Coordinate Provider"
start cmd /c call "init.bat"
cd ../
cd /D "Server"
start cmd /c call "init.bat"
cd ../
cd /D "Client"
start cmd /c call "init.bat"