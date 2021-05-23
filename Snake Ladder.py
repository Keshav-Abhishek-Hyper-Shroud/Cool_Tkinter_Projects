# Importing required libraries
from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title('Snake Ladder Game')
root.resizable(height=False,width=False)

# Setting Title Using Label
title_label=Label(root,text='Snake Ladder Game',font='times 50 bold',bg='cyan')
title_label.pack(pady=10)

# Frames for Numbers 1 to 100
label_frame=Frame(root)
label_frame.pack()

# Managing the sequence of number
num_collection=[]
for y in range(100,0,-10):
	num_collection.append([xx for xx in range(y,y-10,-1)])

num_collection[1]=num_collection[1][::-1]
num_collection[3]=num_collection[3][::-1]
num_collection[5]=num_collection[5][::-1]
num_collection[7]=num_collection[7][::-1]
num_collection[9]=num_collection[9][::-1]

# Plotting Buttons
label_list=[]
i,j=0,0
for x in num_collection:
	for t in x:
		k=Label(label_frame,text=f'{t}',font='times 25 bold',bd=5,width=3,height=1)
		if j==10:
			j=0
			i+=1
		k.grid(row=i,column=j)
		j+=1

		label_list.append(k)

# Snaked or Not
for_tally=label_list.copy()

# Removing some snaked area
for i in label_list:
	if i.cget('text')=='100' or i.cget('text')=='1':
		label_list.remove(i)

# Defining snake's home
random_spot=[];num_spot=[]
for i in range(5):
	got=random.choice(label_list)
	random_spot.append(got)
	label_list.remove(got)

# Tracking snake's home
for i in random_spot:
	i['bg']='red'
	num_spot.append(int(i['text']))

# Controller Window
controller=Toplevel()
controller.title('Snake Ladder - Controller')
controller.resizable(height=False,width=False)

# Point Markers
player_1_score_value=0
player_2_score_value=0

# Runs when player 1 rolls the die
def rolledby1():
	global player_1_score_value,num_spot
	dice_label['text']=f'{random.randint(1,6)}'
	if dice_label.cget('text')=='1':
		player_1['bg']='lightgreen'
	
	if player_1['bg']=='lightgreen' and player_1_score_value+int(dice_label.cget('text'))<=100:
		player_1_score_value+=int(dice_label.cget('text'))
		bite_1=0
		while player_1_score_value in num_spot:
			player_1_score_value=random.randint(1,player_1_score_value)
			bite_1=1
		if bite_1!=0:
			player_2['state']=DISABLED
			player_1['state']=DISABLED
			messagebox.showwarning('Oops!','Snake bite you! Be careful Player 1.')
			player_2['state']=NORMAL
			player_1['state']=NORMAL
		player_1_score['text']=f'You are on {player_1_score_value}'
		if player_1_score['text'].split(' ')[-1]=='100':
			messagebox.showinfo('Hurry!','Player 1 Won!!')
			controller.destroy()
			root.destroy()

	player_1['state']=DISABLED
	player_2['state']=NORMAL

# Runs when player 2 rolls the die
def rolledby2():
	global player_2_score_value,num_spot
	dice_label['text']=f'{random.randint(1,6)}'
	if dice_label.cget('text')=='1':
		player_2['bg']='cyan'

	if player_2['bg']=='cyan' and player_2_score_value+int(dice_label.cget('text'))<=100:
		player_2_score_value+=int(dice_label.cget('text'))
		bite_2=0
		while player_2_score_value in num_spot:
			player_2_score_value=random.randint(1,player_2_score_value)
			bite_2=1
		if bite_2!=0:
			player_2['state']=DISABLED
			player_1['state']=DISABLED
			messagebox.showwarning('Oops!','Snake bite you! Be careful Player 2.')
			player_2['state']=NORMAL
			player_1['state']=NORMAL
		player_2_score['text']=f'You are on {player_2_score_value}'
		if player_2_score['text'].split(' ')[-1]=='100':
			messagebox.showinfo('Hurry!','Player 2 Won!!')
			controller.destroy()
			root.destroy()

	player_2['state']=DISABLED
	player_1['state']=NORMAL

# Dice
dice_label=Label(controller,text=f'{random.randint(1,6)}',font='times 30 bold')
dice_label.pack(fill=X,pady=20)

# Handles Controller Buttons
player_frame=Frame(controller)
player_frame.pack(fill=X)

# Button for players to play
player_1=Button(player_frame,text='Player 1: Roll the Die',font='times 15 bold',command=rolledby1)
player_1.grid(row=0,column=0)

# Point Shower
player_1_score=Label(player_frame,text=f'You are on {player_1_score_value}',font='times 15 bold')
player_1_score.grid(row=0,column=1)

# Point Shower
player_2_score=Label(player_frame,text=f'You are on {player_2_score_value}',font='times 15 bold')
player_2_score.grid(row=1,column=1)

# Button for players to play
player_2=Button(player_frame,text='Player 2 : Roll the Die',font='times 15 bold',command=rolledby2)
player_2.grid(row=1,column=0)
root.mainloop()