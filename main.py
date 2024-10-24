col = 0
row = 0
basic.show_icon(IconNames.GHOST)

def on_forever():
    global row, col
    for index in range(4):
        if input.sound_level() > 128:
            row = randint(5, 0)
            col = randint(5, 0)
        if led.point(col, row):
            led.unplot(col, row)
            basic.pause(50)
            led.plot(col + 1, row)
        basic.pause(150)
        basic.show_icon(IconNames.GHOST)
basic.forever(on_forever)
