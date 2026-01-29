

scoreboard players remove @a artifacts.collectibles.super_mario_world.mushroom.cooldown 1


execute as @a if score @s artifacts.collectibles.super_mario_world.mushroom.cooldown matches 0 at @s run function artifacts:collectibles/super_mario_world/mushroom/deactivate

