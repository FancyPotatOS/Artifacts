
import os
import shutil
import urllib.request as request
import time
import PIL.Image as Image
import pyperclip

from mutagen.oggvorbis import OggVorbis


os.chdir("C:/Users/caleb/AppData/Roaming/.minecraft/saves/Creative 1_21_10/datapacks/Artifacts - 1.21.10")


def generate_files(source_path: str, replacements: dict[str], insertions: list[list[tuple[str]]]):
    file_contents = None
    with open(source_path, "r") as file:
        file_contents = "".join(file.readlines())

    for insertion in insertions:
        for repl in insertion:
            replacements[repl[0]] = repl[1]
        
        new_file_contents = replace_all(file_contents, replacements)

        with open(replace_all(source_path, replacements), "w") as file:
            file.write(new_file_contents)


def replace_all(raw: str, replacements: dict[str]):
    for replacement in replacements.keys():
        raw = raw.replace(replacement, replacements[replacement])
    
    return raw


biomes = [
    "badlands",
    "bamboo_jungle",
    "basalt_deltas",
    "beach",
    "birch_forest",
    "cherry_grove",
    "cold_ocean",
    "crimson_forest",
    "dark_forest",
    "deep_cold_ocean",
    "deep_dark",
    "deep_frozen_ocean",
    "deep_lukewarm_ocean",
    "deep_ocean",
    "desert",
    "dripstone_caves",
    "end_barrens",
    "end_highlands",
    "end_midlands",
    "eroded_badlands",
    "flower_forest",
    "forest",
    "frozen_ocean",
    "frozen_peaks",
    "frozen_river",
    "grove",
    "ice_spikes",
    "jagged_peaks",
    "jungle",
    "lukewarm_ocean",
    "lush_caves",
    "mangrove_swamp",
    "meadow",
    "mushroom_fields",
    "nether_wastes",
    "ocean",
    "old_growth_birch_forest",
    "old_growth_pine_taiga",
    "old_growth_spruce_taiga",
    "pale_garden",
    "plains",
    "river",
    "savanna",
    "savanna_plateau",
    "small_end_islands",
    "snowy_beach",
    "snowy_plains",
    "snowy_slopes",
    "snowy_taiga",
    "soul_sand_valley",
    "sparse_jungle",
    "stony_peaks",
    "stony_shore",
    "sunflower_plains",
    "swamp",
    "taiga",
    "the_end",
    "the_void",
    "warm_ocean",
    "warped_forest",
    "windswept_forest",
    "windswept_gravelly_hills",
    "windswept_hills",
    "windswept_savanna",
    "wooded_badlands",
]

os.chdir("C:/Users/caleb/AppData/Roaming/.minecraft/saves/Creative 1_21_10/datapacks/Artifacts - 1.21.10/data/artifacts/tags/worldgen/biome")

chosen_biomes = []
for biome_groups in [f for f in os.listdir() if os.path.isfile(f)]:
    lines = []
    with open(biome_groups, "r") as file:
      lines = file.readlines()
    lines = [l.replace(" ", "").replace("minecraft:", "").replace("\"", "").replace(",", "").replace("\n", "") for l in lines if len("        \"minecraft:") < len(l)]
    
    if len([l for l in lines if l in chosen_biomes]):
        print("OVERLAP!", lines, chosen_biomes)

    chosen_biomes += lines
  
raw_json = """        "minecraft:_NAME_\""""
pyperclip.copy(",\n".join([replace_all(raw_json, {"_NAME_": x}) for x in biomes if not x in chosen_biomes]))

      


exit()

names = [
    "dkc",
    "inscryption",
    "junk_jack",
    "kirby_amazing_mirror",
    "pokemon/pokeballs",
    "pokemon/minis",
    "powder",
    "super_mario_world",
    "terraria",
    "warioware_inc",
]


raw_loot_table = """
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "value": "artifacts:collectibles/_NAME_/choose",
          "conditions": [
            {
              "condition": "minecraft:location_check",
              "predicate": {
                "biomes": "#artifacts:_NAME_"
              }
            }
          ]
        }
      ],
      "functions": [
        {
          "function": "minecraft:limit_count",
          "limit": 1
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance_with_enchanted_bonus",
          "unenchanted_chance": 0.005,
          "enchanted_chance": 0.01,
          "enchantment": "minecraft:looting"
        }
      ]
    }"""

