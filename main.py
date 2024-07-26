import pyperclip

import sys

import tkinter as tk
from tkinter import messagebox

def widgets() -> None:
   linkLabel = tk.Label(
      root,
      text='Text: ',
      font='System 22',
      bg='DarkSlateBlue',
      padx=5,
      pady=5
   )
   linkLabel.grid(
      row=0,
      column=0,
      padx=5,
      pady=5
   )
   linkText = tk.Text(
      root,
      width=41,
      height=11,
      font='System 22'
   )
   linkText.grid(
      row=0,
      column=1,
      padx=5,
      pady=5,
   )

   convertBut = tk.Button(
      root,
      text='Convert',
      font='System 22',
      bg='SlateGrey',
      command=lambda: convert( linkText )
   )
   convertBut.grid(
      row=3,
      column=0,
      padx=5,
      pady=5,
      columnspan=7
   )

def convert( tkText ) -> None:
   text = tkText.get( '1.0', 'end-1c' )
   outText = ''

   for c in text:
      outText += c + ' '

   pyperclip.copy( outText[:-1] )

   messagebox.showinfo( 'Success', 'Copied' )

if __name__ == '__main__':
   root = tk.Tk()

   root.geometry( '800x450' )
   root.resizable( False, False )
   root.title( 'spaceBetween' )
   root.config( background='DarkSlateBlue' )

   widgets()

   sys.exit( root.mainloop() )