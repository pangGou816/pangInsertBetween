import pyperclip

import sys

import tkinter as tk
from tkinter import messagebox

def widgets() -> None:
   textLabel = tk.Label(
      root,
      text='Text: ',
      font='System 22',
      bg='DarkSlateBlue',
      padx=5,
      pady=5
   )
   textLabel.grid(
      row=0,
      column=0,
      padx=5,
      pady=5
   )
   textText = tk.Text(
      root,
      width=41,
      height=11,
      font='System 22'
   )
   textText.grid(
      row=0,
      column=1,
      padx=5,
      pady=5,
      columnspan=3
   )

   keyLabel = tk.Label(
      root,
      text='Key: ',
      font='System 22',
      bg='DarkSlateBlue',
      padx=1,
      pady=1
   )
   keyLabel.grid(
      row=3,
      column=1,
      padx=1,
      pady=1,
      sticky='e'
   )
   keyText = tk.Entry(
      root,
      textvariable=key,
      width=3,
      font='System 22',
      justify='center'
   )
   keyText.grid(
      row=3,
      column=2,
      padx=5,
      pady=5,
      sticky='w'
   )

   convertBut = tk.Button(
      root,
      text='Convert',
      font='System 22',
      bg='SlateGrey',
      command=lambda: convert( textText )
   )
   convertBut.grid(
      row=3,
      column=3,
      padx=5,
      pady=5,
      sticky='w'
   )

def convert( tkText ) -> None:
   text = tkText.get( '1.0', 'end-1c' )
   outText = ''

   for c in text:
      outText += c + key.get()

   pyperclip.copy( outText[:-1] )

   messagebox.showinfo( 'Success', 'Copied' )

if __name__ == '__main__':
   root = tk.Tk()

   root.geometry( '800x450' )
   root.resizable( False, False )
   root.title( 'spaceBetween' )
   root.config( background='DarkSlateBlue' )

   key = tk.StringVar()

   widgets()

   sys.exit( root.mainloop() )