import formula as f


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

    #Refactor this when it gets messier
    if '7' in chord:
        if 'm' in chord:
            return 'minor7'
    if 'm' in chord:
        return 'minor'
    return 'major'

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
