scale_to_chromatic = {
    '1':  '1',
    'b2': '2',
    '2':  '3',
    '#2': '4',
    'b3': '4',
    '3':  '5',
    '4':  '6',
    '#4': '7',
    'b5': '7',
    '5':  '8',
    '#5': '9',
    'b6': '9',
    '6':  '10',
    'b7': '11',
    '7':  '12',
}

chromatic_to_scale = {
    '1': '1',
    '2': 'b2',
    '3': '2',
    '4': 'b3',
    '5': '3',
    '6': '4',
    '7': 'b5',
    '8': '5',
    '9': 'b6',
    '10': '6',
    '11': 'b7',
    '12': '7',
}

scales = {
    'chromatic-sharp': [
        'C', 'C#', 'D', 'D#',
        'E', 'F', 'F#', 'G',
        'G#', 'A', 'A#', 'B',
    ],
    'chromatic-flat': [
        'C', 'Db', 'D', 'Eb',
        'E', 'F', 'Gb', 'G',
        'Ab', 'A', 'Bb', 'B'
    ],

    #list of scales that use flats instead of sharps
    # that aren't already covered by having a 'b' in their name
    'flat': ['Cm', 'Dm', 'Gm', 'Fm', 'F'],
}

formulas = {
    'modes': {
        'ionian': ['1', '2', '3', '4', '5', '6', '7'],
        'dorian': ['1', '2', 'b3', '4', '5', '6', 'b7'],
        'phrygian': ['1', 'b2', 'b3', '4', '5', 'b6', 'b7'],
        'lydian': ['1', '2', '3', '#4', '5', '6', '7'],
        'mixolydian': ['1', '2', '3', '4', '5', '6', 'b7'],
        'aeolian': ['1', '2', 'b3', '4', '5', 'b6', 'b7'],
        'locrian': ['1', 'b2', 'b3', '4', 'b5', 'b6', 'b7'],
    },
    'chords': {

        # Major
        'major': ['1', '3', '5'],
        'major7':['1', '3', '5', '7'],
        'major9':['1', '3', '5', '7', '2'],

        # Minor
        'minor': ['1', 'b3', '5'],
        'minor7':['1', 'b3', '5', 'b7'],
        'minor9':['1', 'b3', '5', 'b7', '2'],

        # Dominant
        'seven': ['1', '3', '5', 'b7'],
    }
}
