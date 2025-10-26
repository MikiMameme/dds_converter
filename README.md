# 🖼️ DDS→PNG 変換ツール

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made with](https://img.shields.io/badge/Made%20with-ChatGPT-orange?logo=openai)](https://openai.com/)
[![Author](https://img.shields.io/badge/Author-Miki%20Mame-lightgrey)](https://github.com/MikiMameme)  

このツールは、**DDS形式の画像をPNG形式に変換し、指定したフォルダにコピー保存するシンプルなGUIアプリ**です。  
単体ファイル・フォルダ単位の変換に対応しています。  

---

## 🧠 開発のきっかけ

『The Elder Scrolls V: Skyrim Anniversary Edition（AE）』で使用している  
フォトモードMODが **DDS形式で画像を保存する仕様** だったため、  
SNS投稿や共有にそのまま使えず不便でした。  

そのため、**DDSファイルを簡単にPNGに変換できるツール**を  
自分用にPythonで作成しました。  

同じように困っている人の助けになれば幸いです！

---

## 🖥️ 動作環境

- Windows 10 / 11  
- Python 3.10 以降推奨  
- Pillow ライブラリが必要です  
  
## 📦 配布ファイルについて

このリポジトリには、実行ファイル版（dds_converter_gui_advance.zip） も含まれています。  
Pythonをインストールしていない方でも、そのまま動作します。  
  
ZIPを展開し、dds_converter_gui_advance.exe を実行してください。  
  
🔒 注意:  
一部のセキュリティソフトが「未知の実行ファイル」として警告を出す場合があります。  
本ツールは Python スクリプトを pyinstaller でビルドしたものであり、不正な処理は行いません。  
それでも不安がある場合は、Pythonスクリプト版（ソースコード）を実行するか、使用を控えてください。  
  
Use at your own risk.  
  
## 🧱 使い方

EXE または Python スクリプトを起動  

「ファイル選択」または「フォルダ選択」をクリック  

変換後の保存先を選択  

「変換開始」ボタンを押すと、DDS → PNG 変換が行われます  

進捗バー付きで変換の状況が確認できます。


## 🤝 クレジット  
  
このプロジェクトは [ChatGPT (OpenAI GPT-5)] と協力して開発されました。  
設計・コードの一部は ChatGPT の提案をもとに作成されています。

  
## 📝 ライセンス  
  
MIT License  
  
このソフトウェアはオープンソースです。  
自由に利用・改変・再配布できますが、著作権表示とライセンス文を残してください。  