coll = []
for name in names:
    coll.append(replace_all(raw_loot_table, {"_NAME_": name}))

pyperclip.copy(",".join(coll))
print("Copied")


exit()


img_links = [
    "https://static.wikia.nocookie.net/inscryption/images/0/05/Pixelability_mightyleap.png/revision/latest?cb=20230111053056",
    "https://static.wikia.nocookie.net/inscryption/images/5/59/Pixelability_bifurcatedstrike.png/revision/latest?cb=20230111052821",
    "https://static.wikia.nocookie.net/inscryption/images/4/4c/Pixelability_trifurcatedstrike.png/revision/latest?cb=20230111053220",
    "https://static.wikia.nocookie.net/inscryption/images/1/15/Pixelability_frozenaway.png/revision/latest?cb=20230111052936",
    "https://static.wikia.nocookie.net/inscryption/images/a/a8/Pixelability_steeltrap.png/revision/latest?cb=20230111053208",
    "https://static.wikia.nocookie.net/inscryption/images/8/8d/Pixelability_rabbithole.png/revision/latest?cb=20230111053112",
    "https://static.wikia.nocookie.net/inscryption/images/4/4a/Pixelability_sprinter.png/revision/latest?cb=20230111053156",
    "https://static.wikia.nocookie.net/inscryption/images/6/61/Pixelability_touchofdeath.png/revision/latest?cb=20230111053214",
    "https://static.wikia.nocookie.net/inscryption/images/6/68/Pixelability_fledgeling.png/revision/latest?cb=20230111052931",
    "https://static.wikia.nocookie.net/inscryption/images/b/b4/Pixelability_burrower.png/revision/latest?cb=20230111052859",
    "https://static.wikia.nocookie.net/inscryption/images/2/23/Pixelability_fecundity.png/revision/latest?cb=20230111052926",
    "https://static.wikia.nocookie.net/inscryption/images/d/d1/Pixelability_boneking.png/revision/latest?cb=20230111052850",
    "https://static.wikia.nocookie.net/inscryption/images/2/2c/Pixelability_unkillable.png/revision/latest?cb=20230111053226",
    "https://static.wikia.nocookie.net/inscryption/images/8/88/Pixelability_sharpquills.png/revision/latest?cb=20230111053135",
    "https://static.wikia.nocookie.net/inscryption/images/7/7d/Pixelability_hefty.png/revision/latest?cb=20230111053024",
    "https://static.wikia.nocookie.net/inscryption/images/3/38/Pixelability_guardian.png/revision/latest?cb=20230111053004",
    "https://static.wikia.nocookie.net/inscryption/images/f/f1/Pixelability_airbourne.png/revision/latest?cb=20230111052804",
    "https://static.wikia.nocookie.net/inscryption/images/8/85/Pixelability_manylives.png/revision/latest?cb=20230111053044",
    "https://static.wikia.nocookie.net/inscryption/images/d/dc/Pixelability_repulsive.png/revision/latest?cb=20230111053118",
    "https://static.wikia.nocookie.net/inscryption/images/2/2f/Pixelability_worthysacrifice.png/revision/latest?cb=20230111053236",
    "https://static.wikia.nocookie.net/inscryption/images/1/10/Pixelability_bonedigger.png/revision/latest?cb=20230111052844",
    "https://static.wikia.nocookie.net/inscryption/images/8/87/Pixelability_brittle.png/revision/latest?cb=20230111052855",
    "https://static.wikia.nocookie.net/inscryption/images/a/a6/Pixelability_skeletoncrew.png/revision/latest?cb=20230111053140",
    "https://static.wikia.nocookie.net/inscryption/images/3/31/Pixelability_greenmox.png/revision/latest?cb=20230111052958",
    "https://static.wikia.nocookie.net/inscryption/images/a/a4/Pixelability_orangemox.png/revision/latest?cb=20230111053106",
    "https://static.wikia.nocookie.net/inscryption/images/c/ce/Pixelability_bluemox.png/revision/latest?cb=20230111052831",
    "https://static.wikia.nocookie.net/inscryption/images/2/22/Pixelability_gemanimator.png/revision/latest?cb=20230111052941",
    "https://static.wikia.nocookie.net/inscryption/images/2/25/Pixelability_rubyheart.png/revision/latest?cb=20230111053123",
    "https://static.wikia.nocookie.net/inscryption/images/5/5a/Pixelability_mentalgemnastics.png/revision/latest?cb=20230111053049",
    "https://static.wikia.nocookie.net/inscryption/images/7/7a/Pixelability_gemdependant.png/revision/latest?cb=20230111052946",
    "https://static.wikia.nocookie.net/inscryption/images/6/65/Pixelability_greatmox.png/revision/latest?cb=20230111052951",
    "https://static.wikia.nocookie.net/inscryption/images/9/94/Pixelability_handy.png/revision/latest?cb=20230111053009",
    "https://static.wikia.nocookie.net/inscryption/images/3/3b/Pixelability_squirrelshedder.png/revision/latest?cb=20230111053202",
    "https://static.wikia.nocookie.net/inscryption/images/f/f1/Pixelability_attackconduit.png/revision/latest?cb=20230111052810",
    "https://static.wikia.nocookie.net/inscryption/images/c/cd/Pixelability_spawnconduit.png/revision/latest?cb=20230111053147",
    "https://static.wikia.nocookie.net/inscryption/images/9/92/Pixelability_nullconduit.png/revision/latest?cb=20230111053101",
    "https://static.wikia.nocookie.net/inscryption/images/a/a7/Pixelability_batterybearer.png/revision/latest?cb=20230111052816",
    "https://static.wikia.nocookie.net/inscryption/images/5/51/Pixelability_detonator.png/revision/latest?cb=20230111052904",
    "https://static.wikia.nocookie.net/inscryption/images/8/8d/Pixelability_sentry.png/revision/latest?cb=20230111053129",
    "https://static.wikia.nocookie.net/inscryption/images/d/df/Pixelability_energyconduit.png/revision/latest?cb=20230111052918",
    "https://static.wikia.nocookie.net/inscryption/images/2/2a/Pixelability_bombspewer.png/revision/latest?cb=20230111052837",
    "https://static.wikia.nocookie.net/inscryption/images/8/85/Pixelability_doubledeath.png/revision/latest?cb=20230111052909",
    "https://static.wikia.nocookie.net/inscryption/images/2/22/Pixelability_powerdice.png/revision/latest?cb=20211217192017",
    "https://static.wikia.nocookie.net/inscryption/images/8/87/Pixelability_enlarge.png/revision/latest?cb=20211217200918",
    "https://static.wikia.nocookie.net/inscryption/images/8/81/Pixelability_disentomb.png/revision/latest?cb=20211217200721",
    "https://static.wikia.nocookie.net/inscryption/images/b/be/Pixelability_energygun.png/revision/latest?cb=20211217191355",
    "https://static.wikia.nocookie.net/inscryption/images/0/04/Pixelability_looter.png/revision/latest?cb=20230111053035",
    "https://static.wikia.nocookie.net/inscryption/images/4/4f/Pixelability_truescholar.png/revision/latest?cb=20211221050521",
    "https://static.wikia.nocookie.net/inscryption/images/3/39/Pixelability_stimulate.png/revision/latest?cb=20211217195554",
    "https://static.wikia.nocookie.net/inscryption/images/c/ca/Pixelability_bonehorn.png/revision/latest?cb=20211217200410",
    "https://static.wikia.nocookie.net/inscryption/images/2/20/Pixelability_waterborne.png/revision/latest?cb=20230111053231",
    "https://static.wikia.nocookie.net/inscryption/images/c/ce/Pixelability_krakenwaterborne.png/revision/latest?cb=20230111053029",
]

