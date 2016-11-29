class Ack:

    ckSum = None
    length = None
    ackNumber = None

    def __init__(self, length, ackNumber):
        self.ackNumber = ackNumber
        self.length = length
