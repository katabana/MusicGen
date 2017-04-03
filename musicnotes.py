import parts

# scales
scales = {'minor': 'cdefgah', 'major': 'CDEFGAH', 'C': 'CFaG', 'E': 'GCDE',
          'AGH': 'AaGgHh', 'revolution': 'aec', 'weird': 'wCh', 'single': 'E',
          'dominant': 'CFGq', 'default': 'cdefgahCDEFGAH'}


class Notes:

    last_velocity = 80

    def __init__(self, time, start, option):
        self.notes = []

        if len(self.notes) > 0:
            self.last_velocity = self.notes[len(self.notes) - 1][2]
        while start < time:
            if option in scales:
                scale = scales[option]
            else:
                scale = scales['default']
            part = parts.make_tact(4, start, scale, self.last_velocity)
            self.notes = self.notes + part  # generate_chord(start,end,110,140, scale)
            start = start + 6