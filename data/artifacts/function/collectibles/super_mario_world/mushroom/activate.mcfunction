

attribute @s minecraft:block_interaction_range modifier add artifacts:collectibles/super_mario_world/mushroom 1 add_multiplied_base
attribute @s minecraft:entity_interaction_range modifier add artifacts:collectibles/super_mario_world/mushroom 1 add_multiplied_base
attribute @s minecraft:jump_strength modifier add artifacts:collectibles/super_mario_world/mushroom 0.2 add_value
attribute @s minecraft:gravity modifier add artifacts:collectibles/super_mario_world/mushroom 0.018 add_value
attribute @s minecraft:movement_speed modifier add artifacts:collectibles/super_mario_world/mushroom 1 add_multiplied_base
attribute @s minecraft:scale modifier add artifacts:collectibles/super_mario_world/mushroom 1 add_multiplied_base
attribute @s minecraft:step_height modifier add artifacts:collectibles/super_mario_world/mushroom 1 add_multiplied_base
attribute @s minecraft:sneaking_speed modifier add artifacts:collectibles/super_mario_world/mushroom .25 add_multiplied_base

scoreboard players operation @s artifacts.collectibles.super_mario_world.mushroom.cooldown = config.cooldown artifacts.collectibles.super_mario_world.mushroom.cooldown

