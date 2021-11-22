# TR-6S Sequencer

## Overview 

Minimal euclidean drum sequencer for Roland TR-6S using vanilla puredata!


## TODO

- implement non-track cc controls 


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

80 OH TUNE
81 OH DECAY
82 OH LEVEL
108 OH CTRL

70 FILL IN TRIG
71 ACCENT
91 REVERB LEVEL
```

## Track Parameter

```

track <name> <chan> <n1> <n2> \
	  <tune> <decay> <level> <ctrl> \ # cc out
	  <hit> <len> <rot> <snd> <tun> <vel> <dur> <dcy> <ctl> <lvl> \ # cc in

for example

track BD 10 35 36 20 23 24 96  0   1   2   3   4   5   6   7   8   9

track $1 $2 $3 $4 $5 $6 $7 $8 $9 $10 $11 $12 $13 $14 $15 $16 $17 $18


So for all the tracks

track BD 10 35 36 20 23 24 96  0   1  2  3  4  5  6  7  8  9
track SD 10 40 38 25 28 29 97  10 11 12 13 14 15 16 17 18 19
track LT 10 41 43 46 47 48 102 20 21 22 23 24 25 26 27 28 29
track HC 10 54 39 58 59 60 106 30 31 32 33 34 35 36 37 18 39
track CH 10 44 42 61 62 63 107 40 41 42 43 44 45 46 47 48 49
track OH 10 58 46 80 81 82 108 50 51 52 53 54 55 56 57 58 59

```

