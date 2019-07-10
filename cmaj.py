import formula as f
import math


def rotate_to_key(notes_list, key):
    """
    Rotates an array so that @key is the starting element
    i.e.
        rotate_to_key(['C', 'C#', 'D, 'D#' ...], D)
    returns
        ['D, 'D#', E, F ...]
    """
    rotated = list(notes_list) #Create a copy

    key = strip_noise_from_key_signature(key)

    while rotated[0] != key:
        rotated.insert(0, rotated.pop())
    return rotated

def strip_noise_from_key_signature(key):
    """Removes any unneccessary characters (7,9,11,m,M etc...)"""
    #Change this to a map or something
    key = key.replace('9', '')
    key = key.replace('7', '')
    key = key.replace('5', '')
    key = key.replace('m', '')
    key = key.replace('M', '')
    return key

def get_notes_from_intervals(*intervals, key='C'):
    _scale = get_scale_type(key)

    rotated_scale = rotate_to_key(_scale, key)

    notes = ''
    for interval in intervals:
        notes += rotated_scale[int(f.scale_to_chromatic[interval]) -1] + ' '

    return notes

def get_scale_type(key):
    """
    'Parses' the key and gives back a suitable
    chromatic scale
    """
    key = key.replace('7', '')
    key = key.replace('9', '')
    if 'b' in key or key in f.scales['flat']:
        return f.scales['chromatic-flat']

    return f.scales['chromatic-sharp']

def scale(key):
    """
    Returns the scale for a given key
    i.e.
        scale('C')
    Returns
        'C D E F G A B '
    """

    mode = 'ionian'
    if 'm' in key:
        mode = 'aeolian'
    
    scale_to_return = get_notes_from_intervals(*f.formulas['modes'][mode], key=key)
    return scale_to_return

def scale_intervals(intervals):
    scale_to_return = get_notes_from_intervals(*intervals.split(), key='C')
    return scale_to_return


def get_chord_type(chord):
    """'Parses' input for a chord and returns the type of chord from it"""

    cleaned_chord = chord[1:]
    cleaned_chord = cleaned_chord.replace('b', '')
    cleaned_chord = cleaned_chord.replace('#', '')

    mapping = {
        '7': 'seven',
        '9': 'nine',
        'm7': 'minor7',
        'm9': 'minor9',
        'm': 'minor',
        'M7': 'major7',
        'M9': 'major9',
        '': 'major',
    }

    return mapping[cleaned_chord]

def chord(chord):
    """chord('C') -> 'C E G '"""
    chord_type = get_chord_type(chord)

    returned_chord = get_notes_from_intervals(
        *f.formulas['chords'][chord_type], 
        key=chord.split()[0]
    ) 

    return returned_chord

def partial(fundamental, n):
    return fundamental * n

def midi_to_frequency(midi_note):
    frequency = math.pow(2, (midi_note - 69) / 12) * 440
    return round(frequency, 2)

def midi_to_note(midi_note):
    midi_to_note_mapping = {
        21: 'A0',
        22: 'A#0',
        23: 'B0',
        24: 'C1',
        25: 'C#1',
        26: 'D1',
        27: 'D#1',
        28: 'E1',
        29: 'F1',
        30: 'F#1',
        31: 'G1',
        32: 'G#1',
        33: 'A1',
        34: 'A#1',
        35: 'B1',
        36: 'C2',
        37: 'C#2',
        38: 'D2',
        39: 'D#2',
        40: 'E2',
        41: 'F2',
        42: 'F#2',
        43: 'G2',
        44: 'G#2',
        45: 'A2',
        46: 'A#2',
        47: 'B2',
        48: 'C3',
        49: 'C#3',
        50: 'D3',
        51: 'D#3',
        52: 'E3',
        53: 'F3',
        54: 'F#3',
        55: 'G3',
        56: 'G#3',
        57: 'A3',
        58: 'A#3',
        59: 'B3',
        60: 'C4',
        61: 'C#4',
        62: 'D4',
        63: 'D#4',
        64: 'E4',
        65: 'F4',
        66: 'F#4',
        67: 'G4',
        68: 'G#4',
        69: 'A4',
        70: 'A#4',
        71: 'B4',
        72: 'C5',
        73: 'C#5',
        74: 'D5',
        75: 'D#5',
        76: 'E5',
        77: 'F5',
        78: 'F#5',
        79: 'G5',
        80: 'G#5',
        81: 'A5',
        82: 'A#5',
        83: 'B5',
        84: 'C6',
        85: 'C#6',
        86: 'D6',
        87: 'D#6',
        88: 'E6',
        89: 'F6',
        90: 'F#6',
        91: 'G6',
        92: 'G#6',
        93: 'A6',
        94: 'A#6',
        95: 'B6',
        96: 'C7',
        97: 'C#7',
        98: 'D7',
        99: 'D#7',
        100: 'E7',
        101: 'F7',
        102: 'F#7',
        103: 'G7',
        104: 'G#7',
        105: 'A7',
        106: 'A#7',
        107: 'B7',
        108: 'C8',
    }

    try:
        return midi_to_note_mapping[midi_note]
    except:
        # Thrown an exception here instead and catch it in main
        return 'midi note ' + str(midi_note) + ' is out of range. Accepted values are between 21 and 108'
