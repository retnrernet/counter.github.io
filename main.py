from pyscript import document
import time

counter = document.getElementById("counter")
i = 1

while True:
    counter.innerHTML = str(i)
    time.sleep(1)
    i += 1
