class Ack:
    ckSum = None

    def __init__(self, length, ackNumber):
        self.ackNumber = ackNumber
        self.length = length
