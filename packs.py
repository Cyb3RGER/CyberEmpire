import os
from typing import IO

from io_helper import read_int32, read_int64, read_string_u8, read_string_u16, write_int32, write_int64, \
    write_string_u8, write_string_u16, read_int16, write_int16, TYPE_SIZE


class PackDefData:
    def __init__(self, file_path: str):
        self.count: int = 0
        self.pack_defs: list[PackDef] = []
        self.load(file_path)

    def load(self, file_path: str):
        with open(f'{file_path}/main/packdefdata_E.bin', mode='rb') as f:
            self.count = read_int64(f)
            for i in range(0, self.count):
                self.pack_defs.append(PackDef(f))
            for i in range(0, self.count):
                self.pack_defs[i].load_string(f)

    def write(self, file_path: str):
        if not os.path.exists(f'{file_path}/main'):
            os.mkdir(f'{file_path}/main')
        with open(f'{file_path}/main/packdefdata_E.bin', mode='wb') as f:
            write_int64(f, self.count)
            for i in range(0, self.count):
                self.pack_defs[i].write(f)
            for i in range(0, self.count):
                self.pack_defs[i].write_string(f)


class PackDef:
    def __init__(self, f: IO):
        self.id_: int = 0
        self.series_id: int = 0
        self.price: int = 0
        self.unknown: int = 0
        self.id_name_ptr: int = 0
        self.name_ptr: int = 0
        self.unknown_str_ptr: int = 0
        self.id_name: str = ""
        self.name: str = ""
        self.unknown_str: str = ""
        self.load(f)

    def load(self, f: IO):
        self.id_ = read_int32(f)
        self.series_id = read_int32(f)
        self.price = read_int32(f)
        self.unknown = read_int32(f)
        self.id_name_ptr = read_int64(f)
        self.name_ptr = read_int64(f)
        self.unknown_str_ptr = read_int64(f)

    def load_string(self, f: IO):
        f.seek(self.id_name_ptr)
        self.id_name = read_string_u8(f)
        f.seek(self.name_ptr)
        self.name = read_string_u16(f)
        f.seek(self.unknown_str_ptr)
        self.unknown_str = read_string_u8(f)

    def write(self, f: IO):
        write_int32(f, self.id_)
        write_int32(f, self.series_id)
        write_int32(f, self.price)
        write_int32(f, self.unknown)
        write_int64(f, self.id_name_ptr)
        write_int64(f, self.name_ptr)
        write_int64(f, self.unknown_str_ptr)

    def write_string(self, f: IO):
        f.seek(self.id_name_ptr)
        write_string_u8(f, self.id_name)
        f.seek(self.name_ptr)
        write_string_u16(f, self.name)
        f.seek(self.unknown_str_ptr)
        write_string_u8(f, self.unknown_str)


class BattlePack:
    def __init__(self, name):
        self.name: str = name
        self.pack_count: int = 0
        self.pack_ptrs: list[int] = []
        self.packs: list[BattlePackCards] = []

    def load(self, file_path):
        with open(file_path, mode='rb') as f:
            self.pack_count = read_int64(f)
            self.pack_ptrs = []
            for i in range(0, self.pack_count):
                self.pack_ptrs.append(read_int64(f))
            self.packs = []
            for i in range(0, self.pack_count):
                self.packs.append(BattlePackCards())
                # f.seek(self.pack_ptrs[i]) # do we want this?
                self.packs[i].load(f)

    def get_size(self):
        return TYPE_SIZE.INT64 + self.pack_count * TYPE_SIZE.INT64

    def fix_pointers(self):
        pos = self.get_size()
        for i in range(0, self.pack_count):
            self.pack_ptrs = pos
            pos += self.packs[i].get_size()

    def write(self, file_path):
        self.fix_pointers()
        with open(file_path, mode='wb') as f:
            write_int64(f, self.pack_count)
            for i in range(0, self.pack_count):
                write_int64(f, self.pack_count)
            for i in range(0, self.pack_count):
                self.packs[i].write()


class BattlePackCards:
    def __init__(self):
        self.count: int = 0
        self.cards: list[int] = []

    def get_size(self):
        return TYPE_SIZE.INT16 + self.count * TYPE_SIZE.INT16

    def load(self, f):
        self.count = read_int16(f)
        self.cards = []
        for i in range(0, self.count):
            self.cards.append(read_int16(f))

    def write(self, f):
        write_int16(f, self.count)
        for i in range(self.count):
            write_int16(f, self.cards[i])


class Pack:
    def __init__(self, name):
        self.name: str = name
        self.common_count: int = 0
        self.rare_count: int = 0
        self.common_ids: list[int] = []
        self.rare_ids: list[int] = []

    def load(self, file_path):
        with open(file_path, mode='rb') as f:
            self.common_count = read_int16(f)
            self.rare_count = read_int16(f)
            self.common_ids = []
            for i in range(0, self.common_count):
                self.common_ids.append(read_int16(f))
            self.rare_ids = []
            for i in range(0, self.rare_count):
                self.rare_ids.append(read_int16(f))

    def write(self, file_path):
        with open(file_path, mode='wb') as f:
            write_int16(f, self.common_count)
            write_int16(f, self.rare_count)
            for i in range(0, self.common_count):
                write_int16(f, self.common_ids[i])
            for i in range(0, self.rare_count):
                write_int16(f, self.rare_ids[i])
