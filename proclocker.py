import psutil
import subprocess

while True:
    band = 0
    for proc in psutil.process_iter():
        if proc.name() == 'estatus.exe':
            band = 1
            
    if band == 1:
        print("Archivo Activo")
    elif band == 0:
        print("No Encontrado")
        subprocess.call('estatus.exe')
