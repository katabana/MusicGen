from miditime.miditime import MIDITime
import random

# TODO: scales as dictionaries?

# scales
scales = {'minor': 'cdefgah', 'major': 'CDEFGAH', 'C': 'CFaG', 'E': 'GCDE',
          'AGH': 'AaGgHh', 'revolution': 'aec', 'weird': 'wCh', 'single': 'E',
          'dominant': 'CFGq', 'default': 'cdefgahCDEFGAH'}

# chord pitch values
chords = {'C': [60, 64, 67], 'D': [62, 66, 69], 'E': [64, 68, 71],
          'F': [65, 69, 72], 'G': [67, 71, 74], 'A': [69, 73, 76],
          'H': [71, 75, 78], 'c': [60, 63, 67], 'd': [62, 65, 69],
          'e': [64, 67, 71], 'f': [65, 68, 72], 'g': [67, 70, 74],
          'a': [69, 72, 76], 'h': [71, 74, 78], 'q': [67, 71, 74, 77]}


def get_velocity(val, beats):
    a = []
    direction = random.randint(-1, 1)
    for i in range(0, beats):
        if direction == 1:
            maximum = int((255 - val) / beats)
            k = random.randint(0, maximum)
            a.append(int(val + k/beats*i))
        else:
            maximum = int(val / beats)
            k = random.randint(0, maximum)
            a.append(int(val - k/beats*i))

    return a


def get_time(beats):
    time = []
    for i in range(0, beats):
        # 2,14 defualt settings for length of sound
        time = time + [i+(random.randint(2, 14))/4.]
    return time


def make_rythm(beats):
    # for each beat choose if should modify and random values to fill one beat
    rythm = []
    for i in range(1, beats+1):
        if random.randint(0, 2) == 2:
            a = random.randint(1, 4)
            for x in range(0, a):
                rythm += [x*4/float(a)]
        else:
            rythm += [1]
    return rythm


def make_chord(notes, scale):
    s = random.choice(scale)
    chord = chords[s]
    while notes - len(chord) > 3:
        chord += make_chord(notes - len(chord), scale)
    while len(chord) < notes:
        k = random.randint(0, len(chord)-1)
        chord.insert(k, chord[k] + (2 * random.randint(-2, 2)))

    return chord


def make_tact(beats, start, scale):
    tact = []
    rythm = make_rythm(beats)
    chord = make_chord(len(rythm), scale)
    velocity = get_velocity(80, len(rythm))  # maybe field in class -> last velocity?
    time = get_time(len(rythm))

    for i, val in enumerate(rythm):
        tact.append([start + rythm[i], chord[i], velocity[i], time[i]])
        start = start + rythm[i]

    # TODO: which one is better?
    rythm = make_rythm(beats)
    # rythm = [1] * beats
    low = [[start+rythm[0], chord[0] - 17, 80, 2], [start + 2*rythm[1], chord[1] - 13, 80, 2],
           [start + 2*rythm[2], chord[0] - 12, 80, 2]]

    tact = tact + low

    return tact


def generate_notes(time, start, option):
    notes = []
    while start < time:
        if option in scales:
            scale = scales[option]
        else:
            scale = scales['default']
        notes = notes + make_tact(4, start, scale)  # generate_chord(start,end,110,140, scale)
        start = start + 6
    return notes
