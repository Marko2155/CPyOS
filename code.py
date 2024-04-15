import board
import digitalio
import displayio
import microcontroller

b1 = digitalio.DigitalInOut(board.BUTTON_3)
b2 = digitalio.DigitalInOut(board.BUTTON_2)
b3 = digitalio.DigitalInOut(board.BUTTON_1)

app = "home"



display = board.DISPLAY



def pictureView():
    import time
    import terminalio
    from adafruit_display_text import label
    tlabel = label.Label(terminalio.FONT, text="Loading bitmaps in /sd/ folder...", color=0xFFFFFF)
    tlabel.y = 5
    display.root_group = tlabel
    time.sleep(2)
    paths = ["/sd/purple.bmp", "/sd/retro.bmp"]
    path = 0
    def refresh():
        bitmap = displayio.OnDiskBitmap(paths[path])

        display.auto_refresh = True



        tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

        group = displayio.Group()

        group.append(tile_grid)

        display.root_group = group
    ididit1 = False
    ididit2 = False
        
    refresh()

    while True:
        if b1.value == False and ididit1 == False and path > 0:
            path = path - 1
            ididit1 = True
            refresh()
        elif b1.value == True and ididit1 == True:
            ididit1 = False
        if b2.value == False and ididit2 == False and path < len(paths) - 1:
            path = path + 1
            ididit2 = True
            refresh()
        elif b2.value == True and ididit2 == True:
            ididit2 = False
            

import terminalio
from adafruit_display_text import label
apps = ["pictureview"]
option = 0
text = "CPyOS v1.0" + "\nChoose app: " + apps[option] + "\nTo close app, restart device"
    
tlabel = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
tlabel.y = 5
display.root_group = tlabel
ididit1 = False
ididit2 = False
while True:
    text = "Choose app: " + apps[option]
    if b1.value == False and ididit1 == False and option > 0:
        option = option - 1
        ididit1 = True
        text = "CPyOS v1.0" + "\nChoose app: " + apps[option] + "\nTo close app, restart device"
    
        tlabel = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
        tlabel.y = 5
        display.root_group = tlabel
    elif b1.value == True and ididit1 == True:
        ididit1 = False
    if b2.value == False and ididit2 == False and option < len(apps) - 1:
        option = option + 1
        ididit2 = True
        text = "CPyOS v1.0" + "\nChoose app: " + apps[option] + "\nTo close app, restart device"
    
        tlabel = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
        tlabel.y = 5
        display.root_group = tlabel
    elif b2.value == True and ididit2 == True:
        ididit2 = False
    elif b3.value == False:
        if apps[option] == "pictureview":
            pictureView()