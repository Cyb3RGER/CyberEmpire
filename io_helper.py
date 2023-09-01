import io
from enum import Enum, IntEnum
from typing import IO


class TYPE_SIZE(IntEnum):
    INT8 = 1,
    INT16 = 2,
    INT32 = 4,
    INT64 = 8


def read_bytes(file: IO, count: int) -> bytes:
    return file.read(count)


def write_bytes(file: IO, val: bytes):
    file.write(val)


def read_int8(file: IO, signed: bool = False) -> int:
    return int.from_bytes(read_bytes(file, 1), byteorder="little", signed=signed)


def write_int8(file: IO, val: int, signed: bool = False):
    write_bytes(file, val.to_bytes(length=TYPE_SIZE.INT8, byteorder="little", signed=signed))


def read_int16(file: IO, signed: bool = False) -> int:
    return int.from_bytes(read_bytes(file, TYPE_SIZE.INT16), byteorder="little", signed=signed)


def write_int16(file: IO, val: int, signed: bool = False):
    write_bytes(file, val.to_bytes(length=TYPE_SIZE.INT16, byteorder="little", signed=signed))


def read_int32(file: IO, signed: bool = False) -> int:
    return int.from_bytes(read_bytes(file, TYPE_SIZE.INT32), byteorder="little", signed=signed)


def write_int32(file: IO, val: int, signed: bool = False):
    write_bytes(file, val.to_bytes(length=TYPE_SIZE.INT32, byteorder="little", signed=signed))


def read_int64(file: IO, signed: bool = False) -> int:
    return int.from_bytes(read_bytes(file, TYPE_SIZE.INT64), byteorder="little", signed=signed)


def write_int64(file: IO, val: int, signed: bool = False):
    write_bytes(file, val.to_bytes(length=TYPE_SIZE.INT64, byteorder="little", signed=signed))


def read_string_u8(file: IO) -> str:
    read_result: bytes = bytes()
    temp = file.read(1)
    while temp != b'\0':
        read_result += temp
        temp = file.read(1)
    return read_result.decode('utf_8')


def write_string_u8(file: IO, val: str):
    write_bytes(file, val.encode('utf_8') + b'\0')


def read_string_u16(file: IO) -> str:
    read_result: bytes = bytes()
    temp = file.read(2)
    while temp != b'\0\0':
        read_result += temp
        temp = file.read(2)
    return read_result.decode('utf_16_le')


def write_string_u16(file: IO, val: str):
    write_bytes(file, val.encode('utf_16_le') + b'\0\0')
