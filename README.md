# cmaj

Music theory from the command line.

## Examples

### Scales

View major/minor, sharp/flat scales

`cmaj --scale=Em`

`E F# G A B C D`

`cmaj --scale=Bbm`

`Bb C Db Eb F Gb Ab`

`cmaj --scale=C`

`C D E F G A B `

### Chords

View a chord (minor, major, and 7/9 variants). 

`cmaj --chord=C`

`C E G`

`cmaj --chord=Em`

`E G B`

`cmaj --chord=Em9`

`E G B D F#`

`cmaj --chord=DM9`

`D F# A C# E`

### Partials

Get the nth partial of a frequency

`cmaj --freq 440 3`

`1320`
