import random
import tkinter as tk
from tkinter import messagebox


def check_guess():
    global guess_left
    guess_left= 10

    guess=entry_guess.get()
    entry_guess.delete(tk.END)

    if len(guess)!=3 or not guess.isdigit():
        messagebox.showerror('Error:','please enter 3-digit number')
        return
    if guess[0]== guess[1] or guess[1] == guess[2] or guess[2]==guess[0]:
        messagebox.showerror('Error:', 'dont repeat the same number')
        return

    strike=0
    ball=0
    out=0
    for i in range(3):
        if int(guess[i]) in numbers:
            if int(guess[i]) == numbers[i]:
                strike +=1
            else:
                ball +=1
        else:
            out+=1
        if strike ==3:
            print('게임이 종료되었습니다')
            break

    result=f"{strike},'스트라이크', {ball},'볼', {out},'아웃')"
    list_results.insert(tk.END,f"guess: {guess} - {result}")

window = tk.Tk()


title = 'number_baseball'
window.title(title)
numbers = []
number = random.randint(1, 9)
while number not in numbers:
    numbers.append(number)
label_intro = tk.Label(window,text='숫자 야구 게임')
label_intro.pack(pady=10)
label_instruction=tk.Label(window, text='3자리 숫자를 입력하세요:')
label_instruction.pack(pady=5)

entry_guess= tk.Entry(window)
entry_guess.pack(pady=5)

btn_submit =tk.Button(window, text='Submit',command=check_guess)
btn_submit.pack(pady=5)

list_results = tk.Listbox(window, width=40, height=10)
list_results.pack(pady=10)
window.mainloop()
print('---------------------')
print('게임을 종료합니다')
