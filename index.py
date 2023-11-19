import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

dictact = {1:"普通攻擊",2:"卸力",3:"使用暗器"}
cmd = '0'
bossdmg = 0
playerdmg = 0
Flag = False
def loop():
    bossreaction()
    dmgcount()
    print(f"CMD:{cmd}")
    print(f"PD:{playerdmg}")
    print(f"BD:{bossdmg}")
    print(f"{block()}")
    bosshp(playerdmg,bossdmg)
    playerHP(playerdmg,bossdmg)
    Turn()
    playerAP()

def bossreaction():
    global action
    action = random.randint(1,3) #1是普A 2是卸力 3是丟暗器 

def playeraction(x):
    global cmd,playerdmg
    if x == 1:
        cmd = str(1)
    if x == 2:
        cmd = str(2)
    if x == 3:
        cmd = str(3)
    if x == 4:
        cmd = str(4)
    loop()

def block():
    global Flag

    block_percent = random.randint(1,100)
    print(block_percent)
    if block_percent > 70:
        Flag = True
        print(Flag)
    else:
        Flag = False
        print(Flag)

def dmgcount():
    global action,playerdmg,bossdmg
    if cmd == '1':
        if action == 1:
            playerdmg = int(random.triangular(70,100,120))
            bossdmg = (int(random.randint(60, 80)))
            bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},造成了{bossdmg}點傷害")
            playeract_label.config(text=f"你的打擊造成了{playerdmg}點傷害")
        if action == 2:
            bossdmg = 0
            if block():
                playerdmg = 0
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},閃避成功,完全迴避了傷害")
                playeract_label.config(text=f"你的打擊造成了{playerdmg}點傷害")
            else:
                playerdmg = int(int(random.triangular(70,100,120))*0.8)
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},閃避失敗,但隔擋了一部分傷害")
                playeract_label.config(text=f"你的打擊造成了{playerdmg}點傷害")
        if action == 3:
            playerdmg = int(random.randint(70,80))
            bossdmg = (int(random.randint(45, 80))+40)
            bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},並受到你的打擊{playerdmg}點傷害")
            playeract_label.config(text=f"你因為{dictact[action]},被差合了!你受到{bossdmg}點傷害")

    if cmd == '2':
        playerdmg = 0
        if action == 1:
            if block():
                bossdmg = 0
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},造成了{bossdmg}點傷害")
                playeract_label.config(text=f"你完美閃避,完全迴避了傷害")
            else:
                bossdmg = int(int(random.randint(45, 80))*0.8)
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]}")
                playeract_label.config(text=f"你的閃避失敗了,但還是格擋了一部分,受到{bossdmg}點傷害")

        if action == 2:
            if block():
                bossdmg = 0
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},它盯著你,像個傻逼")
                playeract_label.config(text=f"你閃避了個寂寞,你也盯著它,像個傻逼")

            else:
                bossdmg = 0
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},它盯著你,像個傻逼")
                playeract_label.config(text=f"你閃避失敗,還格檔個寂寞,你也盯著它,像個傻逼")
        if action == 3:
            if block():
                bossdmg = 0
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},造成了{bossdmg}點傷害")
                playeract_label.config(text=f"你完美閃避,完全迴避了傷害")

            else:
                bossdmg =   int(max(0, random.randint(45, 80)) - 45)

                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]}")
                playeract_label.config(text=f"你的閃避失敗了,但你格檔成功了暗器,受到{bossdmg}點傷害")

    if cmd == '3':
        if action == 1:
            playerdmg = int(int(random.randint(90,120))+40)
            bossdmg = (int(random.randint(45, 80)))
            bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},造成了{bossdmg}點傷害")
            playeract_label.config(text=f"你差合了它!造成了{playerdmg}點傷害")
        if action == 2:
            bossdmg = 0
            if block():
                playerdmg = 0
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},閃避成功,完全迴避了傷害")
                playeract_label.config(text=f"你的暗器造成了{playerdmg}點傷害")
            else:
                playerdmg = int(int(random.randint(90,120))-50)
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},閃避失敗,它沒看過這種'杯壁'玩意兒,只檔下部分傷害")
                playeract_label.config(text=f"你的打擊造成了{playerdmg}點傷害,是外鄉人的勝利!")
        if action == 3:
            playerdmg = int(random.randint(90,120))
            bossdmg = (int(random.randint(45, 60)))
            bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},並受到你的射擊{playerdmg}點傷害")
            playeract_label.config(text=f"你們互相{dictact[action]},你受到{bossdmg}點傷害")
    if cmd == '4':
        if action == 2:
            bossdmg = 0
            if block():
                playerdmg = 0
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},閃避成功,完全迴避了傷害")
                playeract_label.config(text=f"你的打擊造成了{playerdmg}點傷害")
            else:
                double = random.randint(2,4)
                playerdmg = int((250*double))*0.9
                bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},閃避失敗,但必殺技幾乎無法阻擋,受了很重的傷")
                playeract_label.config(text=f"你的打擊造成了{playerdmg}點傷害!")
        else:
            double = random.randint(2,4)
            playerdmg = int(250*double)
            bossact_label.config(text=f"BOSS上回合使用了{dictact[action]},但是必殺技無法被阻擋!受到{playerdmg}點傷害")
            playeract_label.config(text=f"必殺技造成高額傷害!!")

