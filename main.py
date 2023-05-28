def back_to_the_track():
    reromicro.move_backward(50)
    basic.pause(250)
    reromicro.brake()
def right_180():
    reromicro.turn_right(50)
    basic.pause(460)
    reromicro.brake()
def left_90():
    reromicro.turn_left(50)
    basic.pause(250)
    reromicro.brake()
speed = 35
strip = neopixel.create(DigitalPin.P1, 7, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
basic.pause(500)
left_90()
basic.pause(500)
strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
basic.pause(500)
right_180()
basic.pause(500)
strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
basic.pause(500)
left_90()
basic.pause(500)
strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
basic.pause(500)
back_to_the_track()
basic.pause(500)
strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
basic.pause(500)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
left_90()

def on_forever():
    global speed
    reromicro.read_line_sensors()
    if reromicro.line_sensor_detects_line(LineSensors.LEFT) and (reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.RIGHT)):
        reromicro.brake()
        basic.pause(100)
        strip.show_rainbow(1, 100)
        right_180()
        basic.pause(500)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    elif reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.RIGHT):
        reromicro.run_motor(Motors.LEFT, speed)
        reromicro.run_motor(Motors.RIGHT, 35)
    elif reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.LEFT):
        reromicro.run_motor(Motors.LEFT, 35)
        reromicro.run_motor(Motors.RIGHT, speed)
    elif reromicro.line_sensor_detects_line(LineSensors.CENTER):
        reromicro.run_motor(Motors.LEFT, speed)
        reromicro.run_motor(Motors.RIGHT, speed)
    elif reromicro.line_sensor_detects_line(LineSensors.LEFT):
        reromicro.run_motor(Motors.LEFT, 0)
        reromicro.run_motor(Motors.RIGHT, speed)
    elif reromicro.line_sensor_detects_line(LineSensors.RIGHT):
        reromicro.run_motor(Motors.LEFT, speed)
        reromicro.run_motor(Motors.RIGHT, 0)
    if reromicro.read_ultrasonic() <= 5:
        basic.clear_screen()
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        speed = 0
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif reromicro.read_ultrasonic() > 5 and reromicro.read_ultrasonic() <= 15:
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        basic.clear_screen()
        speed = 0
        basic.show_icon(IconNames.ANGRY)
    elif reromicro.read_ultrasonic() > 15 and reromicro.read_ultrasonic() <= 25:
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        basic.clear_screen()
        speed = 0
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    else:
        basic.clear_screen()
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        speed = 35
basic.forever(on_forever)
