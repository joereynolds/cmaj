Note that in the majority of cases,
commands can be added to with a comma (,)

### Get the notes of a chord
Input:
    cmajor --chord=C
Output:
    C E G

Input:
    cmajor --chord=C,Ebm
Output:
    C E G
    Eb Gb Bb

### Get the chord from notes
Input:
    cmajor --make-chord=C,E,G,B
Output:
    C major 7

### Get the notes of a scale
Input:
    cmajor --scale=Em
Output:
    E F# G A B C D

Also works with intervals.
Note that we specified a root key.
If unspecified, it defaults to C
Input:
    cmajor --scale=C:1,2,3,6
Output:
    C D E A

Input:
    cmajor --scale=1,b2,4,5
Output:
    C Db F G

### Get the scale from notes
Input:
    cmajor --make-scale=A,C,D,E,G
Output:
    A pentatonic

### Get a note from a frequency
Input:
    cmajor --hz=440
Output:
    A

Can specify a range of frequencies
Input:
    cmajor --hz=440,500,466
Output:
    A B(+7 cents, frequency=493.88) A#/Bb

### Get a frequency from a note
Note that you must specify the octave.
How else would it know what to do?
Input:
    cmajor --note=A4
Output:
    440hz

### Get common tones between two things

Returns the common tones between N things.
Things in this case can be, a chord, scale, or list of intervals.

Note sure how to differentiate from scales and chords at the moment
so here are some (bad) examples
#### Scale example

Input:
    cmajor --common=Em,Cm
Output:
    C D G

#### Chord example
Input:
    cmajor --common=G,Em
Output:
    G B

#### Interval example
Input:
    cmajor --common=[A,B,C],[C,D,E]
Output:
    C

### Get the modes of a scale

Input:
    cmajor --scale-mode=Em
Output:
    Ionian      G
    Dorian      A
    Phygian     B
    Lydian      C
    Mixolydian  D
    Aeolian     E
    Locrian     F#

### Get the mode of a scale
Input:
    cmajor --scale-mode=Em:locrian
Output:
    F# Locrian

### Get the scale of a mode
Input:
    cmajor --mode-scales=E-locrian
Output:
    Ionian      F
    Dorian      G
    Phrygian    A
    Lydian      Bb
    Mixolydian  C
    Aeolian     D
    Locrian     E

### Get the interval between N notes

Input:
    cmajor --interval=C,A,G
Output
    M6, P5

Input:
    cmajor --interval=C,Ab
Output
    m6

Input:
    cmajor --interval=C
Output
    Unison
