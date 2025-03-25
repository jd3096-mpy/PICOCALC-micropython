from buzzer_music import music
from time import sleep

#Example songs

song='0 B4 0.75 14;2 B4 0.75 14;4 B4 0.75 14;5 A4 0.75 14;7 B4 0.75 14;9 D5 0.75 14;11 B4 0.75 14;13 F#4 0.75 14;14 A4 1.75 14;16 B4 0.75 14;18 B4 0.75 14;20 B4 0.75 14;21 A4 0.75 14;23 B4 0.75 14;25 F5 0.75 14;27 E5 0.75 14;29 D5 0.75 14;30 A4 1.75 14;32 B4 0.75 14;34 B4 0.75 14;36 B4 0.75 14;37 A4 0.75 14;39 B4 0.75 14;41 D5 0.75 14;43 B4 0.75 14;45 F#4 0.75 14;46 A4 1.75 14;48 B4 0.75 14;50 B4 0.75 14;52 B4 0.75 14;53 A4 0.75 14;55 B4 0.75 14;57 F5 0.75 14;59 E5 0.75 14;61 B4 0.75 14;62 A4 1.75 14;64 B4 0.75 14;66 B4 0.75 14;68 B4 0.75 14;69 A4 0.75 14;71 B4 0.75 14;73 D5 0.75 14;75 B4 0.75 14;77 F#4 0.75 14;78 A4 1.75 14;80 B4 0.75 14;82 B4 0.75 14;84 B4 0.75 14;85 A4 0.75 14;87 B4 0.75 14;89 F5 0.75 14;91 E5 0.75 14;93 D5 0.75 14;94 A4 1.75 14;96 B4 0.75 14;98 B4 0.75 14;100 B4 0.75 14;101 A4 0.75 14;103 B4 0.75 14;105 D5 0.75 14;107 B4 0.75 14;109 F#4 0.75 14;110 A4 1.75 14;112 B4 0.75 14;114 B4 0.75 14;116 B4 0.75 14;118 A4 0.75 14;119 B4 0.75 14;128 F#6 5.75 14;134 F6 5.75 14;142 D6 0.75 14;143 E6 0.75 14;144 F6 2.75 14;147 E6 2.75 14;150 D6 1.75 14;152 C#6 2.75 14;155 D6 2.75 14;158 E6 1.75 14;160 F#6 5.75 14;166 B6 5.75 14;172 B5 1.75 14;174 C#6 1.75 14;176 D6 2.75 14;179 E6 2.75 14;182 D6 1.75 14;184 C#6 2.75 14;187 A6 2.75 14;190 G6 1.75 14;192 B5 5.75 14;192 D6 5.75 14;192 F#6 5.75 14;198 B5 5.75 14;198 D6 5.75 14;198 F6 5.75 14;206 D6 0.75 14;207 E6 0.75 14;208 G5 2.75 14;208 C#6 2.75 14;208 F6 2.75 14;211 E6 2.75 14;214 D6 1.75 14;216 A#5 2.75 14;216 C#6 2.75 14;219 D6 2.75 14;222 E6 1.75 14;224 B5 5.75 14;224 F#6 5.75 14;230 F6 5.75 14;230 B6 5.75 14;236 B6 1.75 14;238 C#7 1.75 14;240 B6 2.75 14;240 D7 2.75 14;243 E7 2.75 14;246 G6 1.75 14;248 F#6 2.75 14;251 D7 2.75 14;254 E7 1.75 14;256 B5 5.75 14;256 D6 5.75 14;256 F#6 5.75 14;262 B5 5.75 14;262 D6 5.75 14;262 F6 5.75 14;270 D6 0.75 14;271 E6 0.75 14;272 G5 2.75 14;272 B5 2.75 14;272 F6 2.75 14;275 E6 2.75 14;278 D6 1.75 14;280 G5 2.75 14;280 C#6 2.75 14;283 D6 2.75 14;286 E6 1.75 14;288 B5 5.75 14;288 D6 5.75 14;288 F#6 5.75 14;294 C#6 5.75 14;294 F6 5.75 14;294 B6 5.75 14;300 B5 1.75 14;302 C#6 1.75 14;304 D6 2.75 14;307 E6 2.75 14;310 D6 1.75 14;312 C#6 2.75 14;315 A6 2.75 14;318 G6 1.75 14;320 B5 5.75 14;320 D6 5.75 14;320 F#6 5.75 14;326 B5 5.75 14;326 D6 5.75 14;326 F6 5.75 14;334 D6 0.75 14;335 E6 0.75 14;336 D6 5.75 14;336 F#6 5.75 14;342 F6 5.75 14;342 B6 5.75 14;348 B5 1.75 14;350 C#6 1.75 14;352 D6 2.75 14;355 G6 2.75 14;358 F#6 1.75 14;360 F6 2.75 14;363 D7 2.75 14;366 A#6 1.75 14;368 B6 3.75 14;0 B3 0.75 15;2 B3 0.75 15;4 B3 0.75 15;5 A3 0.75 15;7 B3 0.75 15;9 D4 0.75 15;11 B3 0.75 15;13 F#3 0.75 15;14 A3 1.75 15;16 B3 0.75 15;18 B3 0.75 15;20 B3 0.75 15;21 A3 0.75 15;23 B3 0.75 15;25 F4 0.75 15;27 E4 0.75 15;29 D4 0.75 15;30 A3 1.75 15;32 B3 0.75 15;34 B3 0.75 15;36 B3 0.75 15;37 A3 0.75 15;39 B3 0.75 15;41 D4 0.75 15;43 B3 0.75 15;45 F#3 0.75 15;46 A3 1.75 15;48 B3 0.75 15;50 B3 0.75 15;52 B3 0.75 15;53 A3 0.75 15;55 B3 0.75 15;57 F4 0.75 15;59 E4 0.75 15;61 B3 0.75 15;62 A3 1.75 15;64 B3 0.75 15;66 B3 0.75 15;68 B3 0.75 15;69 A3 0.75 15;71 B3 0.75 15;73 D4 0.75 15;75 B3 0.75 15;77 F#3 0.75 15;78 A3 1.75 15;80 B3 0.75 15;82 B3 0.75 15;84 B3 0.75 15;85 A3 0.75 15;87 B3 0.75 15;89 F4 0.75 15;91 E4 0.75 15;93 D4 0.75 15;94 A3 1.75 15;96 B3 0.75 15;98 B3 0.75 15;100 B3 0.75 15;101 A3 0.75 15;103 B3 0.75 15;105 D4 0.75 15;107 B3 0.75 15;109 F#3 0.75 15;110 A3 1.75 15;112 B3 0.75 15;114 B3 0.75 15;116 B3 0.75 15;118 A3 0.75 15;119 B3 0.75 15;128 B3 5.75 15;128 F#4 5.75 15;128 B4 5.75 15;134 G#3 5.75 15;134 D4 5.75 15;134 F4 5.75 15;144 B3 7.75 15;144 B4 7.75 15;152 F#3 7.75 15;152 F#4 7.75 15;160 B3 5.75 15;160 F#4 5.75 15;160 B4 5.75 15;166 G#3 5.75 15;166 D4 5.75 15;166 F4 5.75 15;176 C#4 7.75 15;176 C#5 7.75 15;184 F#3 7.75 15;184 F#4 7.75 15;192 B3 5.75 15;192 F#4 5.75 15;192 B4 5.75 15;198 G#3 5.75 15;198 D4 5.75 15;198 F4 5.75 15;208 B3 7.75 15;208 B4 7.75 15;216 F#3 7.75 15;216 F#4 7.75 15;224 B3 5.75 15;224 F#4 5.75 15;224 B4 5.75 15;230 G#3 5.75 15;230 D4 5.75 15;230 F4 5.75 15;240 C#4 7.75 15;240 C#5 7.75 15;248 F#3 7.75 15;248 F#4 7.75 15;256 B3 5.75 15;256 F#4 5.75 15;256 B4 5.75 15;262 G#3 5.75 15;262 D4 5.75 15;262 F4 5.75 15;272 B3 7.75 15;272 B4 7.75 15;280 F#3 7.75 15;280 F#4 7.75 15;288 B3 5.75 15;288 F#4 5.75 15;288 B4 5.75 15;294 G#3 5.75 15;294 D4 5.75 15;294 F4 5.75 15;304 C#4 7.75 15;304 C#5 7.75 15;312 F#3 7.75 15;312 F#4 7.75 15;320 B3 5.75 15;320 F#4 5.75 15;320 B4 5.75 15;326 G#3 5.75 15;326 D4 5.75 15;326 F4 5.75 15;336 B3 5.75 15;336 F#4 5.75 15;336 B4 5.75 15;342 G#3 5.75 15;342 D4 5.75 15;342 F4 5.75 15;352 C#4 7.75 15;352 C#5 7.75 15;360 F#3 7.75 15;360 F#4 7.75 15;368 B3 3.75 15;368 F#4 3.75 15'

"""
Find a piece of music on onlinesequencer.net, click edit,
then select all notes with CTRL+A and copy them with CTRL+C

Paste string as shown above after removing ";:" from
the end and "Online Sequencer:120233:" from the start
"""

from machine import Pin

#One buzzer on pin 0
mySong = music(song, pins=[Pin(10)])

#Four buzzers
#mySong = music(song, pins=[Pin(0),Pin(1),Pin(2),Pin(3)])

while True:
    mySong.tick()
    sleep(0.03)