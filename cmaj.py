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
        chord += rotated_scale[int(f.scale_to_chromatic[interval]) -1] + ' '
    return chord

def get_scale_type(key):
    """
    'Parses' the key and gives back a suitable
    chromatic scale
    """
    if 'b' in key:
        return f.scales['chromatic-flat']
    return f.scales['chromatic-sharp']

def scale(key):
    """
    Returns the scale for a given key
    i.e.
        scale('C')
    Returns
        'CDEFGAB'
    """
    scale_to_return = get_notes_from_intervals(*f.formulas['modes']['ionian'], key=key)
    return scale_to_return

def chord(chord):
    """chord('C') -> 'C E G '"""
    chord_type = get_chord_type(chord)
    returned_chord = get_notes_from_intervals(*f.formulas['chords'][chord_type], key=chord[0]) 
    return returned_chord
