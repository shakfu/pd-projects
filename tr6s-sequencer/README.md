# TR-6S Sequencer

## Overview 

Minimal euclidean drum sequencer for Roland TR-6S using vanilla puredata!


## TODO

- [ ] Levels is not working !


## MIDI Map

### User Interface CC

All for MIDI channel 10

```
track 	cc 		parameter
----	-- 		---------
BD		0 		Hits
BD 		1 		Length
BD 		2 		Rotation
BD 		3 		Sound selection
BD 		4 		Tune
BD 		5 		Velocity
BD 		6 		Duration
BD 		7 		Decay
BD 		8 		Ctrl 
BD 		9 		Level
	
SD		10 		Hits
SD 		11 		Length
SD 		12 		Rotation
SD 		13 		Sound selection
SD 		14 		Tune
SD 		15 		Velocity
SD 		16 		Duration
SD 		17 		Decay
SD 		18 		Ctrl 
SD 		19 		Level
	
LT		20 		Hits
LT 		21 		Length
LT 		22 		Rotation
LT 		23 		Sound selection
LT 		24 		Tune
LT 		25 		Velocity
LT 		26 		Duration
LT 		27 		Decay
LT 		28 		Ctrl 
LT 		29 		Level
	
HC		30 		Hits
HC 		31 		Length
HC 		32 		Rotation
HC 		33 		Sound selection
HC 		34 		Tune
HC 		35 		Velocity
HC 		36 		Duration
HC 		37 		Decay
HC 		38 		Ctrl 
HC 		39 		Level

CH		40 		Hits
CH 		41 		Length
CH 		42 		Rotation
CH 		43 		Sound selection
CH 		44 		Tune
CH 		45 		Velocity
CH 		46 		Duration
CH 		47 		Decay
CH 		48 		Ctrl 
CH 		49 		Level
	
OH		50 		Hits
OH 		51 		Length
OH 		52 		Rotation
OH 		53 		Sound selection
OH 		54 		Tune
OH 		55 		Velocity
OH 		56 		Duration
OH 		57 		Decay
OH 		58 		Ctrl 
OH 		59 		Level

```


### Drums
```
MIDI Chanel 10

DRUM	NOTE-Rx	NOTE-Tx	
----	------	-------
BD 		35		36
SD 		40		38
LT 		41		43
HC 		54		39
CH 		44		42
OH 		58		46


```

### Control Change (CC)

```
CC PARAM
-- -----
9 SHUFFLE
12 EXTERNAL IN LEVEL
14 AUTO FILL IN [ON]
15 MASTER FX [ON]
16 DELAY LEVEL
17 DELAY TIME
18 DELAY FEEDBACK
19 MASTER FX CTRL

20 BD TUNE
23 BD DECAY
24 BD LEVEL
96 BD CTRL

25 SD TUNE
28 SD DECAY
29 SD LEVEL
97 SD CTRL

46 LT TUNE
47 LT DECAY
48 LT LEVEL
102 LT CTRL

58 HC TUNE
59 HC DECAY
60 HC LEVEL
106 HC CTRL

61 CH TUNE
62 CH DECAY
63 CH LEVEL
107 CH CTRL

70 AUTO FILL IN [MANUAL TRIG] ACCENT
71 ACCENT

80 OH TUNE
81 OH DECAY
82 OH LEVEL
108 OH CTRL

91 REVERB LEVEL
```

## Track Parameter

```
track <name> <n1> <n2> <cc-tune> <cc-decay> <cc-level> <cc-ctrl>

for example

track BD 35 36 20 23 24 96

track $1 $2 $3 $4 $5 $6 $7


So for all the tracks

track BD 35 36 20 23 24 96
track SD 40 38 25 28 29 97
track LT 41 43 46 47 48 102
track HC 54 39 58 59 60 106
track CH 44 42 61 62 63 107
track OH 58 46 80 81 82 108

```


## Problems

### `ctlin` does not accept $-substitution!

Which creates an unholy mess in `tracks.pd`

Seems this issue is widespread:

- see: https://lists.puredata.info/pipermail/pd-list/2009-03/068698.html
	- possible solutions: https://lists.puredata.info/pipermail/pd-list/2009-03/068702.html


