# -*- coding: utf-8 -*-
"""進数変換ツールコード.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aIRXxpmBjVtz-cSoa9etZP7Ft8TCLy3X
"""

import streamlit as st

st.title("進数変換ツール")

# 数値の入力と進数選択のUI
input_value = st.text_input("数値を入力してください")
base_selection = st.radio("入力した値の進数を選んでください", ("10進数", "2進数", "16進数"))

# 変換ボタンを作成
if st.button("変換"):
    try:
        # 入力された進数に応じて10進数に変換
        if base_selection == "10進数":
            decimal_value = int(input_value)
        elif base_selection == "2進数":
            decimal_value = int(input_value, 2)
        elif base_selection == "16進数":
            decimal_value = int(input_value, 16)

        # 各進数への変換（2進数・16進数は接頭辞を除いた形式にする）
        st.write("### 各進数での表記")
        st.write("**10進数:**", decimal_value)
        binary_str = format(decimal_value, 'b')  # 先頭の0bなしで2進数に変換
        st.write("**2進数:**", binary_str)
        hex_str = format(decimal_value, 'x')  # 先頭の0xなしで16進数に変換（小文字）
        st.write("**16進数:**", hex_str)

        # 10進数から2進数への変換過程の表示
        st.write("### 10進数から2進数への変換過程")
        n = decimal_value
        steps = []
        if n == 0:
            steps.append("0はそのまま2進数でも0です。")
        else:
            while n > 0:
                quotient = n // 2  # 商
                remainder = n % 2  # 余り
                steps.append(f"{n} ÷ 2 = {quotient} 余り {remainder}")
                n = quotient
        for step in steps:
            st.write(step)

    except ValueError:
        st.error("入力された値が正しい形式ではありません。")