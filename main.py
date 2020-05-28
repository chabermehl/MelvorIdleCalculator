# from selenium import webdriver

# driver = webdriver.Chrome(
#     executable_path=r"C:\Users\charles\git\MelvorCalculator\chromedriver.exe")
# driver.get("https://melvoridle.com/index.php")
# redwood_elem = driver.find_element_by_xpath(
#     "//*[@id='mastery-screen-skill-0-8']")
# print(redwood_elem)

trees = {
    "normal": 99,
    "oak": 99,
    "willow": 99,
    "teak": 92,
    "maple": 93,
    "mahogany": 89,
    "yew": 99,
    "magic": 99,
    "redwood": 99,
}

current_wc_tokens = 0

total_mastery = len(trees) * 99
current_mastery = 0
for tree, mastery in trees.items():
    current_mastery += mastery

print("Remaining Mastery = " + str(total_mastery - current_mastery))
print("Tokens Needed = " + str((total_mastery-current_mastery) - current_wc_tokens))
