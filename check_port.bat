@echo off
set port=%1
:loop
netstat -na | find "%port%" && (
    echo Port %port% open.
) || (
    echo Port %port% not open. Retrying.
    timeout /t 1 /nobreak > nul
    goto loop
)
