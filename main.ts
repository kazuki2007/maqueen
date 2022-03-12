input.onButtonPressed(Button.A, function () {
    動作 = 0
})
input.onButtonPressed(Button.B, function () {
    動作 = 1
})
let 動作 = 0
動作 = 0
basic.forever(function () {
    if (動作 == 0) {
        if (input.soundLevel() > 100) {
            maqueen.motorStop(maqueen.Motors.All)
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
            maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
        } else if (maqueen.Ultrasonic(PingUnit.Centimeters) <= 20) {
            if (maqueen.Ultrasonic(PingUnit.Centimeters) <= 6) {
                maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
                maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
                basic.showLeds(`
                    # . . . #
                    . # . # .
                    . . # . .
                    . . . . .
                    . . . . .
                    `)
                maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 50)
            } else {
                basic.showLeds(`
                    . . # . .
                    . . # . .
                    . . # . .
                    . . . . .
                    . . # . .
                    `)
                maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
                maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 100)
            }
        } else {
            basic.showLeds(`
                # # # # #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 150)
            maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
            maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
        }
    } else if (動作 == 1) {
        basic.showLeds(`
            # # . # #
            . . . . .
            # . # . #
            . . . . .
            # # . # #
            `)
        maqueen.motorStop(maqueen.Motors.All)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    }
})
