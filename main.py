# from selenium import webdriver

# driver = webdriver.Chrome(
#     executable_path=r"C:\Users\charles\git\MelvorCalculator\chromedriver.exe")
# driver.get("https://melvoridle.com/index.php")
# redwood_elem = driver.find_element_by_xpath(
#     "//*[@id='mastery-screen-skill-0-8']")
# print(redwood_elem)

trees = {
    "normal": 81,
    "oak": 50,
    "willow": 52,
    "teak": 53,
    "maple": 51,
    "mahogany": 46,
    "yew": 59,
    "magic": 60,
    "redwood": 63,
}

current_wc_tokens = 298

total_mastery = len(trees) * 99
current_mastery = 0
for tree, mastery in trees.items():
    current_mastery += mastery

print("Remaining Mastery = " + str(total_mastery - current_mastery))
print("Tokens Needed = " + str((total_mastery-current_mastery) - current_wc_tokens))
