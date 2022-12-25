from db import db_manager as DB

import random

nums = list(range(1, 1000))
random.shuffle(nums)

wordDB=DB(r"C:\Users\arman\Documents\juragi\data\main.db")

with open("data\wordlist.txt","r",encoding="UTF-8") as f:
    for n, i in enumerate(f.read().splitlines()):
        wordDB.addWord(i,nums[n])
        print(n)