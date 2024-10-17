import tkinter as tk
import math
import keyboard
import pyautogui
import time

def get_xy(xx,yy,zz):

	global wd,ht,gnd,hvar

	xx=xx*hvar
	yy=gnd+yy*hvar
	zz=zz*hvar


	cx,cy=wd/2,ht/2
	f=-550

	xx*=wd
	yy*=wd
	zz*=wd

	xx=-xx


	x=((xx*f)/(zz-f))+cx
	y=((yy*f)/(zz-f))+cy


	return x,y



def main():
	global can,ht,wd


	can.delete("all")

	draw_floor()


	xa,ya=get_xy(0,0,3)
	xb,yb=get_xy(0,1.7,3)

	can.create_line(xa,ya, xb,yb, fill="cyan")

	can.create_oval(wd/2-3,ht/2-3, wd/2+3,ht/2+3,outline="#ffffff")



def draw_floor():
	global gnd,area,loc,loc2


	tile_x,tile_y=1,1   #in meters

	


	n_xtile=area[0]/tile_x
	n_ytile=area[1]/tile_y





	yv=area[1]*loc[1]+loc2[-1]

	zst=0

	for y in range(int(n_ytile)):

		xv=-area[0]*loc[0]


		for x in range(int(n_xtile)):
			ar=[]
			a=[[0,0],[1,0],[1,1],[0,1]]

			zst=0

			


			for x_ in a:

				xx,yy,zz=rot_x(xv+x_[0]*tile_x,0,yv-x_[1]*tile_y)

				#print(xv+x_[0]*tile_x,0,yv-x_[1]*tile_y)

				_x,_y=get_xy(xx,yy,zz)

				if zz<0:
					zst=1

				ar.append(_x)
				ar.append(_y)

			#print(ar)


			c=0
			c2=0
			c3=0
			c_=1
			for _ in range(len(ar)):

				if ar[_]<0:
					c+=1

				if c_%2==0:
					if ar[_]<0:
						c2+=1

				else:
					if ar[_]<0:
						c3+=1


				c_+=1


			
			if c2==0:

				if c!=8:

					#if c3==0:



					if zst==0:


						can.create_polygon(ar,fill="#222222",outline="#666666")

			xv+=tile_x


		#if yv<0:
		#	break#
		yv-=tile_y




		l1=[0.25,0.25]

		xx=-area[0]*loc[0]+area[0]*l1[0]
		zz=area[1]*loc[1]-area[1]*l1[1]+loc2[-1]


		x1,y1,z1=rot_x(xx,0,zz)
		x2,y2,z2=rot_x(xx,1.7,zz)


		xx1,yy1=get_xy(x1,y1,z1)
		xx2,yy2=get_xy(x2,y2,z2)

		st=0

		if z1<0 or z2<0:
			st=1

		if st==0:

			can.create_line(xx1,yy1, xx2,yy2,fill="cyan")










		l1=[0.4,0.4]

		xx=-area[0]*loc[0]+area[0]*l1[0]
		zz=area[1]*loc[1]-area[1]*l1[1]+loc2[-1]

		x1,y1,z1=rot_x(xx,0,zz)
		x2,y2,z2=rot_x(xx,1.7,zz)


		xx1,yy1=get_xy(x1,y1,z1)
		xx2,yy2=get_xy(x2,y2,z2)

		st=0

		if z1<0 or z2<0:
			st=1

		if st==0:

			can.create_line(xx1,yy1, xx2,yy2,fill="red")




def rot_x(x,y,z):

	global loc,loc2,x_ang


	#print(x,y,z)


	



	r=math.sqrt((x-0)**2+(z-3)**2)

	#print(r)

	vv="#ffffff"


	if x<=0 and z>3:

		

		o=0-x
		h=r


		try:
			v=o/h
		except:
			v=0

		ang=math.asin(v)


		ang=math.degrees(ang)+180+x_ang




		x_=r*math.sin(math.radians(ang))+0
		z_=-r*math.cos(math.radians(ang))+3


		



		#print("xxx",x_,y,z_)


		

		vv="red"


	if x>0 and z>=3:
		o=z-3
		h=r


		try:
			v=o/h
		except:
			v=0

		ang=math.asin(v)

		ang=math.degrees(ang)+90+x_ang


		x_=r*math.sin(math.radians(ang))+0
		z_=-r*math.cos(math.radians(ang))+3



		vv="yellow"

	if x>=0 and z<3:
		o=x-0
		h=r


		try:
			v=o/h
		except:
			v=0

		ang=math.asin(v)

		ang=math.degrees(ang)+x_ang

		x_=r*math.sin(math.radians(ang))+0
		z_=-r*math.cos(math.radians(ang))+3



		vv="green"

	if x<0 and z<=3:

		o=3-z
		h=r




		try:
			v=o/h
		except:
			v=0

		ang=math.asin(v)

		ang=math.degrees(ang)+270+x_ang

		x_=r*math.sin(math.radians(ang))+0
		z_=-r*math.cos(math.radians(ang))+3



		vv="blue"

	if x==0 and z==3:
		ang=0



		x_=r*math.sin(math.radians(ang))+0
		z_=-r*math.cos(math.radians(ang))+3

	

	

	#print(ang)








	return x_,y,z_



def check_keys():

	global x_ang, y_ang,area,loc


	"""

	if keyboard.is_pressed('left'):
		x_ang-=5
		main()
	if keyboard.is_pressed('right'):
		x_ang+=5
		main()
	if keyboard.is_pressed('up'):
		print("up")
	if keyboard.is_pressed('down'):
		print("down")	

	"""

	if keyboard.is_pressed('w') or keyboard.is_pressed('W'):


		if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
			x_ang+=5


		elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):
			x_ang-=5


		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang))
		y=v*math.cos(math.radians(180+x_ang))

		loc[0]-=x
		loc[1]+=y

		time.sleep(0.01)

		main()


	elif keyboard.is_pressed('s') or keyboard.is_pressed('S'):


		if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
			x_ang+=5


		elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):
			x_ang-=5



		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang+180))
		y=v*math.cos(math.radians(180+x_ang+180))

		loc[0]-=x
		loc[1]+=y


		time.sleep(0.01)

		main()

	elif keyboard.is_pressed("d") or keyboard.is_pressed("D"):
		x_ang+=5

		main()


	elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):
		x_ang-=5

		main()
	root.after(10,check_keys)	


root=tk.Tk()
wd=int(root.winfo_screenwidth())
ht=int(root.winfo_screenheight())

root.wm_attributes("-fullscreen",1)




gnd=-ht/2
hvar=-gnd/2
area=[20,20]#in meters

loc=[0.5,0.5]
loc2=[0,0,3]

x_ang=0
y_ang=0

def mouse_motion():
	global motionx,motiony,x_ang,y_ang


	currentMouseX, currentMouseY = pyautogui.position()


	if currentMouseX>motionx:
		x_ang+=15
		pyautogui.moveTo(wd/2, ht/2)
		main()
	elif currentMouseX<motionx:
		x_ang-=15
		pyautogui.moveTo(wd/2, ht/2)

		main()



	


	root.after(10,mouse_motion)


motionx,motiony=wd/2,ht/2
can=tk.Canvas(width=wd,height=ht,relief="flat",highlightthickness=0,border=0,bg="#000000",cursor="none")
can.place(in_=root,x=0,y=0)



main()

check_keys()
mouse_motion()
root.mainloop()