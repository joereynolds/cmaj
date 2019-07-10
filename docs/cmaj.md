## --chord

`--chord` returns the individual notes of a chord. Currently the `--chord`
option supports the following:

- Major chords `cmaj --chord C`
- Major 7 chords `cmaj --chord CM7`
- Major 9 chords `cmaj --chord CM9`
- Minor chords `cmaj --chord Cm`
- Minor 7 chords `cmaj --chord Cm7`
- Minor 9 chords `cmaj --chord Cm9`

**Example**

## --freq

`--freq` returns the nth partial for a frequency.

- Getting the 4th partial of 440 `cmaj --freq 440 4`
- Getting the fundamental frequency `cmaj --freq 440 1`

**Example**


## --mtof

`--mtof` returns the frequency of a given MIDI note.

`cmaj --mtof 62`

**Example**


## --mton

`--mton` returns the musical note of a given MIDI note.

`cmaj --mton 62`

**Example**

```
$ cmaj --mton 65
F4

$ cmaj --mton 0
midi note 0 is out of range. Accepted values are between 21 and 108
```


## --scale

`--scale` returns the individual notes that make a specified scale.

- Getting a major scale `cmaj --scale E`
- Getting a minor scale `cmaj --scale Bbm`

**Example**

```
$ cmaj --scale Em
E F# G A B C D 

$ cmaj --scale Bb
Bb C D Eb F G A 
```
