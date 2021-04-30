import dictionary #import dictionary identifying the anagrams
from tkinter import * #for UI

def findAnagrams():
    word = e1.get()
    word = word.lower()
    anagrams = []
    rearranged_word = sorted(word)
    rearranged_word = "".join(rearranged_word)
    for item in dictionary.words:
        if len(word) == len(item):
            rearranged_item = sorted(item)
            rearranged_item = "".join(rearranged_item)
            if rearranged_word == rearranged_item :
                anagrams.append(item)
    for i in range(len(anagrams)):
        w = Text(master, width=10, height=2)
        text.set("Anagrams are : ")
        w.grid(row=i+5, column = 1)
        w.insert(END, anagrams[i])


master = Tk()
text = StringVar()
result=Label(master, text="", textvariable=text).grid(row=3,column=1, sticky=W)
Label(master, text="Enter a word to find its anagram: ").grid(row=0, sticky=W)
e1 = Entry(master)
 
e1.grid(row=0, column=1)
 
b = Button(master, text="Show", command=findAnagrams)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
mainloop()