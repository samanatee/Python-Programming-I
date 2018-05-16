'''
Created on May 14, 2018

@author: Samantha Hangsan

create Calculator application using OOP GUI principles
'''
from tkinter import Tk, Frame, Button, RAISED, RIDGE, Entry, END
from functools import partial


class Calculator(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)	# Widget Frame – house the keys and the entry field in a grid
		parent.title('Calculator')
		self.pack()

		# Widget Entry – displays what expression is calculated and the result of calculation.
			# When calculator application starts, the field displays value 0. 
			# When user clicks ‘AC’, the field is reset and displays 0. 
			# When user clicks on the calculator keys, the full expression that is calculated should be displayed:
		self.entry = Entry(self, relief = RIDGE, borderwidth = 3,
				width = 20, bg = 'gray', font = ('Helvetica', 18))
		self.entry.insert(END, '0')
		self.entry.grid(row = 0, column = 0, columnspan = 4, sticky = 'nsew')
		self.expr = ''
		self.startOfNextOperand = True

		# Widget Button: represents the calculator keys. 
			# When user clicks on keys, the key text should appear in the entry field
			# When user clicks ‘=’, the field shows the result of calculation
		button_labels = [['AC', '%', '/'],
						 ['7', '8', '9', '*'],
						 ['4', '5', '6', '-'],
						 ['1', '2', '3', '+'],
						 ['0', '.', '=']]

		for r in range(5):
			for c in range(4):
				if (r == 0 or r == 4):
					if (c == 0):
						x = button_labels[r][c]
						self.button = Button(self, text = button_labels[r][c],
							width = 14, height = 3, relief = RAISED, command = partial(self.click_command,x))
						self.button.grid(row = r + 1, column = c, columnspan = 2, sticky = 'nsew')
					else: 
						try: 
							x = button_labels[r][c]
							self.button = Button(self, text = button_labels[r][c],
								width = 7, height = 3, relief = RAISED, command = partial(self.click_command,x))
							self.button.grid(row = r + 1, column = c + 1, sticky = 'nsew')
		
						except IndexError:
							break
				else:
					x = button_labels[r][c]
					self.button = Button(self, text = button_labels[r][c],
						width = 7, height = 3, relief = RAISED, command = partial(self.click_command,x))
					self.button.grid(row = r + 1, column = c, sticky = 'nsew')


	def click_command(self, key):
		if (key == '='): 
			# evaluate expression and display result
			try: 
				result = eval(self.expr)
				self.expr = str(result)
				self.entry.delete(0, END)
				self.entry.insert(END, result)
				self.startOfNextOperand = True
			except: 
				self.entry.delete(0, END)
				self.entry.insert(END, 'Error')
		elif (key in '+*-/%'):
			self.expr += key
			self.entry.insert(END, key)
			self.startOfNextOperand = False
		elif (key == 'AC'):
			self.entry.delete(0, END)
			self.entry.insert(END, '0')
			self.startOfNextOperand = True
			self.expr = ''
		else:
			if self.startOfNextOperand:
				self.expr = ''
				self.entry.delete(0, END)
				self.startOfNextOperand = False
			self.expr += key
			self.entry.insert(END, key) 
		
def main():
	root = Tk()
	Calculator(root)
	root.mainloop()

if __name__ == '__main__':
	main()


