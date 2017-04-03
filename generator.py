from miditime.miditime import MIDITime
import musicnotes


def generate_file(filename, time, option, bpm):

    mymidi = MIDITime(bpm, filename)

    # Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
    sounds = musicnotes.Notes(time, 0, option)
    midinotes = sounds.notes

    magicnotes = [
        [0, 61, 127, 3],
        [2, 66, 127, 2],
        [5, 69, 127, 1],
        [6, 68, 127, 2],
        [8, 66, 127, 2],
        [11, 73, 127, 2],
        [13, 71, 127, 4],
        [18, 68, 107, 2],
        [22, 66, 100, 2],
        [25, 69, 127, 1],
        [26, 68, 127, 1],
        [28, 64, 117, 2],
        [31, 66, 100, 2],
        [33, 61, 90, 3],
    ]

    if filename == 'magic.mid':
        mymidi = MIDITime(240, filename)
        mymidi.add_track(magicnotes)
        mymidi.save_midi()
        exit(0)

    # Add a track with those notes
    mymidi.add_track(midinotes)

    # Output the .mid file
    mymidi.save_midi()
