def clear_window(window):
	window.configure(background="white") 
	for child in window.winfo_children():
		child.destroy()