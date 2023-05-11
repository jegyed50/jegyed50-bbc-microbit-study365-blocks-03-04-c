// https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-c
// https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-a/blob/master/03-04-pomodoro-timeline.jpg
// JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-04-C
// 30 perces analóg óra, fél másoperces időtartamok, csak LED és pause
// Mint a B megoldás, de egy 4-es FOR ciklussal
input.onButtonPressed(Button.A, function () {
    basic.showString("w")
    basic.pause(2500)
    basic.showString("R")
    basic.pause(500)
    basic.showString("w")
    basic.pause(2500)
    basic.showString("R")
    basic.pause(500)
    basic.showString("w")
    basic.pause(2500)
    basic.showString("w")
    basic.pause(1500)
    basic.showString("R")
    basic.clearScreen()
})
basic.forever(function () {
	
})
