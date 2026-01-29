
execute if predicate artifacts:entity/perfect_pitch/wearing run tag @s add artifacts.enchantment.perfect_pitch.toggle

execute unless entity @s[tag=artifacts.enchantment.perfect_pitch.toggle] run item modify entity @s armor.head artifacts:perfect_pitch/add
execute if entity @s[tag=artifacts.enchantment.perfect_pitch.toggle] run item modify entity @s armor.head artifacts:perfect_pitch/remove

tag @s remove artifacts.enchantment.perfect_pitch.toggle
