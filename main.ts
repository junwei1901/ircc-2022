function back_to_the_track () {
    reromicro.MoveBackward(50)
    basic.pause(250)
    reromicro.Brake()
}
function right_180 () {
    reromicro.TurnRight(50)
    basic.pause(460)
    reromicro.Brake()
}
function left_90 () {
    reromicro.TurnLeft(50)
    basic.pause(250)
    reromicro.Brake()
}
let speed = 35
let strip = neopixel.create(DigitalPin.P1, 7, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Green))
basic.pause(500)
left_90()
basic.pause(500)
strip.showColor(neopixel.colors(NeoPixelColors.Orange))
basic.pause(500)
right_180()
basic.pause(500)
strip.showColor(neopixel.colors(NeoPixelColors.Blue))
basic.pause(500)
left_90()
basic.pause(500)
strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
basic.pause(500)
back_to_the_track()
basic.pause(500)
strip.showColor(neopixel.colors(NeoPixelColors.White))
basic.pause(500)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
left_90()
basic.forever(function () {
    reromicro.ReadLineSensors()
    if (reromicro.LineSensorDetectsLine(LineSensors.Left) && (reromicro.LineSensorDetectsLine(LineSensors.Center) && reromicro.LineSensorDetectsLine(LineSensors.Right))) {
        reromicro.Brake()
        basic.pause(100)
        strip.showRainbow(1, 100)
        right_180()
        basic.pause(500)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
    } else if (reromicro.LineSensorDetectsLine(LineSensors.Center) && reromicro.LineSensorDetectsLine(LineSensors.Right)) {
        reromicro.RunMotor(Motors.Left, speed)
        reromicro.RunMotor(Motors.Right, 35)
    } else if (reromicro.LineSensorDetectsLine(LineSensors.Center) && reromicro.LineSensorDetectsLine(LineSensors.Left)) {
        reromicro.RunMotor(Motors.Left, 35)
        reromicro.RunMotor(Motors.Right, speed)
    } else if (reromicro.LineSensorDetectsLine(LineSensors.Center)) {
        reromicro.RunMotor(Motors.Left, speed)
        reromicro.RunMotor(Motors.Right, speed)
    } else if (reromicro.LineSensorDetectsLine(LineSensors.Left)) {
        reromicro.RunMotor(Motors.Left, 0)
        reromicro.RunMotor(Motors.Right, speed)
    } else if (reromicro.LineSensorDetectsLine(LineSensors.Right)) {
        reromicro.RunMotor(Motors.Left, speed)
        reromicro.RunMotor(Motors.Right, 0)
    }
    if (reromicro.ReadUltrasonic() <= 5) {
        basic.clearScreen()
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        speed = 0
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    } else if (reromicro.ReadUltrasonic() > 5 && reromicro.ReadUltrasonic() <= 15) {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        basic.clearScreen()
        speed = 0
        basic.showIcon(IconNames.Angry)
    } else if (reromicro.ReadUltrasonic() > 15 && reromicro.ReadUltrasonic() <= 25) {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        basic.clearScreen()
        speed = 0
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
    } else {
        basic.clearScreen()
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        speed = 35
    }
})
