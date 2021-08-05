import tkinter as tk
import tkinter.font as tkfont


new_password = ""
click_enter = 0
successful = 0
newPasswordLabel = 0


def encryptPassword(event):
	global new_password
	global click_enter
	global successful
	global newPasswordLabel

	file = open('password.txt', 'a')
	passwordName = enterPasswordName.get()
	password = enterPassword.get()

	if click_enter == 1:
		successful.destroy()
		newPasswordLabel.destroy()
		

	for i in range(len(password)):
		if password[i] == 'a' or password[i] == 'A':
			new_password += '&'

		elif password[i] == 'e' or password[i] == 'E':
			new_password += '3'

		elif password[i] == '3':
			new_password += 'E'

		elif password[i] == 'i' or password[i] == 'I':
			new_password += '%'

		elif password[i] == 'o' or password[i] == 'O':
			new_password += '0'

		elif password[i] == 'x' or password[i] == 'X':
			new_password += '*'

		elif password[i] == 's' or password[i] == 'S':
			new_password += '5'

		elif password[i] == 'z' or password[i] == 'Z':
			new_password += '2'

		elif password[i] == 'l' or password[i] == 'L':
			new_password += '7'

		elif password[i] == 'b' or password[i] == 'B':
			new_password += '8'

		elif password[i] == 'v' or password[i] == 'V':
			new_password += '^'

		elif password[i] == '5':
			new_password += '$'

		else:
			new_password += password[i]

	file.write(passwordName + ':' + new_password + '\n')
	file.close()
	
	newPasswordText = 'Your new password is ' + new_password
	new_password = ''

	font2 = tkfont.Font(size = 15, weight = "bold")

	newPasswordLabel = tk.Label(root, text = newPasswordText, bg = 'black', fg = 'white', font = font2)
	successful = tk.Label(root, text = 'Your new password is saved in "password.txt"', bg = 'black', fg = 'white', font = font2)
	
	newPasswordLabel.place(rely = 0.7, relx = 0.15)
	successful.place(relx = 0.15, rely = 0.8)

	click_enter = 1


#making a window
root = tk.Tk()
root.title("password encryptor")
root.geometry("852x480")

#adding background image
bgimage = tk.PhotoImage(file = "background.png")
bglabel = tk.Label(root, image = bgimage)
bglabel.place(relwidth = 1, relheight = 1)

#adding first text
font1 = tkfont.Font(size = 25, weight = "bold")
header = tk.Label(root, text = "Enter Password name:", bg = "black", fg = "White", font = font1)
header.place(relx = 0.25, rely = 0.2)

#adding input for password name
enterPasswordName = tk.Entry(bglabel)
enterPasswordName.place(rely = 0.3, relx= 0.15, relwidth = 0.7, height = 30)


#adding second text
header = tk.Label(root, text = "Enter Password:", bg = "black", fg = "White", font = font1)
header.place(relx = 0.33, rely = 0.5)


#adding input for password itself
enterPassword = tk.Entry(bglabel)
enterPassword.bind("<Return>", encryptPassword)
enterPassword.place(rely = 0.6, relx= 0.15, relwidth = 0.7, height = 30)


tk.mainloop()

