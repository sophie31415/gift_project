import streamlit as st
import random
from streamlit_extras.let_it_rain import rain # Импортируем дождь

st.set_page_config(page_title="тебе подарок", page_icon="🎁")

# Функция для запуска сердечек
def heart_rain():
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=3,
        animation_length=3, # Дождь будет идти 3 секунды
    )

st.title("письмо от князя")

# Состояния игры
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 5)
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = set()

guess = st.number_input("загадай число от 1 до 5:", min_value=1, max_value=5, step=1)

if st.button("чекаем"):
    # 1. ВИСЕЛИЦА
    if guess == 1:
        st.subheader(" это же hangman")
        word = "любимый"
        
        # Поле для ввода буквы
        letter = st.text_input("введи букву:").upper()
        if st.button("Ок"):
            st.session_state.guessed_letters.add(letter)
            
        display_word = "".join([c if c in st.session_state.guessed_letters else " _ " for c in word])
        st.header(f"`{display_word}`")
        
        if "_" not in display_word:
            st.success("Ты угадал! ❤️")
            heart_rain()

    # 2. РЕТРИВЕР
    elif guess == 2:
        st.subheader("тебя слили..")
        st.image("https://kulturologia.ru/blogs/220717/35300/")
        heart_rain() # Сердечки при появлении песика

    # 3. ЦУ-Е-ФА
    elif guess == 3:
        st.subheader("✊✌️✋ Цу-е-фа")
        choice = st.selectbox("Выбирай:", ["Камень", "Ножницы", "Бумага"])
        bot = random.choice(["Камень", "Ножницы", "Бумага"])
        st.write(f"Я выбрала: {bot}")
        if choice == bot: st.info("Ничья!")
        elif (choice=="Камень" and bot=="Ножницы") or (choice=="Ножницы" and bot=="Бумага"):
            st.success("Ты победил!")
            heart_rain()

    # 4. КОМПЛИМЕНТ
    elif guess == 4:
        st.subheader("люблю тебя")
        st.success("ты самое милое чучело")
        heart_rain() # Вместо снега теперь сердечки!

    # 5. СЕРДЕЧКО ИЗ ТЕКСТА
    elif guess == 5:
        st.code("""
          **       **
        ******   ******
       ********* *********
        """, language="text")
        st.write("### Бесконечная любовь!")
        heart_rain()

    else:
        st.write("Попробуй другое число!")