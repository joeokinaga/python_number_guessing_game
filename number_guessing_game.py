import tkinter as tk
import random
import time


random_number = 0
attempts = 0
start_time = 0
timer_running = False


def set_difficulty(difficulty):
    global random_number
    if difficulty == "Easy":
        random_number = random.randint(1, 100)
        instructions_label.config(text="Guess a number between 1 and 100:")
    elif difficulty == "Medium":
        random_number = random.randint(1, 500)
        instructions_label.config(text="Guess a number between 1 and 500:")
    else:  
        random_number = random.randint(1, 1000)
        instructions_label.config(text="Guess a number between 1 and 1000:")
    
    start_new_game()


def start_new_game():
    global attempts, start_time, timer_running
    attempts = 0
    start_time = time.time()
    timer_running = True 
    result_label.config(text="")
    entry.delete(0, tk.END)
    submit_button.config(text="Submit", command=check_guess)
    update_timer() 


    if instructions_label.cget("text") == "Guess a number between 1 and 100:":
        global random_number
        random_number = random.randint(1, 100)
    elif instructions_label.cget("text") == "Guess a number between 1 and 500:":
        random_number = random.randint(1, 500)
    else:  # "Guess a number between 1 and 1000:"
        random_number = random.randint(1, 1000)


def check_guess():
    global attempts, timer_running
    try:
        guess = int(entry.get())
        attempts += 1


        if guess < random_number:
            result_label.config(text="Too low! Try a higher number.")
        

        elif guess > random_number:
            result_label.config(text="Too high! Try a lower number.")
        

        else:
            elapsed_time = round(time.time() - start_time)
            result_label.config(text=f"Congratulations! You guessed the number in {attempts} tries and {elapsed_time} seconds.")
            submit_button.config(text="Next Game", command=start_new_game)
            timer_running = False 
        
        entry.delete(0, tk.END)
    
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
        entry.delete(0, tk.END)


def update_timer():
    if timer_running:
        elapsed_time = round(time.time() - start_time)  
        timer_label.config(text=f"Time: {elapsed_time} seconds")
        root.after(1000, update_timer) 


root = tk.Tk()
root.title("Number Guessing Game")


instructions_label = tk.Label(root, text="Guess a number between 1 and 100:")
instructions_label.pack()


difficulty_frame = tk.Frame(root)
difficulty_label = tk.Label(difficulty_frame, text="Select Difficulty:")
difficulty_label.pack(side="left")
for difficulty in ["Easy", "Medium", "Hard"]:
    button = tk.Button(difficulty_frame, text=difficulty, command=lambda d=difficulty: set_difficulty(d))
    button.pack(side="left")
difficulty_frame.pack()


timer_label = tk.Label(root, text="Time: 0 seconds")
timer_label.pack()


entry = tk.Entry(root)
entry.pack()


submit_button = tk.Button(root, text="Submit", command=check_guess)
submit_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
