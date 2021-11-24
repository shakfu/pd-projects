# TR-8S Sequencer

## Overview 

Minimal euclidean drum sequencer for Roland TR-8S using vanilla puredata!


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
	
MT		30 		Hits
MT 		31 		Length
MT 		32 		Rotation
MT 		33 		Sound selection
MT 		34 		Tune
MT 		35 		Velocity
MT 		36 		Duration
MT 		37 		Decay
MT 		38 		Ctrl 
MT 		39 		Level
	
HT		40 		Hits
HT 		41 		Length
HT 		42 		Rotation
HT 		43 		Sound selection
HT 		44 		Tune
HT 		45 		Velocity
HT 		46 		Duration
HT 		47 		Decay
HT 		48 		Ctrl 
HT 		49 		Level
	
RS		50 		Hits
RS 		51 		Length
RS 		52 		Rotation
RS 		53 		Sound selection
RS 		54 		Tune
RS 		55 		Velocity
RS 		56 		Duration
RS 		57 		Decay
RS 		58 		Ctrl 
RS 		59 		Level
	
HC		60 		Hits
HC 		61 		Length
HC 		62 		Rotation
HC 		63 		Sound selection
HC 		64 		Tune
HC 		65 		Velocity
HC 		66 		Duration
HC 		67 		Decay
HC 		68 		Ctrl 
HC 		69 		Level
	
CH		70 		Hits
CH 		71 		Length
CH 		72 		Rotation
CH 		73 		Sound selection
CH 		74 		Tune
CH 		75 		Velocity
CH 		76 		Duration
CH 		77 		Decay
CH 		78 		Ctrl 
CH 		79 		Level
	
OH		80 		Hits
OH 		81 		Length
OH 		82 		Rotation
OH 		83 		Sound selection
OH 		84 		Tune
OH 		85 		Velocity
OH 		86 		Duration
OH 		87 		Decay
OH 		88 		Ctrl 
OH 		89 		Level
	
CC		90 		Hits
CC 		91 		Length
CC 		92 		Rotation
CC 		93 		Sound selection
CC 		94 		Tune
CC 		95 		Velocity
CC 		96 		Duration
CC 		97 		Decay
CC 		98 		Ctrl 
CC 		99 		Level

RC		100 	Hits
RC 		101 	Length
RC 		102 	Rotation
RC 		103 	Sound selection
RC 		104 	Tune
RC 		105 	Velocity
RC 		106 	Duration
RC 		107 	Decay
RC 		108 	Ctrl 
RC 		109 	Level
```


### Drums
```
MIDI Chanel 10

DRUM	NOTE-Rx	NOTE-Tx	
----	------	-------
BD 		35		36
SD 		40		38
LT 		41		43
MT 		45		47
HT 		48		50
RS 		56		37
HC 		54		39
CH 		44		42
OH 		58		46
CC 		61		49
RC 		63		51
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

49 MT TUNE
50 MT DECAY
51 MT LEVEL
103 MT CTRL

52 HT TUNE
53 HT DECAY
54 HT LEVEL
104 HT CTRL

55 RS TUNE
56 RS DECAY
57 RS LEVEL
105 RS CTRL

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

83 CC TUNE
84 CC DECAY
85 CC LEVEL
109 CC CTRL

86 RC TUNE
87 RC DECAY
88 RC LEVEL
110 RC CTRL

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
track MT 10 45 47 49 50 51 103 30 31 32 33 34 35 36 37 18 39
track HT 10 48 50 52 53 54 104 40 41 42 43 44 45 46 47 48 49
track RS 10 56 37 55 56 57 105 50 51 52 53 54 55 56 57 58 59
track HC 10 54 39 58 59 60 106 60 61 62 63 64 65 66 67 68 69
track CH 10 44 42 61 62 63 107 70 71 72 73 74 75 76 77 78 79
track OH 10 58 46 80 81 82 108 80 81 82 83 84 85 86 87 88 89
track CC 10 61 49 83 84 85 109 90 91 92 93 94 95 96 97 98 99
track RC 10 63 51 86 87 88 110 100 101 102 103 104 105 106 107 108 109



```


## Problems



