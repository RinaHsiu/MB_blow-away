let col = 0
let row = 0
basic.showIcon(IconNames.Ghost)
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
        if (input.soundLevel() > 128) {
            row = randint(5, 0)
            col = randint(5, 0)
        }
        if (led.point(col, row)) {
            led.unplot(col, row)
            basic.pause(50)
            led.plot(col + 1, row)
        }
    }
})
