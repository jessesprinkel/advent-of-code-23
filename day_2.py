from dataclasses import dataclass, field
from collections import defaultdict

# Part 1 and 2

VALID_DRAW = {
    'red': 12,
    'green': 13,
    'blue': 14
}

@dataclass
class Draw:
    red: int = 0
    green: int = 0
    blue: int = 0

    @property
    def valid_draw(self) -> bool:
        return self.red <= VALID_DRAW['red'] and self.green <= VALID_DRAW['green'] and self.blue <= VALID_DRAW['blue']

@dataclass
class Game:
    draws: list = field(default_factory=list) 
    id: int = 0

    @property
    def valid_game(self) -> bool:
        return all(d.valid_draw for d in self.draws)
    
    @property
    def lowest_power_set(self) -> int:
        lowest_red = max(self.draws, key=lambda x: x.red).red
        lowest_green = max(self.draws, key=lambda x: x.green).green
        lowest_blue = max(self.draws, key=lambda x: x.blue).blue
        return lowest_red * lowest_green * lowest_blue
        

games = []

with open('input/day2.txt') as f:

    for line in f.readlines():
        game_id = int(line.split(':')[0].split()[1])
        game = Game(id=game_id)
        sets = line.split(':')[1].split(';')
        for set in sets:
            color_dict = defaultdict(int)
            for color in set.split(','):
                color_dict[color.split()[1]] += int(color.split()[0])
            draw = Draw(**color_dict)
            game.draws.append(draw)

        games.append(game)


print(f"Part 1: The sum of valid game id's is : {sum(g.id for g in games if g.valid_game)}")

print(f"Part 2: The sum of the power sets of valid games is : {sum(g.lowest_power_set for g in games)}")