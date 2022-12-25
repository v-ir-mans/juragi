# using time module
import time
import uuid
import sqlite3
import random

class db_manager:
    def __init__(self, path) -> None:
        self.path=path

    def addWord(self,word,num):
        self.start()
        self.cursor.execute("INSERT OR IGNORE INTO FullWordList (Word,Num,Used) VALUES (?,?,0);",(word, num))
        self.conn.commit()
        self.end()

    def getWordByID(self, ID):
        self.start()
        self.cursor.execute("SELECT Word, Num FROM Presents WHERE ID=? ORDER BY Time", (ID,))
        word_found=self.cursor.fetchall()
        word_dict=[dict(zip(["Word","Num"],w)) for w in word_found]
        self.end()  
        return word_found
    
    def getAllPresents(self):
        self.start()
        self.cursor.execute("SELECT Word, Num, ID FROM Presents ORDER BY RANDOM()",)
        word_found=self.cursor.fetchall()
        self.end()  
        return word_found
    
    def deleteAllPresents(self):
        self.start()
        self.cursor.execute("DELETE FROM Presents",)
        self.conn.commit()
        self.end()  

    
    def repinAllWords(self):
        self.start()
        self.cursor.execute("UPDATE FullWordList SET Used=0",)
        self.conn.commit()
        self.end()


    def getRandomWord(self):
        self.start()
        self.cursor.execute("SELECT Word, Num FROM FullWordList WHERE Used=0  ORDER BY RANDOM() LIMIT 1")
        word_found=self.cursor.fetchone()
        word_dict=dict(zip(["Word","Num"],word_found))
        self.end()  
        return word_dict

    def pinNum(self, num, T=1):
        self.start()
        self.cursor.execute("UPDATE FullWordList SET Used=? WHERE Num=?",(T,num))
        self.conn.commit()
        self.end()


    def addPresent(self,word,num,id=False):
        ts = time.time()
        if not(id):
            id=self.createID()
        
        self.start()
        self.cursor.execute("INSERT OR REPLACE INTO Presents (Word,Num,ID,Time) VALUES (?,?,?,?);",(word, num, id, ts))
        self.conn.commit()
        self.end()

        
        return id
    
    def removePresentByNum(self,num):
        self.start()
        self.cursor.execute("DELETE FROM Presents WHERE Num=?",(num,))
        self.conn.commit()
        self.end()
        
        self.pinNum(num, 0)

    def createID(self):
        return str(uuid.uuid4())

    def convertCounterRegions(self,Counter_regions):
        regions=['NA','SA','EU','AF','AS','OC']
        region_list=[]
        for r in regions:
            region_list.append(Counter_regions[r])
        return region_list
    
    def searchTrack(self,Name:str):
        self.start()
        self.cursor.execute("SELECT * FROM Tracks WHERE Name=?", (Name,))
        track_found=self.cursor.fetchone()
        self.end()

        if track_found:
            names=("Name","Country","Location","Lon","Lat","Geonames","Region")
            data_dict=dict(zip(names,track_found))
            return data_dict
        else:
            return False

    def start(self):
        self.conn=sqlite3.connect(self.path)
        self.cursor=self.conn.cursor()
    def end(self):
        
        self.conn.close()


if __name__=="__main__":
    pass