from bs4 import BeautifulSoup
import requests
import json
import tkinter
from tkinter import *

class GUI:

        
        
    def __init__(self, master):
        global gui
        gui = master
        self.master = master
        master.title ("Webscraper")
        Label(master, text="Logan Selley ez webscraper").grid(row=0)
        Label(master, text="url:").grid(row=2)
        Label(master, text="html tag:").grid(row=3)
        Label(master, text="secondary tags (separate with spaces):").grid(row=4)
        Label(master, text="css class?:").grid(row=5)
        Label(master, text="secondary css classes? (separate with spaces):").grid(row=6)
        
        url = StringVar()
        html = StringVar()
        html2 = StringVar()
        css = StringVar()
        css2 = StringVar()
        e1 = Entry(master, textvariable=url)
        root.grid_rowconfigure(1, minsize=20)
        e1.grid(row=2, column=1)
        e2 = Entry(master, textvariable=html)
        e2.grid(row=3, column=1)
        e3 = Entry(master, textvariable=html2)
        e3.grid(row=4, column=1)
        e4 = Entry(master, textvariable=css)
        e4.grid(row=5, column=1)
        root.grid_rowconfigure(7, minsize=20)
        e5 = Entry(master, textvariable=css2)
        e5.grid(row=6, column=1)
        b = Button(master, text='excecute', command=lambda: scrape(url, html, html2, css, css2))
        b.grid(row=8)
        
        
def scrape(url, tag, tag2, css, css2):
    print(url.get() + " 1 " + " 2 " + tag.get() + " 3 " + css.get() + " " + tag2.get() + " " + css2.get())
    if url.get() == "":
        print("valid url required, include http://")
    else:
        response = requests.get(url.get(), timeout=5)
        content = BeautifulSoup(response.text, "html.parser")
        print(str(content.find_all("button", id_="readable")))
        Arr = {}
        secondaryTags = tag2.get().split(" ")
        secondaryCSS = css2.get().split(" ")
        if len(secondaryTags) > len(secondaryCSS):
            while len(secondaryTags) != len(secondaryCSS):
                secondaryCSS.append("")
        elif len(secondaryCSS) > len(secondaryTags):
            while len(secondaryTags) != len(secondaryCSS):
                del secondaryCSS[-1]
        if tag.get() == "":
            if css.get() != "":
                Arr['class'] = content.find(class_=css.get()).text
            else:
                Arr['html'] = content.text
        else:
            Arr['data'] = []
            if css.get() == "":
                for item in content.find_all(tag.get()):
                    print(item.text)
                    if not secondaryTags:
                        if secondaryCSS:
                            # tags and css
                            for position in range(len(secondaryTags)):
                                Arr[secondaryTags[position].text] = item.find(secondaryTags[position], attrs={"class":secondaryCSS[position]}).text
                                
                        else:
                            #just tags
                            for position in range(len(secondaryTags)):
                                Arr[secondaryTags[position].text] = item.find(secondaryTags[position]).text
                            
                    else:
                        Arr['data'].append(item.text)
                    
            else:
                for item in content.find_all(tag.get(), attrs={"class": css.get()}):
                    if secondaryTags:
                        if secondaryCSS:
                            # tags and css
                            for position in range(len(secondaryTags)):
                                Arr[secondaryTags[position].text] = item.find(secondaryTags[position], attrs={"class":secondaryCSS[position]}).text
                            
                        else:
                            #just tags
                            for position in range(len(secondaryTags)):
                                Arr[secondaryTags[position].text] = item.find(secondaryTags[position]).text
                            
                    else:
                        Arr['data'].append(item.text)
        print(Arr)
        with open('data.json', 'w') as outfile:
            json.dump(Arr, outfile)
            

root = Tk()
my_gui = GUI(root)
root.mainloop()

    