raw_str = """
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "value": "artifacts:collectibles/inscryption/_ITEMNAME_"
        }
      ]
    }"""
raw_str_coll = []

replacements = {}
insertions = []

target_size = (87, 87)
for link in img_links:
    sigil_name = link[71:-38]

    insertions.append([("_ITEMNAME_", sigil_name)])

    raw_str_coll.append(replace_all(raw_str, {"_ITEMNAME_": sigil_name}))
    
    continue
    img_filename = f"C:/Users/caleb/AppData/Roaming/.minecraft/resourcepacks/Artifacts - 1.21.10/assets/artifacts/textures/item/collectibles/inscryption/{sigil_name}.png"

    img = Image.open(img_filename).convert("RGBA")
    target_pos = (int((target_size[0] - img.width) / 2), int((target_size[1] - img.height) / 2))

    new_img = Image.new("RGBA", target_size, "#00000000")
    new_img.paste(img, (target_pos[0], target_pos[1], target_pos[0] + img.width, target_pos[1] + img.height))

    new_img.save(img_filename)

    break
    request.urlretrieve(link, f"C:/Users/caleb/AppData/Roaming/.minecraft/resourcepacks/Artifacts - 1.21.10/assets/artifacts/textures/item/collectibles/inscryption/{sigil_name}.png")

    time.sleep(1)

