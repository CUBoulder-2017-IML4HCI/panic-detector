radio.onDataPacketReceived(({receivedString}) => {
    serial.writeLine(receivedString)
})
radio.setGroup(8)
