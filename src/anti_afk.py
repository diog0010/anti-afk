import pyautogui as pag, sys

x, y = pag.size()

pag.moveTo(x/2, y/2)

try:
    print("Press CTRL+C to stop the program.")
    while True:
        pag.moveTo(x/2+15, y/2, 2)
        pag.moveTo(x/2-15, y/2, 2)
except KeyboardInterrupt:
    print("Shutting down...")
    sys.exit()