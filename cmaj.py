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

    if 'm' in key:
        key = key[:-1]

    while rotated[0] != key:
        rotated.insert(0, rotated.pop())
    return rotated

def get_notes_from_intervals(*intervals, key='C'):
    """

    """

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
    if 'b' in key:
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
