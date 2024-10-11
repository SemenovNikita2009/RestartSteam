import signal
import psutil
import os

steamPName = {"steam.exe", "steamservice.exe", "steamwebhelper.exe", "GameOverlayUI.exe"}

def getProcessId(processName):
    for process in psutil.process_iter():
        if process.name() == processName:
            return process.pid

steamP = {}
for process in steamPName:
    steamP[process] = getProcessId(process)

for process in steamP:
    try:
        os.kill(steamP[process], signal.SIGTERM)
        print(f"\"{process}\" успешно завершен.")
    except:
        print(f"Не удалось завершить \"{process}\"")

input("Для выхода нажмите любую кнопку...")