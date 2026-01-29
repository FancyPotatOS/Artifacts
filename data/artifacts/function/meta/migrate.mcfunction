
# Ensure the master scoreboard exists
scoreboard objectives add artifacts.master dummy

# Apply migration if required
execute unless score version artifacts.master matches 1.. run function artifacts:meta/migrations/latest_version
