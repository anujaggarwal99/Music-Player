from pygame import *
import glob
from PIL import ImageTk
import PIL.Image
import sys
#sys.path.append('C:/Users/naveen/Desktop/ada')
pause = True

mixer.init()
l = glob.glob('F:/project/ada/*.ogg')
song_list = []
time_list = [567, 448, 355, 515, 405, 412, 470, 468, 523]
red = '#%02x%02x%02x' % (255,8,0)



for i in range(len(l)) : 
    song_list.append(l[i][l[i].index('\\')+1:])
#print(song_list)
#print()

dictionary = dict(zip(time_list, song_list))
print("\n\n\n",dictionary)

slist = list(dictionary.values())
tlist = list(dictionary.keys())
#print(tlist)



#print(list(dictionary.values()))
#print(len(dictionary))

def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
 
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
 


import copy
sorted_song_list = copy.deepcopy(slist)



merge_sort(sorted_song_list, 0, len(sorted_song_list))
#print('\n\n\n',sorted_song_list)
final_list = copy.deepcopy(sorted_song_list)
 



from tkinter import Tk,Label,Canvas,Button,Toplevel,Entry
top = Tk()
top.geometry('600x600')
top.title('Player')
top.resizable(False,False)
top.configure(bg = 'black')


mixer.music.load(final_list[0])
mixer.music.play()
index = 0



pause = False
'''def playpause(event) :
    global pause,play_button
    if pause == False :
        pause = True
        mixer.music.pause()
        play_button.config(text = ' ► ')
    elif pause == True :
        mixer.music.unpause()
        pause = False
        play_button.config(text = '  ▌▌')
#top.bind("<space>",playpause) '''


def play_pause() :
    global pause,play_button
    if pause == False :
        pause = True
        mixer.music.pause()
        play_button.config(text = ' ► ')
    elif pause == True :
        mixer.music.unpause()
        pause = False
        play_button.config(text = '  ▌▌')


m = '#%02x%02x%02x' % (0,162,232)
play_button = Button(top, text = '  ▌▌',bg = 'black',foreground = 'purple',width = 4,activebackground = 'black',activeforeground=m,borderwidth=0 ,font=('times new roman',20),command = play_pause)
play_button.pack()
play_button.place(x=250,y=546)




#top.bind("n",nextsong)
tex= None
def next_song() :
    global index,pause,tex
    index += 1
    if index == len(song_list) :
        index = 0
    if index < len(song_list) :
        mixer.music.load(song_list[index])
        mixer.music.stop()
        mixer.music.play()
        pause = False
        play_button.config(text = ' ▌▌')
        tex = 'Playing : '+final_list[index][:-4]
        playing_label.config(text = tex)
        
    

next_button = Button(top,text='⏭',bg = 'black',foreground='purple',width=4,activebackground = 'black',activeforeground=m, borderwidth = 0,font = ('times new roman',20),command = next_song)
next_button.pack()
next_button.place(y = 546, x = 300)



def prev_song() :
    global index,pause,tex
    
    index -= 1
    if index < 0 :
        index = 8
    if index >= 0 :
        mixer.music.load(song_list[index])
        mixer.music.stop()
        mixer.music.play()
        pause = False
        play_button.config(text = ' ▌▌')
        tex = 'Playing : '+final_list[index][:-4]
        playing_label.config(text = tex)
    '''else :
        index += 1
        print('first song')'''


prev_button = Button(top,text='⏮',bg = 'black',foreground='purple',width=4,activebackground = 'black',activeforeground=m, borderwidth = 0,font = ('times new roman',20),command = prev_song)
prev_button.pack()
prev_button.place(y = 546, x = 200)

#top.bind('p',prevsong)
#top.bind('b',prevsong)



