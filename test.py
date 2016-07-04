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
        tests = [
            [
                'G B D F# ', 
                 cmaj.get_notes_from_intervals('1', '3', '5', '7', key='G')
            ],
            [
                'Bb D F ',
                cmaj.get_notes_from_intervals('1', '3', '5', key='Bb')
            ],
            [
                'C E G B ',
                cmaj.get_notes_from_intervals('1', '3', '5', '7')
            ],
        ]

        self.check_tests(tests)

    def test_chord(self):
        tests = [
            ['C E G ', cmaj.chord('C')],
            ['G B D ', cmaj.chord('G')],
            ['E G B ', cmaj.chord('Em')],
            ['A C# E ', cmaj.chord('A')],
            ['Bb D F ', cmaj.chord('Bb')],
            ['Bb Db F ', cmaj.chord('Bbm')],
            ['F# A C# ', cmaj.chord('F#m')],
            ['A C E G ', cmaj.chord('Am7')],
            ['D F A C ', cmaj.chord('Dm7')],
            ['C Eb G Bb ', cmaj.chord('Cm7')],
        ]
        self.check_tests(tests)


    def check_tests(self, tests):
        for test_case in tests:
            expected = test_case[0]
            actual = test_case[1]
            self.assertEqual(expected, actual)

    def test_strip_noise_from_key_signatures(self):
        tests = [
            ['A', cmaj.strip_noise_from_key_signature('Am7')],
            ['Bb', cmaj.strip_noise_from_key_signature('Bbm7')],
        ]

        self.check_tests(tests)

    def test_get_scale_type(self):

        sharp = [
            'C', 'C#', 'D', 'D#',
            'E', 'F', 'F#', 'G',
            'G#', 'A', 'A#', 'B',
        ]

        flat = [
            'C', 'Db', 'D', 'Eb',
            'E', 'F', 'Gb', 'G',
            'Ab', 'A', 'Bb', 'B',
        ]

        tests = [
            [flat, cmaj.get_scale_type('Bb')],
            [sharp, cmaj.get_scale_type('C')],
            [sharp, cmaj.get_scale_type('C#')],
        ]

        self.check_tests(tests)

    def test_get_chord_type_for_major_chord(self):
        expected = 'major'
        actual = cmaj.get_chord_type('C')
        self.assertEqual(expected, actual)

    def test_get_chord_type_for_minor_chord(self):
        expected = 'minor'
        actual = cmaj.get_chord_type('Cm')
        self.assertEqual(expected, actual)

    def test_scale(self):
        tests = [
            #Minor key
            ['E F# G A B C D ', cmaj.scale('Em')],
            ['Bb C Db Eb F Gb Ab ', cmaj.scale('Bbm')],
            #Flat
            ['Bb C D Eb F G A ', cmaj.scale('Bb')],
            #Natural
            ['G A B C D E F# ', cmaj.scale('G')],
            ['C D E F G A B ', cmaj.scale('C')],
        ]

        self.check_tests(tests)

    #@TODO add test cases for flats
    def test_scale_intervals(self):
        tests = [
            #natural
            ['C D E F G A B ', cmaj.scale_intervals('1 2 3 4 5 6 7')],
            #sharps
            ['C D# E F# G# A B ', cmaj.scale_intervals('1 #2 3 #4 #5 6 7')],
        ]

        self.check_tests(tests)


if __name__ == '__main__':
    unittest.main()
