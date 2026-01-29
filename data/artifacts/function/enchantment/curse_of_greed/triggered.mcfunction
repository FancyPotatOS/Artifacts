

scoreboard players reset @s toggle_curse_of_greed
advancement revoke @s only artifacts:enchantment/toggle_curse_of_greed

execute if items entity @s armor.chest #minecraft:chest_armor run function artifacts:enchantment/curse_of_greed/toggle

