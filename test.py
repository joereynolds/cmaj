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

    def test_get_notes_for_chord(self):
        expected = 'GBDF#'
        actual = cmaj.get_notes_for_chord('1', '3', '5', '7', key='G')
        self.assertEqual(expected, actual)

    def test_get_notes_for_chord_with_default_argument(self):
        expected = 'CEGB'
        actual = cmaj.get_notes_for_chord('1', '3', '5', '7')
        self.assertEqual(expected, actual)

    @unittest.skip('Function not implemented')
    def test_scale_on_neutral_key(self):
        actual = cmaj.scale('C')
        expected = 'CDEFGAB'
        self.assertEqual(actual, expected)

    @unittest.skip('Function not implemented')
    def test_scale_on_flat_key(self):
        pass

    @unittest.skip('Function not implemented')
    def test_scale_on_sharp_key(self):
        pass



if __name__ == '__main__':
    unittest.main()