def searchsong() :
    w4 = Toplevel(bg = 'black')
    w4.title('Search Results')
    w4.geometry('450x380')
    w4.resizable(False,False)
    searchlabel = Label(w4,text = 'Search Results',font = ('moon',40,'bold'),bg='black',foreground=red)
    searchlabel.pack()

    def playsearchsong(playindex,newlist) :
        global index
        global pause
        pause = False
        play_button.config(text = ' ▌▌')
            
        print(index)
        for i in final_list :
            if newlist[playindex] in i :
                index = final_list.index(i)
        mixer.music.stop()
        mixer.music.load(final_list[index])
        mixer.music.play()
        playing_label.config(text = 'Playing : '+final_list[index][:-4])

    def search(word,song) :
        word = word.upper()
        ind = []
        for i in song :
            j = i[:-4].upper()
            if word in j :
                ind.append(song.index(i))
                print(i)

        return(ind)
    searchlist = search(search_entry.get(),final_list)
    xsum = 10
    ysum = 120
    newlist = []
    print(searchlist)
    for i in searchlist :
        newlist.append(final_list[i])
    if len(newlist)  == 0 :
        no = Label(w4,text = ' No\nResults\nFound',font = ('moon',30),bg='black',foreground=m)
        no.pack()
        no.place(y = 120, x = 150)

    else:

        bnew = []
        for i in range(len(newlist)) :
            bnew.append(Button(w4,text = newlist[i][:-4],bg = 'black',foreground = 'purple', activebackground = 'black',font = ('moon',13),activeforeground = m,command=lambda x=i: playsearchsong(x,newlist)))
        for i in bnew :
            i.pack()
            if ysum >= 330 :
                ysum = 120
                xsum = 220
            
            i.place(x=xsum,y=ysum)
            
            ysum +=50
        print(ysum)
    


    
    
    


def callback1(event) :
    
     if 'search... .. .' in search_entry.get() :
        print('yes')
        search_entry.delete(0,END)


heading = Label(top,bg ='black',foreground = red,text = 'Music Player',font = ('moon',40,'bold'))
heading.pack()
heading.place(x = 100,y = 20)


search_entry = Entry(top,bg = 'black',foreground=m,insertbackground = 'white',highlightcolor = 'purple',highlightthickness=1)
search_entry.insert(0,'search... .. .')
search_entry.pack()
search_entry.place(x = 440,y =2)
search_entry.bind('<Button-1>',callback1)
print(search_entry.get())

search_button = Button(top,bg = 'black',foreground = 'purple', activebackground = 'black',text = '⏎',font = ('moon',13),activeforeground = m,borderwidth = 0,command = searchsong)
search_button.pack()
search_button.place(x = 570)

im = PIL.Image.open("music.png")
pic = ImageTk.PhotoImage(im)

can = Canvas(top,width = 400, height = 400,highlightthickness=0)
can.pack()
can.place(x=105,y=80)
can.create_image(202,195,image=pic)



#img_label = Label(top)
#img_label.img = PhotoImage(file='music.png')
#img_label.config(image=img_label.img)
#img_label.pack()





playing_label = Label(top,text = ' Playing : Abhi Abhi',font=('moon',20),bg ='black',foreground = m)
playing_label.pack()
playing_label.place(y = 500,x = 120)

def printknapSack(W, wt, val, n): 
    K = [[0 for w in range(W + 1)] 
        for i in range(n + 1)] 

 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1]  + K[i - 1][w - wt[i - 1]],  K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 

    res1 = []
    res = K[n][W]


    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break

        if res == K[i - 1][w]: 
            continue
        else: 




            res1.append(wt[i-1])

            res = res - val[i - 1] 
            w = w - wt[i - 1]
    return(res1)


def disable_event(w2) :
    mixer.music.stop()
    mixer.music.load(final_list[index])
    mixer.music.play()
    w2.destroy()
    playing_label.config(text = "Playing : "+final_list[index][:-4])
    print('na')

