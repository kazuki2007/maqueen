def on_button_pressed_a():
    global 動作
    動作 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global 動作
    動作 = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

動作 = 0
動作 = 0

def on_forever():
    if 動作 == 0:
        if input.sound_level() > 100:
            maqueen.motor_stop(maqueen.Motors.ALL)
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        elif maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 20:
            if maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 6:
                maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
                maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
                basic.show_leds("""
                    # . . . #
                                        . # . # .
                                        . . # . .
                                        . . . . .
                                        . . . . .
                """)
                maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 50)
            else:
                basic.show_leds("""
                    . . # . .
                                        . . # . .
                                        . . # . .
                                        . . . . .
                                        . . # . .
                """)
                maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
                maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
        else:
            basic.show_leds("""
                # # # # #
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 150)
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    elif 動作 == 1:
        basic.show_leds("""
            # # . # #
                        . . . . .
                        # . # . #
                        . . . . .
                        # # . # #
        """)
        maqueen.motor_stop(maqueen.Motors.ALL)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
basic.forever(on_forever)
