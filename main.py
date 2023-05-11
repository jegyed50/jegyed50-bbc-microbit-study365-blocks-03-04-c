# https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-c
# https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-a/blob/master/03-04-pomodoro-timeline.jpg
# JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-04-C
# 30 perces analóg óra, fél másoperces időtartamok, csak LED és pause
# Mint a B megoldás, de egy 4-es FOR ciklussal

def on_button_pressed_a():
    basic.show_string("w")
    basic.pause(2500)
    basic.show_string("R")
    basic.pause(500)
    basic.show_string("w")
    basic.pause(2500)
    basic.show_string("R")
    basic.pause(500)
    basic.show_string("w")
    basic.pause(2500)
    basic.show_string("w")
    basic.show_string("R")
    basic.pause(1500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
