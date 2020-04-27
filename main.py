trees = {
    "normal": 81,
    "oak": 50,
    "willow": 52,
    "teak": 41,
    "maple": 24,
    "mahogany": 23,
    "yew": 59,
    "magic": 60,
    "redwood": 58,
}

current_wc_tokens = 268

total_mastery = len(trees) * 99
current_mastery = 0
for tree, mastery in trees.items():
    current_mastery += mastery

print("Remaining Mastery = " + str(total_mastery - current_mastery))
print("Tokens Needed = " + str((total_mastery-current_mastery) - current_wc_tokens))
