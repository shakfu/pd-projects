# Vermona DRM1-mk3 Sequencer

## Overview 

Minimal euclidean drum sequencer for Roland TR-8S using vanilla puredata!


## MIDI Map

## Track Parameter

```
track <name> <chan> <n1> <n2> \
	  <hit> <len> <rot> <snd> <vel> <dur> \ # cc in

for example

track BD 10 35 36 0  1  2  3  4  5

track $1 $2 $3 $4 $5 $6 $7 $8 $9 $10

So for all the tracks

track KI 10 36 XX 0  1  2  3  4  5
track D1 10 48 38 6  7  8  9  10 11 
track D2 10 41 43 12 13 14 15 16 17 
track MU 10 58 47 18 19 20 21 22 23 
track SD 10 40 50 24 25 26 27 28 29 
track H1 10 49 51 30 31 32 33 34 35 
track H2 10 42 44 36 37 38 39 40 41
track HC 10 39 42 42 43 44 45 46 47
```


## Problems



