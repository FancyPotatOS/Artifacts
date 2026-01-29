

execute if predicate artifacts:collectibles/kirby_amazing_mirror/held/left_hand/is_trophy_base if predicate artifacts:collectibles/kirby_amazing_mirror/held/right_hand/is_trophy_no_base run function artifacts:collectibles/kirby_amazing_mirror/combine_to_right

execute if predicate artifacts:collectibles/kirby_amazing_mirror/held/right_hand/is_trophy_base if predicate artifacts:collectibles/kirby_amazing_mirror/held/left_hand/is_trophy_no_base run function artifacts:collectibles/kirby_amazing_mirror/combine_to_left

playsound minecraft:block.amethyst_block.break player @s ~ ~ ~ 1 1
execute at @s anchored eyes run particle minecraft:item{item:"minecraft:gold_block"} ^ ^-0.15 ^0.2 0 0 0 0.03 10 normal
