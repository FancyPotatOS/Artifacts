#
#   Tick
#   
#   Purpose: To update combination clock and run when needed
#
#   Input: None
#


scoreboard players add combination.clock artifacts.master 1
scoreboard players operation combination.clock artifacts.master %= config.combination.clock artifacts.master

execute if score combination.clock artifacts.master matches 0 run function artifacts:combination/clock