print(",".join(raw_str_coll))
    
#generate_files(f"C:/Users/caleb/AppData/Roaming/.minecraft/saves/Creative 1_21_10/datapacks/Artifacts/data/artifacts/loot_table/collectibles/inscryption/_ITEMNAME_.json", replacements, insertions)




exit()

item_names = [
    "abeemination",
    "bloody_spine",
    "celestial_sigil",
    "clothier_voodoo_doll",
    "deer_thing",
    "gelatin_crystal",
    "guide_voodoo_doll",
    "lihzahrd_power_cell",
    "mechanical_eye",
    "mechanical_skull",
    "mechanical_worm",
    "prismatic_lacewing",
    "slime_crown",
    "suspicious_looking_eye",
    "truffle_worm",
    "worm_food",
]

replacements = {}
insertions = []
for name in item_names:
    insertions.append([
        ("_ITEMNAME_", name),
        ("_PROPERNAME_", name.replace("_", " ").title())
    ])

generate_files("C:/Users/caleb/AppData/Roaming/.minecraft/saves/Creative 1_21_10/datapacks/Artifacts/data/artifacts/loot_table/collectibles/terraria/_ITEMNAME_.json", replacements, insertions)



exit()

## Create all pokemon records entries
pokeballs = [
    "poke_ball",
    "great_ball",
    "ultra_ball",
    "master_ball",
    "dive_ball",
    "luxury_ball",
    "nest_ball",
    "net_ball",
    "premier_ball",
    "repeat_ball",
    "safari_ball",
    "timer_ball",
]

songs = [
    "frlg_battle_wild_pokemon",
    "frlg_lavender_town",
    "frlg_s_s_anne",
    "frlg_surfing",
    "rgby_battle_gym_leader",
    "rgby_celadon_city",
    "rgby_pokemon_tower",
    "rgby_route_one",
    "rse_battle_team_aqua_team_magma",
    "rse_littleroot_town",
    "rse_route_one_zero_one",
    "rse_sootopolis_city",
]

artists = [
    "Go Ichinose",
    "Junichi Masuda",
    "Junichi Masuda, Shota Kageyama",
    "Morikazu Aoki",
    "Junichi Masuda",
    "Junichi Masuda",
    "Junichi Masuda",
    "Morikazu Aoki",
    "Junichi Masuda",
    "Go Ichinose",
    "Junichi Masuda",
    "Go Ichinose"
]

def get_song_length(filepath: str):
    
    ogg_file = OggVorbis(filepath)
    return str(int(ogg_file.info.length))

def clean_song_name(name: str):
    name = " ".join(name.split("_")[1:]).title()
    if name.startswith("Battle"):
        name = name.replace("Battle ", "Battle! (") + ")"
        name.replace("One Zero One", " 101").replace("One", "1").replace("Aqua Team", "Aqua, Team").replace(" S ", " S. ")
    
    return name

replacements = {}
insertions = []

for index in range(len(songs)):
    insertions.append([("_ITEMNAME_", pokeballs[index]),("_SONGNAME_", songs[index]), ("_PROPERNAME_", clean_song_name(songs[index])), ("_ARTIST_", artists[index]), ("_LENGTH_", get_song_length(f"C:/Users/caleb/AppData/Roaming/.minecraft/resourcepacks/Artifacts - 1.21.10/assets/artifacts/sounds/music/pokemon/{songs[index]}.ogg"))])


generate_files("C:/Users/caleb/AppData/Roaming/.minecraft/saves/Creative 1_21_10/datapacks/Artifacts/data/artifacts/loot_table/records/pokemon/_ITEMNAME_.json", replacements, insertions)
