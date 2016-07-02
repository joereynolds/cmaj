import unittest

import cmaj


class TestCmaj(unittest.TestCase):

    def test_rotate_to_key(self):
        non_rotated = [
            'D', 'D#', 'E', 'F',
            'F#', 'G', 'G#', 'A',
            'A#', 'B', 'C', 'C#'
        ]

        rotated = cmaj.rotate_to_key(non_rotated, 'C')
        expected_rotated = [
            'C', 'C#', 'D', 'D#',
            'E', 'F', 'F#', 'G',
            'G#', 'A', 'A#', 'B'
        ]
        self.assertEqual(rotated, expected_rotated)

    def test_rotate_to_key_with_flats(self):
        non_rotated = [
            'C', 'Db', 'D', 'Eb', 
            'E', 'F', 'Gb', 'G', 
            'Ab', 'A', 'Bb', 'B'
        ]

        rotated = cmaj.rotate_to_key(non_rotated, 'Bb')
        expected_rotated = [
            'Bb', 'B', 'C', 'Db', 
            'D', 'Eb', 'E', 'F', 
            'Gb', 'G', 'Ab', 'A', 
        ]
        self.assertEqual(rotated, expected_rotated)

    def test_get_notes_for_chord(self):
        expected = 'G B D F# '
        actual = cmaj.get_notes_for_chord('1', '3', '5', '7', key='G')
        self.assertEqual(expected, actual)

    def test_get_notes_for_chord_on_flat_key(self):
        expected = 'Bb D F '
        actual = cmaj.get_notes_for_chord('1', '3', '5', key='Bb')
        self.assertEqual(expected, actual)

    def test_get_notes_for_chord_with_default_argument(self):
        expected = 'C E G B '
        actual = cmaj.get_notes_for_chord('1', '3', '5', '7')
        self.assertEqual(expected, actual)

    def test_scale_on_neutral_key(self):
        expected = 'C D E F G A B '
        actual = cmaj.scale('C')
        self.assertEqual(actual, expected)

    def test_get_scale_type_from_input(self):
        expected = 'major'
        actual = cmaj.get_scale_type_from_input('C')
        self.assertEqual(actual, expected)

    def test_get_scale_type_from_input_with_a_minor_key(self):
        expected = 'minor'
        actual = cmaj.get_scale_type_from_input('Cm')
        self.assertEqual(actual, expected)
        
    def test_scale_on_flat_key(self):
        expected = 'Bb C D Eb F G A '
        actual = cmaj.scale('Bb')
        self.assertEqual(actual, expected)

    def test_scale_on_sharp_key(self):
        expected = 'G A B C D E F# '
        actual = cmaj.scale('G')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