def juke_box() :
    w2 = Toplevel(bg = 'black')
    w2.title('Jukebox')
    w2.geometry('600x400')
    w2.resizable(False,False)
    jukelabel = Label(w2,text = 'Jukebox',font = ('moon',40),bg='black',foreground=red)
    jukelabel.pack()
    timelabel = Label(w2,text = 'Time',font = ('moon',20),bg='black',foreground=m)
    timelabel.pack()
    timelabel.place(x=40,y=70)
    timeentry = Entry(w2,bg = 'black',foreground=m,insertbackground = 'white',highlightcolor = 'purple',highlightthickness=1)
    timeentry.insert(0,'Enter Time')
    timeentry.pack()
    timeentry.place(x=115,y=76)
    def callback2(event) :
     if 'Enter Time' in timeentry.get() :
        print('yes')
        timeentry.delete(0,END)
    timeentry.bind('<Button-1>',callback2)
    number = []
    newlist = []
    def knap() :
        t = int(timeentry.get())
        t = t*100
        val = [1]*9
        wt = copy.deepcopy(time_list)
        n = len(val)
        x = printknapSack(t, wt, val, n)
        
       
        for i in x :
           number.append(wt.index(i))
        for i in number :
            newlist.append(final_list[i])
        xsum = 10
        ysum = 120

        def playjuke(jukeindex) :
            global pause
            pause = False
            play_button.config(text = ' ▌▌')
            print(jukeindex)
            mixer.music.stop()
            mixer.music.load(newlist[jukeindex])
            mixer.music.play()
            playing_label.config(text = 'Playing : '+newlist[jukeindex][:-4])

        newlist.sort(reverse = True)
        bnew = []
        for i in range(len(newlist)) :
            bnew.append(Button(w2,text = newlist[i][:-4],bg = 'black',foreground = 'purple', activebackground = 'black',font = ('moon',13),activeforeground = m,command=lambda x=i: playjuke(x)))
        for i in bnew :
            i.pack()
            if ysum >= 330 :
                ysum = 120
                xsum = 330
            
            i.place(x=xsum,y=ysum)
            
            ysum +=50
        print(ysum)
                    
        

    createbutton = Button(w2,text = 'Create',bg = 'black',foreground = 'purple', activebackground = 'black',font = ('moon',13),activeforeground = m,command=knap)
    createbutton.pack()
    createbutton.place(y=360,x=200)

    w2.protocol("WM_DELETE_WINDOW",lambda :  disable_event(w2))

juke = Button(top,text = 'Jukebox',bg = 'black',foreground = 'purple', activebackground = 'black',font = ('moon',13),activeforeground = m,borderwidth = 0,command = juke_box)
juke.pack()
juke.place(x=440,y=555)



def playlist() :
    w3 = Toplevel(bg = 'black')
    w3.title('Playlist')
    w3.geometry('600x400')
    w3.resizable(False,False)
    playlabel = Label(w3,text = 'Playlist',font = ('moon',40,'bold'),bg='black',foreground=red)
    playlabel.pack()

    xsum = 10
    ysum = 120

    def playplaylist(playindex) :
        global index
        global pause
        pause = False
        play_button.config(text = ' ▌▌')
        print(index)
        index = playindex
        mixer.music.stop()
        mixer.music.load(final_list[index])
        mixer.music.play()
        playing_label.config(text = 'Playing : '+final_list[index][:-4])

    bnew = []
    for i in range(len(final_list)) :
        bnew.append(Button(w3,text = final_list[i][:-4],bg = 'black',foreground = 'purple', activebackground = 'black',font = ('moon',13),activeforeground = m,command=lambda x=i: playplaylist(x)))
    for i in bnew :
        i.pack()
        if ysum >= 330 :
            ysum = 120
            xsum = 310
        
        i.place(x=xsum,y=ysum)
        
        ysum +=50
    print(ysum)


playlistbutton = Button(top,text = 'Playlist',bg='black',foreground = 'purple', activebackground = 'black',font = ('moon',13),activeforeground = m,borderwidth = 0,command = playlist)
playlistbutton.pack()
playlistbutton.place(x = 100,y=555)




top.mainloop()
mixer.music.stop()
