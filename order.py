from db import db_manager
from itertools import count
from random import shuffle

class Present:
    _n=count(0)
    def __init__(self, Word, ID, Num) -> None:
        self.word=Word
        self.id=ID
        self.num=Num
        self.n=next(self._n)



    def show(self):
        print(f"My num is {self.num}\nI'm from {self.word}\nMy ID:\n{self.id}")
        print(self.n)
    def test(self, test_tuple):
        if self.num == test_tuple[0]:
            return False, "NUM"
        if self.id == test_tuple[1]:
        
            return False, "ID"

        self.parent_num=test_tuple[0]
        return True, "Smile"

def getOrder(presents_list):
    
    presents=[Present(i[0], i[2], i[1]) for i in presents_list]
    all_nums=[(p.num, p.id) for p in presents]
    
    test_cycle=0
    while test_cycle<10000:
        
        print(f"Shuffling {test_cycle} time")
        new_nums=all_nums.copy()
        shuffle(new_nums)
        
        good=True
        for n, tp in enumerate(new_nums):
            bol, prob=presents[n].test(tp)
            if not(bol):
                good=False
        
        if good:
            print("Atradu")
            return True, presents, test_cycle
        else:
            test_cycle+=1
    
    return False, presents, test_cycle


if __name__=="__main__":
    
    
    
    DB=db_manager(r"C:\Users\arman\Documents\juragi\data\main.db")
    order=getOrder(DB.getAllPresents())


                