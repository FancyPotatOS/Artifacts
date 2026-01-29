

scoreboard players reset @s toggle_perfect_pitch
advancement revoke @s only artifacts:enchantment/toggle_perfect_pitch

execute if items entity @s armor.head #minecraft:head_armor run function artifacts:enchantment/perfect_pitch/toggle

