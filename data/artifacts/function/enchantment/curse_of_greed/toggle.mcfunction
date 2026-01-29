
execute if predicate artifacts:entity/curse_of_greed/wearing run tag @s add artifacts.enchantment.curse_of_greed.toggle

execute unless entity @s[tag=artifacts.enchantment.curse_of_greed.toggle] run item modify entity @s armor.chest artifacts:curse_of_greed/add
execute if entity @s[tag=artifacts.enchantment.curse_of_greed.toggle] run item modify entity @s armor.chest artifacts:curse_of_greed/remove

tag @s remove artifacts.enchantment.curse_of_greed.toggle
