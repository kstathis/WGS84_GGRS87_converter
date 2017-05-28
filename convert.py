import Tkinter
from pyproj import Proj, transform
import pyperclip
import webbrowser


# create a window object
mywindow = Tkinter.Tk()
mywindow.title("WGS84 <--> GGRS87 Converter")

#---------------------------------------------------------------------------------------------------WGS84

# WGS84 label
wgs84_label = Tkinter.Label(mywindow, text="WGS84 ( lat,lon ) in dd.dddd")
wgs84_label.config(font=(None, 12))
wgs84_label.grid(row=0, column=0)

# WGS84 entry
wgs84_entry = Tkinter.Entry(mywindow, width=35)
wgs84_entry.config(font=(None, 12))
wgs84_entry.grid(row=1, column=0)

# WGS84 entry clear function
def wgs84_clear():
 wgs84_entry.delete(0, 'end')
 error_label["text"] = ""

# WGS84 clear button
wgs84_clear_btn = Tkinter.Button(mywindow, text="Clear entry", fg="blue", command=wgs84_clear)
wgs84_clear_btn.grid(row=1, column=1)

# WGS84 copy to clipboard function
def wgs84_clip():
 pyperclip.copy(wgs84_entry.get())

# WGS84 copy to clipboard button  
wgs84_clip_btn = Tkinter.Button(mywindow, text="to Clipboard", fg="#009b7e", command=wgs84_clip)
wgs84_clip_btn.grid(row=1, column=2)

# WGS84 show point in Google Maps function
def wgs84_browser():
 coord_link = wgs84_entry.get()
 coord_link = coord_link.split(",")
 coord_link = list(coord_link)
 coord_link = str(coord_link[0]) + "," + str(coord_link[1])
 
 webbrowser.open('https://www.google.com/maps?q=' + coord_link, new = 2)

# WGS84 show point in Google Maps button  
wgs84_browser_btn = Tkinter.Button(mywindow, text="to Browser", fg="#8d0736", command=wgs84_browser)
wgs84_browser_btn.grid(row=1, column=3)

#---------------------------------------------------------------------------------------------------GGRS87

# GGRS87 label
ggrs87_label = Tkinter.Label(mywindow, text="GGRS87 ( x,y )")
ggrs87_label.config(font=(None, 12))
ggrs87_label.grid(row=2, column=0)

# GGRS87 entry
ggrs87_entry = Tkinter.Entry(mywindow, width=35)
ggrs87_entry.config(font=(None, 12))
ggrs87_entry.grid(row=3, column=0)

# GGRS87 clear entry function
def ggrs87_clear():
 ggrs87_entry.delete(0, 'end')
 error_label["text"] = ""

# GGRS87 clear button
ggrs87_clear_btn = Tkinter.Button(mywindow, text="Clear entry", fg="blue", command=ggrs87_clear)
ggrs87_clear_btn.grid(row=3, column=1)

# GGRS87 copy to clipboard function
def ggrs87_clip():
 pyperclip.copy(ggrs87_entry.get())

# GGRS87 copy to clipboard button  
ggrs87_clip_btn = Tkinter.Button(mywindow, text="to Clipboard", fg="#009b7e", command=ggrs87_clip)
ggrs87_clip_btn.grid(row=3, column=2)

# error display label
error_label = Tkinter.Label(mywindow, text="")
error_label.grid(row=4, column=0)

# the function of converting
def cconvert():

 wgs84_user = wgs84_entry.get()
 ggrs87_user = ggrs87_entry.get()
 
 wgs84_list = wgs84_user.split(",")
 ggrs87_list = ggrs87_user.split(",")
 
 wgs84 = Proj(init='epsg:4326') # WGS84 in EPSG Geodetic Parameter Dataset
 ggrs87 = Proj(init='epsg:2100') # GGRS87 in EPSG Geodetic Parameter Dataset
 
 if (wgs84_user and len(ggrs87_user) == 0):
  answer = transform(wgs84, ggrs87, wgs84_list[1], wgs84_list[0])
  answer = list(answer)
  answer = str(answer[0]) + "," + str(answer[1])
  ggrs87_entry.insert(0,answer)

 elif (ggrs87_user and len(wgs84_user) == 0):
  answer = transform(ggrs87, wgs84, ggrs87_list[0], ggrs87_list[1])
  answer = list(answer)
  answer = str(answer[1]) + "," + str(answer[0])
  wgs84_entry.insert(0,answer)

 else :
  error_label["text"] = "Enter valid data in only one input..."
 
# test coordinates
# 36.9642095,21.6605704   =   291582.631273,4093170.96185


# convert button
convert_btn = Tkinter.Button(mywindow, text="Convert", fg="green", command=cconvert)
convert_btn.config(font=(None, 30))
convert_btn.grid(row=5, column=0)

# close window button
close_btn = Tkinter.Button(mywindow, text="Close app", fg="red", command=mywindow.quit)
close_btn.grid(row=5, column=2)


# main events loop
mywindow.mainloop()
mywindow.destroy()




'''
Prerequisities
--------------
sudo apt-get install python-tk
sudo apt-get install python-pyproj
sudo apt-get install python-pyperclip

'''




