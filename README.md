# Bitcoin-Puzzle

Interesting puzzle, I checked for patterns between binary values, decimal values, floor values. Just cant find anything

I updated an excel sheet puzzle bitcoin.xlsx with allot more data of each puzzle. Like decimal, binary, floor, and allot 
more data per puzzle. Even multipliers of the data to the next puzzle.

Since this range is just so huge, I think a random generator would maybe work best to try and find the needle.

I attached below my python script trying the next puzzle randomly if someone might benefit to

https://github.com/negate7o4/Bitcoin-Puzzle

On my rig, I7 if I run 5 X instances, it checks about 11 500 possibilities per second but eats 80% cpu.
So the code chews threw 16.5 Mil random possibilities per day

If you want to try a different puzzle, just change these values in the script :

address = '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'

start_key = '0000000000000000000000000000000000000000000000040000000000000000'
stop_key = '000000000000000000000000000000000000000000000007ffffffffffffffff'

Also take note of the cpu threads the code uses, update according to your threads.

Their is also a text file in my repository of the correct pip's you need to install for the code to work
