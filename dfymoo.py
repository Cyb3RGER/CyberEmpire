import os
import random


class DfymooValue:
    def __init__(self):
        self.n = None
        self.s = None
        self.o = None


class Dfymoo:
    def __init__(self):
        self.i = []
        self.w = ""
        self.h = ""
        self.vals: list[DfymooValue] = []

    def load(self, file_path):
        with open(file_path, mode='r') as f:
            lines = f.read().splitlines()
        self.i = lines[0].split(' ')[1:]
        self.w = lines[1].split(' ')[1]
        self.h = lines[2].split(' ')[1]
        i = 0
        for line in lines[4:]:
            if line.startswith('~'):
                i += 1
                continue
            split = line.split(' ')
            if len(self.vals) == i:
                self.vals.append(DfymooValue())
            self.vals[i].__setattr__(split[0], split[1:] if len(split) > 2 else split[1])

    def write(self, file_path):
        base, name = os.path.split(file_path)
        if not os.path.exists(f'{base}'):
            os.makedirs(f'{base}', exist_ok=True)
        with open(file_path, mode='w') as f:
            f.write(f'i {" ".join(self.i)}\n')
            f.write(f'w {self.w}\n')
            f.write(f'h {self.h}\n')
            f.write(f'~\n')
            for v in self.vals:
                if v.n is not None:
                    f.write(f'n {v.n}\n')
                if v.s is not None:
                    f.write(f's {" ".join(v.s)}\n')
                if v.o is not None:
                    f.write(f'o {" ".join(v.o)}\n')
                f.write(f'~')
                if self.vals.index(v) != len(self.vals) - 1:
                    f.write('\n')

    def get_names(self):
        return [v.n for v in self.vals]
