import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

def convert_dds_to_png(input_path, output_dir):
    """DDSファイルをPNGに変換して保存"""
    try:
        img = Image.open(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0] + ".png"
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)
        return True
    except Exception as e:
        messagebox.showerror("エラー", f"{input_path}\nの変換中にエラーが発生しました。\n{e}")
        return False

def select_input():
    """モードに応じてファイルまたはフォルダを選択"""
    if mode.get() == "file":
        path = filedialog.askopenfilename(filetypes=[("DDS files", "*.dds")])
        if path:
            input_path.set(path)
    else:
        path = filedialog.askdirectory()
        if path:
            input_path.set(path)

def select_output():
    """出力フォルダを選択"""
    path = filedialog.askdirectory()
    if path:
        output_dir.set(path)

def start_conversion():
    """変換処理"""
    inputs = []

    # 入力の確認
    if not input_path.get():
        messagebox.showwarning("警告", "入力ファイルまたはフォルダを選択してください。")
        return
    if not output_dir.get():
        messagebox.showwarning("警告", "出力先フォルダを選択してください。")
        return

    # 入力モードに応じてリストを作成
    if mode.get() == "file":
        inputs = [input_path.get()]
    else:
        folder = input_path.get()
        for file in os.listdir(folder):
            if file.lower().endswith(".dds"):
                inputs.append(os.path.join(folder, file))

    if not inputs:
        messagebox.showinfo("情報", "変換対象のDDSファイルが見つかりません。")
        return

    # 進捗バーを初期化
    progress["maximum"] = len(inputs)
    progress["value"] = 0

    converted = 0
    for path in inputs:
        if convert_dds_to_png(path, output_dir.get()):
            converted += 1
        progress.step(1)
        root.update_idletasks()

    messagebox.showinfo("完了", f"{converted} 件のファイルを変換しました！")

# -------------------------------
# Tkinter UI構築
# -------------------------------
root = tk.Tk()
root.title("DDS → PNG 変換ツール")
root.geometry("460x350")
root.resizable(False, False)

mode = tk.StringVar(value="file")  # file or folder
input_path = tk.StringVar()
output_dir = tk.StringVar()

# モード選択
frame_mode = tk.LabelFrame(root, text="処理モード")
frame_mode.pack(fill="x", padx=10, pady=10)

tk.Radiobutton(frame_mode, text="ファイル単体", variable=mode, value="file").pack(side="left", padx=20, pady=5)
tk.Radiobutton(frame_mode, text="フォルダ単位", variable=mode, value="folder").pack(side="left", padx=20, pady=5)

# 入力
frame_input = tk.LabelFrame(root, text="入力ファイル／フォルダ")
frame_input.pack(fill="x", padx=10, pady=5)

tk.Entry(frame_input, textvariable=input_path, width=55).pack(side="left", padx=5, pady=5)
tk.Button(frame_input, text="選択", command=select_input).pack(side="left", padx=5)

# 出力
frame_output = tk.LabelFrame(root, text="出力先フォルダ")
frame_output.pack(fill="x", padx=10, pady=5)

tk.Entry(frame_output, textvariable=output_dir, width=55).pack(side="left", padx=5, pady=5)
tk.Button(frame_output, text="選択", command=select_output).pack(side="left", padx=5)

# 進捗バー
frame_progress = tk.LabelFrame(root, text="進捗状況")
frame_progress.pack(fill="x", padx=10, pady=15)

progress = ttk.Progressbar(frame_progress, length=420, mode="determinate")
progress.pack(padx=10, pady=10)

# 実行ボタン
tk.Button(root, text="変換開始", command=start_conversion, bg="#4CAF50", fg="white", width=20, height=2).pack(pady=10)

root.mainloop()
