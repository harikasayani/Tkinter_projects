from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.geometry("600x400")
window.title("Text Editor")
def openfile():
    filepath=askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    else:
        txt.delete(1.0,END)
        with open(filepath,'r') as f:
            b=f.read()
            txt.insert(END,b)
            window.title(filepath)
def saveasfile():
    filepath1=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    with open(filepath1,'w') as s:
        b1=txt.get(1.0,END)
        s.write(b1)
        window.title(filepath1)

txt=Text(window)
txt.grid(row=0,column=1)
frame=Frame(window,width=100)
frame.grid(row=0,column=0,sticky="ns")
bt1=Button(frame,text="open",fg="red",command=openfile)
bt2=Button(frame,text="save as",fg="green",command=saveasfile)
bt1.grid(row=0,column=0,padx=10,pady=10,ipadx=10)
bt2.grid(row=1,column=0,padx=10,pady=10,ipadx=6)
mainloop()
