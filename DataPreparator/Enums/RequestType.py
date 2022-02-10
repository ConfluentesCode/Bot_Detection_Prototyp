import enum


class RequestType(enum.IntEnum):
    TEXT = 0
    WEB = 1
    IMG = 2
    DOC = 3
    AV = 4
    PROG = 5
    COMPRESSED = 6
    MALFORMED = 7
    NOE = 8
