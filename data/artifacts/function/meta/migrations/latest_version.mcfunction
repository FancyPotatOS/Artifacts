#
#   Migration File V1
#   
#   Purpose: To update the datapack up to this level, then apply new/updated configs or setup
#
#   Input: None
#


tellraw @a ["",{"text":"[Artifacts Datapack - V1]","bold":true,"color":"dark_blue"}," - Setup"]

# Apply last migration
#execute unless score version artifacts.master matches 1.. run function artifacts:meta/migrate/migration_v0

# Set the version
scoreboard players set version artifacts.master 1


scoreboard objectives add artifacts.time_since_used_record minecraft.custom:minecraft.total_world_time
scoreboard players set config.special_window artifacts.time_since_used_record 40

scoreboard players set config.combination.clock artifacts.master 20


# SMW mushroom
scoreboard objectives add artifacts.collectibles.super_mario_world.mushroom.cooldown dummy
scoreboard objectives add artifacts.collectibles.super_mario_world.mushroom.time_since_used minecraft.custom:minecraft.total_world_time
scoreboard players set config.cooldown artifacts.collectibles.super_mario_world.mushroom.cooldown 200


# Triggers
scoreboard objectives add toggle_curse_of_greed trigger
scoreboard objectives modify toggle_curse_of_greed displayname [{"text":"Toggled ",color:"white"}, {"text":"Curse of Greed","color":"red",hover_event:{action:"show_text","value":{"text":"Allows the world to drop artifacts around the player",color:"gray",italic:true}}}]

scoreboard objectives add toggle_perfect_pitch trigger
scoreboard objectives modify toggle_perfect_pitch displayname [{"text":"Toggled ",color:"white"}, {"text":"Perfect Pitch",color:"gray",hover_event:{action:"show_text","value":{"text":"Allows the world to drop artifact records around the player",color:"gray",italic:true}}}]


return 0
# Used for Spyglass
scoreboard objectives add fpconflict.conflict_map dummy

