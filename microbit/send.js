let Pulse = 0
let Moisture = 0
let Temp = 0
let Acce_x = 0
let Acce_y = 0
let Acce_z = 0
let classification = " "
let roll_x = 0
basic.forever(() => {
    Pulse = pins.analogReadPin(AnalogPin.P0)
    roll_x = input.rotation(Rotation.Roll)
    Temp = input.temperature()
    Acce_x = input.acceleration(Dimension.X)
    Acce_y = input.acceleration(Dimension.Y)
    Acce_z = input.acceleration(Dimension.Z)
    radio.sendString(Pulse.toString() + "," + roll_x.toString() + "," + Temp.toString() + "," + Acce_x.toString()
        + "," + Acce_y.toString() + "," + Acce_z.toString() + ",")
})
radio.setGroup(8)
