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

    def test_get_notes_from_intervals(self):
        expected = 'G B D F# '
        actual = cmaj.get_notes_from_intervals('1', '3', '5', '7', key='G')
        self.assertEqual(expected, actual)

    def test_get_notes_from_intervals(self):
        expected = 'Bb D F '
        actual = cmaj.get_notes_from_intervals('1', '3', '5', key='Bb')
        self.assertEqual(expected, actual)

    def test_get_notes_from_intervals_with_default_argument(self):
        expected = 'C E G B '
        actual = cmaj.get_notes_from_intervals('1', '3', '5', '7')
        self.assertEqual(expected, actual)

    def test_scale_on_neutral_key(self):
        expected = 'C D E F G A B '
        actual = cmaj.scale('C')
        self.assertEqual(actual, expected)


    #@TODO refactor tests to be like this shining example
    def test_chord(self):
        tests = [
            ['C E G ', cmaj.chord('C')],
            ['G B D ', cmaj.chord('G')],
            ['A C# E ', cmaj.chord('A')]
        ]

        for test_case in tests:
            expected = test_case[0]
            actual = test_case[1]
            self.assertEqual(expected, actual)

    def test_get_chord_type_for_major_chord(self):
        expected = 'major'
        actual = cmaj.get_chord_type('C')
        self.assertEqual(expected, actual)

    def test_get_chord_type_for_minor_chord(self):
        expected = 'minor'
        actual = cmaj.get_chord_type('Cm')
        self.assertEqual(expected, actual)

    @unittest.skip('problem')
    def test_scale_on_minor_key(self):
        expected = 'E F# G A B C D '
        actual = cmaj.scale('Em')
        self.assertEqual(expected, actual)

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
