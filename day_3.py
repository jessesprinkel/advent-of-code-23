import numpy as np


class PartNumber:
    def __init__(self) -> None:
        self.valid = False

class Gear:
    def __init__(self) -> None:
        self.part_numbers: list = []


class Character:
    def __init__(self, chr: str, row: int, column: int, type: str, part_number: PartNumber = None, gear: Gear = None) -> None:
        self.character = chr
        self.column = column
        self.row = row
        self.type = type
        self.part_number = part_number
        self.gear = gear

    def __repr__(self) -> str:
        return self.character.__str__()
        

class EngineSchematic:
    def __init__(self, height, width) -> None:
        self.schematic = np.zeros([height, width], dtype=Character)
        self.numbers: list = []

    def update_schema(self, row: int, column: int, character: Character):
        self.schematic[row, column] = character
    
    def validate_numbers(self):
        for i, row in enumerate(self.schematic):
            for i_, chr in enumerate(row):
                if chr.type == 'part':
                    if chr.part_number.valid:
                        continue
                    else:
                        for row, column in self.adjacent_spaces(chr.row, chr.column):
                            if self.valid_position(row=row, column=column) and self.schematic[row, column].type == 'symbol':
                                if self.schematic[row, column].gear:
                                    self.schematic[row, column].gear.part_numbers.append(chr.part_number)
                                chr.part_number.valid = True
            

    def valid_position(self, row, column) -> bool:
        return row < len(self.schematic) and column < len(self.schematic[0])
    
    @staticmethod
    def adjacent_spaces(row, column) -> list:
        return [[row, column - 1], [row, column + 1], [row - 1, column], [row + 1, column],
                [row - 1, column - 1], [row - 1, column + 1], [row + 1, column - 1], [row + 1, column + 1]]
    
    def unique_valid_parts(self) -> list:
        return set([ch.part_number for r in engine_schematic.schematic for ch in r if ch.part_number and ch.part_number.valid])
    
    def add_sum(self) -> int:
        number_list = []
        for part in self.unique_valid_parts():
            part_numbers = []
            for row in self.schematic:
                for ch in row:
                    if ch.part_number is part:
                        part_numbers.append(ch.character)
            number_list.append(''.join(part_numbers))

        return sum([int(n) for n in number_list])

    def sum_gear_ratios(self) -> int:
        gear_ratios = []
        for i, row in enumerate(self.schematic):
            for i_, chr in enumerate(row):
                if chr.gear and len(chr.gear.part_numbers) == 2:
                    ratio_1 = ''.join([c.character for r in engine_schematic.schematic for c in r if c.part_number == chr.gear.part_numbers[0]])
                    ratio_2 = ''.join([c.character for r in engine_schematic.schematic for c in r if c.part_number == chr.gear.part_numbers[1]])
                    gear_ratios.append(int(ratio_1) * int(ratio_2))

        return sum(gear_ratios)


with open('input/day3.txt') as f:
    for i, line in enumerate(f):
        pass
    file_lines = i + 1
    line_length = len(line)

engine_schematic = EngineSchematic(height=file_lines, width=line_length)

with open('input/day3.txt') as f:
    for r, line in enumerate(f):

        number_found = None
        for c, chr in enumerate(line):
            if chr == '\n':
                continue
            if chr.isnumeric():
                part_number = engine_schematic.schematic[r, c - 1].part_number if number_found == c - 1 else PartNumber()
                symbol = Character(chr=chr, column=c, row=r, type='part', part_number=part_number)
                engine_schematic.update_schema(row=r, column=c, character=symbol)
                number_found = c
            elif chr == '*':
                symbol = Character(chr=chr, column=c, row=r, type='symbol', gear=Gear())
                engine_schematic.update_schema(row=r, column=c, character=symbol)
            elif chr != '.':
                symbol = Character(chr=chr, column=c, row=r, type='symbol')
                engine_schematic.update_schema(row=r, column=c, character=symbol)
            else:
                symbol = Character(chr=chr, column=c, row=r, type='period')
                engine_schematic.update_schema(row=r, column=c, character=symbol)

engine_schematic.validate_numbers()

total = engine_schematic.add_sum()

print(f'Part 1: the total sum of all the valid parts is {total}')

gear_ratios = engine_schematic.sum_gear_ratios()

print(f'Part 2: the sum of all gear ratios is {gear_ratios}')