def Turn():
    turn_text = Turn_label.cget("text")
    turn_value = int(turn_text.split(":")[1])
    turn_value += 1
    Turn_label.config(text=f"Turn:{turn_value}")

def bosshp(playerdmg,bossdmg):

    bossHP = bossHP_label.cget("text")
    bossHP = str(bossHP.split("/")[0])
    bossHP = int(bossHP.split(":")[1])
    bossHP_value = int(max(0, bossHP - playerdmg))

    if bossHP_value != 0:
        bossHP_label.config(text=f"BOSS HP:{bossHP_value}/1500")
    else:
        bossHP_label.config(text=f"BOSS HP:{bossHP_value}/1500")
        messagebox.showinfo("win","you win")

def playerHP(playerdmg,bossdmg):
    playerHP_text = playerHP_label.cget("text")
    pHP = str(playerHP_text.split("/")[0])
    playerHP_value = int(pHP.split(":")[1])
    playerHP_value = int(max(0, playerHP_value - bossdmg))

    if playerHP_value != 0:
        playerHP_label.config(text=f"HP:{playerHP_value}/500")
    else:
        playerHP_label.config(text=f"HP:{playerHP_value}/500")
        messagebox.showinfo("lose","you lose")

def playerAP():
    playerAP = playerAP_label.cget("text")
    playerAP = str(playerAP.split("/")[0])
    playerAP = int(playerAP.split(":")[1])
    if cmd != '4':
        if (playerAP + 10) <= 100:
            playerAP_value = int(playerAP + 10)
            playerAP_label.config(text=f"AP:{playerAP_value}/100")
            if playerAP_value >= 80:
                button4['state'] = tk.NORMAL
    else:
        if playerAP >= 80:
            button4['state'] = tk.DISABLED
            playerAP_value = int(playerAP - 80)
            playerAP_label.config(text=f"AP:{playerAP_value}/100")
        else:
            button4['state'] = tk.DISABLED


def load_and_display_image(image_path):

    img = Image.open(image_path)
    width, height = img.size
    max_width = 512
    max_height = 450
    ratio = min(max_width / width, max_height / height)

    img = img.resize((int(width * ratio), int(height * ratio)), Image.ANTIALIAS)

    tk_img = ImageTk.PhotoImage(img)

    image_label = tk.Label(boss_frame, image=tk_img)
    image_label.image = tk_img  

    image_label.grid(row=4, column=0)


root = tk.Tk()
root.title("game")

boss_frame = tk.Frame(root)
boss_frame.grid(row=0, column=0)

Turn_label = tk.Label(boss_frame, text="Turn:1")
Turn_label.grid(row=0, column=0)

bossact_label = tk.Label(boss_frame, text="BOSS上回合執行了:?")
bossact_label.grid(row=1, column=0,pady= 5)

playeract_label = tk.Label(boss_frame, text="你上回合執行了:?")
playeract_label.grid(row=2, column=0,pady= 5)

bossHP_label = tk.Label(boss_frame, text="BOSS HP:1500/1500")
bossHP_label.grid(row=3, column=0,pady= 10)

load_and_display_image("BOSS1.jpg")

player_frame = tk.Frame(root)
player_frame.grid(row=1, column=0, sticky="ew")

playerHP_label = tk.Label(player_frame, text="HP:500/500")
playerHP_label.grid(row=0, column=0, padx=50, pady=10)
playerAP_label = tk.Label(player_frame, text="AP:0/100")
playerAP_label.grid(row=1, column=0, padx=50, pady=10)

# 配置player_frame的第一列权重为1
for i in range(1,5):
    player_frame.columnconfigure(i, weight=2)

button1 = tk.Button(player_frame, text="普通攻擊", command=lambda: playeraction(1))
button1.grid(row=0, column=1, rowspan=2, sticky="ew")
button2 = tk.Button(player_frame, text="卸力", command=lambda: playeraction(2))
button2.grid(row=0, column=2, rowspan=2, sticky="ew")
button3 = tk.Button(player_frame, text="暗器", command=lambda: playeraction(3))
button3.grid(row=0, column=3, rowspan=2, sticky="ew")
button4 = tk.Button(player_frame, text="必殺技", command=lambda: playeraction(4),state=tk.DISABLED)
button4.grid(row=0, column=4, rowspan=2, sticky="ew")
root.mainloop()