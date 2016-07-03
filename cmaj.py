scale_to_chromatic = {
    '1':  '1',
    'b2': '2',
    '2':  '3',
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
        'major': ['1', '3', '5'],
        'minor': ['1', 'b3', '5']
    }
}

def rotate_to_key(notes_list, key):
    """
    Rotates an array so that @key is the starting element
    i.e.
        rotate_to_key(['C', 'C#', 'D, 'D#' ...], D)
    returns
        ['D, 'D#', E, F ...]
    """
    rotated = list(notes_list) #Create a copy

    while rotated[0] != key:
        rotated.insert(0, rotated.pop())
    return rotated

def get_chord_type(chord):
    """'Parses' input for a chord and returns the type of chord from it"""
    if len(chord) == 1:
        return 'major'
    if 'm' in chord:
        return 'minor'

def get_notes_from_intervals(*intervals, key='C'):

    _scale = get_scale_type(key)

    rotated_scale = rotate_to_key(_scale, key)
    chord = ''

    for interval in intervals:
        chord += rotated_scale[int(scale_to_chromatic[interval]) -1] + ' '
    return chord

def get_scale_type(key):
    """
    'Parses' the key and gives back a suitable
    chromatic scale
    """
    if 'b' in key:
        return scales['chromatic-flat']
    return scales['chromatic-sharp']

def scale(key):
    """
    Returns the scale for a given key
    i.e.
        scale('C')
    Returns
        'CDEFGAB'
    """
    scale_to_return = get_notes_from_intervals(*formulas['modes']['ionian'], key=key)
    return scale_to_return

def chord(chord):
    """chord('C') -> 'C E G '"""
    chord_type = get_chord_type(chord)
    returned_chord = get_notes_from_intervals(*formulas['chords'][chord_type])
    return returned_chord
