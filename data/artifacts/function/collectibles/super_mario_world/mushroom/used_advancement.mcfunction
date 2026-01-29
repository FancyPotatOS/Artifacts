
advancement revoke @s only artifacts:collectibles/super_mario_world/mushroom/used

execute if score @s artifacts.collectibles.super_mario_world.mushroom.time_since_used matches 0.. run function artifacts:collectibles/super_mario_world/mushroom/activate

scoreboard players set @s artifacts.collectibles.super_mario_world.mushroom.time_since_used -2

