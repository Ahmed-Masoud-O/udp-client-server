class Packet:
    ckSum = None
    length = None
    seqNo = None
    data = None

    def __init__(self, length, seqNo, data):
        self.length = length
        self.seqNo = seqNo
        self.data = data
