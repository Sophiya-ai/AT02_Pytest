def count_vowel(string):
    vowels = set("aeiouауоиэыяюеё")
    summa = 0
    for char in string.lower():
        if char in vowels:
            summa += 1
    return summa
