import subprocess
from time import sleep

commands = [
    "service ssh start",
    "service ssh reload",
    "service ssh restart",
]
for command in commands:
    subprocess.check_call(command, shell=True)

while True:
    sleep(60)