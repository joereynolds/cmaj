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

__scale = ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#']

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

def get_notes_for_chord(*notes, key='C'):
    rotated_scale = rotate_to_key(__scale, key)
    chord = ''

    for note in notes:
        chord += rotated_scale[int(scale_to_chromatic[note]) -1]
    return chord

def scale(key):
    """
    Returns the scale for a given key
    i.e.
        scale('C')
    Returns
        'CDEFGAB'
    """
    pass

