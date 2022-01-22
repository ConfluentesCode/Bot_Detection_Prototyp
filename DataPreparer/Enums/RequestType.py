import enum


class RequestType(enum.IntEnum):
    TEXT = 1
    WEB = 2
    IMG = 3
    DOC = 4
    AV = 5
    PROG = 6
    COMPRESSED = 7
    MALFORMED = 8
    NOE = 9
