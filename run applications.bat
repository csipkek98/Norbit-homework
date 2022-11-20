@Echo Off
cd /D "Coordinate Provider"
start cmd /k call "run.bat"
cd ../
cd /D "Server"
start cmd /k call "run.bat"
cd ../
cd /D "Client"
start cmd /k call "run.bat"