# nord3p-sequencer (in puredata)

A basic euclidean drum sequencer for the nord 3p drum synt based a very nifty
implementation by [stutter](https://forum.pdpatchrepo.info/topic/5968/euclidean-rhythm-abstraction).

Includes a touchosc template.


## TODO

- [x] add midi (touchosc) controls for euclid and midi params
- [x] add different clock derivations for each channel
- [ ] add modulation


## MIDI Mapping


```
track <name> <channel> 0 1 2 3 4 5


track 1 0  1  2  3  4  5
track 2 6  7  8  9  10 11
track 3 12 13 14 15 16 17
track 4 18 19 20 21 22 23
track 5 24 25 26 27 28 29
track 6 30 31 32 33 34 35

```