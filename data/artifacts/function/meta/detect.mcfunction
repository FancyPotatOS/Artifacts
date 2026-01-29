
execute unless score version.artifacts fpconflict.conflict_map matches 1 run tellraw @a ["",{"text":"[Conflict]","color":"red"}," - ",{"text":"Artifacts Datapack - V1 ","color":"blue"},"(",{"text":"Overlapping versions.","italic":true,"color":"dark_aqua"},")"]
