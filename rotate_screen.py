import rotatescreen
screens = rotatescreen.get_secondary_displays()
if len(screens)>0:
    screen = screens[0]
    width = abs(screen.info['Monitor'][0])
    height = abs(screen.info['Monitor'][-1])
    if width>height:
        screen.rotate_to(90)
    else:
        screen.rotate_to(0)