import random

# chord pitch values
chords = {'C': [60, 64, 67], 'D': [62, 66, 69], 'E': [64, 68, 71],
          'F': [65, 69, 72], 'G': [67, 71, 74], 'A': [69, 73, 76],
          'H': [71, 75, 78], 'c': [60, 63, 67], 'd': [62, 65, 69],
          'e': [64, 67, 71], 'f': [65, 68, 72], 'g': [67, 70, 74],
          'a': [69, 72, 76], 'h': [71, 74, 78], 'q': [67, 71, 74, 77]}


# makes pitch values from randomly choosen chord from scale
def make_chord(notes, scale):
    s = random.choice(scale)
    chord = chords[s]
    while notes - len(chord) > 3:
        chord += make_chord(notes - len(chord), scale)
    while len(chord) < notes:
        k = random.randint(0, len(chord) - 1)
        chord.insert(k, chord[k] + (2 * random.randint(-2, 2)))

    return chord


# makes rythm values for beats number
def make_rythm(beats):
    # for each beat choose whether should modify and get random values to fill one beat
    rythm = []
    for i in range(1, beats + 1):
        if random.randint(0, 2) == 2:
            a = random.randint(1, 4)
            for x in range(0, a):
                rythm += [x * 4 / float(a)]
        else:
            rythm += [1]
    return rythm


# makes velocity values from value for beats number
def make_velocity(val, beats):
    a = []
    direction = random.randint(-1, 1)
    for i in range(0, beats):
        if direction == 1:
            maximum = int((255 - val) / beats)
            k = random.randint(0, maximum)
            a.append(int(val + k / beats * i))
        else:
            maximum = int(val / beats)
            k = random.randint(0, maximum)
            a.append(int(val - k / beats * i))

    return a


# makes time values for beats number
def get_time(beats):
    time = []
    for i in range(0, beats):
        # 2,14 defualt settings for length of sound
        time.append(i + (random.randint(2, 14)) / 4.)
    return time


class Tact:

    def __init__(self, beats, start, scale, last_velocity):
        self.rythm = make_rythm(beats)
        self.notes = len(self.rythm)
        self.chord = make_chord(self.notes, scale)
        self.velocity = make_velocity(last_velocity, self.notes)
        self.time = get_time(self.notes)
        self.l_rythm = make_rythm(beats)
        self.low_chord = [[start + self.l_rythm[0], self.chord[0] - 17, 80, 2],
                          [start + 2 * self.l_rythm[1], self.chord[1] - 13, 80, 2],
                          [start + 2 * self.l_rythm[2], self.chord[0] - 12, 80, 2]]


def make_tact(beats, start, scale, last_velocity):
    parts = Tact(beats, start, scale, last_velocity)
    tact = []

    for i, val in enumerate(parts.rythm):
        tact.append([start + parts.rythm[i], parts.chord[i], parts.velocity[i], parts.time[i]])
        start = start + parts.rythm[i]

    return tact + parts.low_chord
