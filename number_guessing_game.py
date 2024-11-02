import tkinter as tk
import random
import time

# グローバル変数の初期化
random_number = 0
attempts = 0
start_time = 0
timer_running = False

# 難易度を設定する関数
def set_difficulty(difficulty):
    global random_number
    if difficulty == "Easy":
        random_number = random.randint(1, 100)
        instructions_label.config(text="Guess a number between 1 and 100:")
    elif difficulty == "Medium":
        random_number = random.randint(1, 500)
        instructions_label.config(text="Guess a number between 1 and 500:")
    else:  # Hard
        random_number = random.randint(1, 1000)
        instructions_label.config(text="Guess a number between 1 and 1000:")
    
    start_new_game()

# 新しいゲームを開始する関数
def start_new_game():
    global attempts, start_time, timer_running
    attempts = 0
    start_time = time.time()
    timer_running = True  # タイマーを起動
    result_label.config(text="")
    entry.delete(0, tk.END)
    submit_button.config(text="Submit", command=check_guess)
    update_timer()  # タイマー更新を開始

    # 新しいランダムな数字を生成
    if instructions_label.cget("text") == "Guess a number between 1 and 100:":
        global random_number
        random_number = random.randint(1, 100)
    elif instructions_label.cget("text") == "Guess a number between 1 and 500:":
        random_number = random.randint(1, 500)
    else:  # "Guess a number between 1 and 1000:"
        random_number = random.randint(1, 1000)

# プレイヤーの入力をチェックする関数
def check_guess():
    global attempts, timer_running
    try:
        guess = int(entry.get())
        attempts += 1

        # 数字がランダムナンバーより小さい場合
        if guess < random_number:
            result_label.config(text="Too low! Try a higher number.")
        
        # 数字がランダムナンバーより大きい場合
        elif guess > random_number:
            result_label.config(text="Too high! Try a lower number.")
        
        # 数字が正解の場合
        else:
            elapsed_time = round(time.time() - start_time)  # 小数点以下を削除
            result_label.config(text=f"Congratulations! You guessed the number in {attempts} tries and {elapsed_time} seconds.")
            submit_button.config(text="Next Game", command=start_new_game)
            timer_running = False  # タイマーを停止
        
        entry.delete(0, tk.END)
    
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
        entry.delete(0, tk.END)

# タイマー更新関数
def update_timer():
    if timer_running:
        elapsed_time = round(time.time() - start_time)  # 小数点以下を削除
        timer_label.config(text=f"Time: {elapsed_time} seconds")
        root.after(1000, update_timer)  # 1秒ごとにタイマーを更新

# ウィンドウの設定
root = tk.Tk()
root.title("Number Guessing Game")

# ラベル
instructions_label = tk.Label(root, text="Guess a number between 1 and 100:")
instructions_label.pack()

# 難易度選択ボタン
difficulty_frame = tk.Frame(root)
difficulty_label = tk.Label(difficulty_frame, text="Select Difficulty:")
difficulty_label.pack(side="left")
for difficulty in ["Easy", "Medium", "Hard"]:
    button = tk.Button(difficulty_frame, text=difficulty, command=lambda d=difficulty: set_difficulty(d))
    button.pack(side="left")
difficulty_frame.pack()

# タイマー表示ラベル
timer_label = tk.Label(root, text="Time: 0 seconds")
timer_label.pack()

# 入力ボックス
entry = tk.Entry(root)
entry.pack()

# ボタン
submit_button = tk.Button(root, text="Submit", command=check_guess)
submit_button.pack()

# 結果のラベル
result_label = tk.Label(root, text="")
result_label.pack()

# ウィンドウの表示
root.mainloop()
