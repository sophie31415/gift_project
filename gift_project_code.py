import streamlit as st
import random
from streamlit_extras.let_it_rain import rain # Импортируем дождь
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Загружаем анимации (ссылки на красивые сердца)
lottie_heart = load_lottieurl("https://lottiefiles.com")
lottie_celebrate = load_lottieurl("https://lottiefiles.com")

image_dog= "https://kulturologia.ru/files/u18476/shenkizolotogoretrivera-14.jpg"

st.set_page_config(page_title="that's a present 4 u honey!", page_icon="🎁")

# Функция для запуска сердечек
def heart_rain():
    rain(
        emoji="❤️",
        font_size=64,
        falling_speed=3,
        animation_length=3, # Дождь будет идти 3 секунды
    )

st.markdown("""
    <style>
    /* 1. Подключаем тонкий и длинный шрифт */
    @import url('https://googleapis.com');

    /* 2. Фон "Глубокий океан" */
    .stApp {
        background-color: #003366; /* Глубокий синий */
    }

    /* 3. Центрирование */
    .main .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    /* 4. Тонкий, длинный и курсивный текст */
    div, p, label, .stText, .stMarkdown, h1, h2, h3 {
        font-family: 'Josefin Sans', sans-serif !important;
        font-weight: 90 !important; /* Делаем шрифт максимально тонким */
        color: #E0F2F1 !important; /* Цвет морской пены (почти белый) */
        font-size: 28px !important; 
        font-style: italic !important;
        text-align: center !important;
    }

    /* 5. Делаем поле ввода и кнопки аккуратными */
    .stNumberInput, .stTextInput, .stButton {
        width: fit-content;
        margin: 0 auto;
    }

    /* Убираем жирность у заголовков, чтобы они оставались тонкими */
    h1, h2, h3 {
        font-weight: 100 !important;
        font-size: 45px !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False

if not st.session_state.start_clicked:
    # Заголовок
    st.markdown("#hi sweetie,thats some presents i made for u!")
    
    # Собачка (центрируется автоматически благодаря CSS выше)
    st.image("https://placedog.net", width=400)
    
    st.markdown("### *ur special for me*")
    
    if st.button("open!"):
        st.session_state.start_clicked = True
        st.rerun()
else:
    
    
    st.title("some letter..❤️")

    # Состояния игры
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 5)
    if 'guessed_letters' not in st.session_state:
        st.session_state.guessed_letters = set()

    guess = st.number_input("guess a number from 1 to 5!", min_value=1, max_value=10, step=1)

        # 1. ВИСЕЛИЦА
    if guess == 1:
            st.subheader("mini-game")
            word = "sweetheart"
            
            # --- Инициализация памяти игры ---
            if 'guessed_letters' not in st.session_state:
                st.session_state.guessed_letters = set()
            if 'attempts' not in st.session_state:
                st.session_state.attempts = 6  # Даем 6 попыток

            # --- Подсказка и счетчик ---
            st.info("💡 hint: it started  w an **'S'**")
            st.write(f"honey, u have: {st.session_state.attempts} attemts!")

            # --- Ввод буквы ---
            # Мы добавляем key="hangman_input", чтобы Streamlit не путался
            letter = st.text_input("write one eng letter:", max_chars=1, key="hangman_input").upper()
            
            if letter:
                if letter in st.session_state.guessed_letters:
                    st.warning(f"u already have written this letter,aww,dont sleeep!! 😉")
                elif letter in word:
                    st.session_state.guessed_letters.add(letter)
                    st.toast("yeap,i have this letter!", icon="✅")
                else:
                    st.session_state.guessed_letters.add(letter)
                    st.session_state.attempts -= 1
                    
                    # Милые подколы при ошибке
                    roasts = [
                        "ur my stupid hehe🌴",
                        "i believe in u!(almost..)😎",
                        "?? r u a fcking robot,dear?? 🤖",
                        "oops, i  see someone couldnt read the hint... 🙊"
                    ]
                    st.error(random.choice(roasts))

            # --- Отображение слова ---
            display_word = "".join([c if c in st.session_state.guessed_letters else " _ " for c in word])
            st.header(f"`{display_word}`")

            # --- Финал игры ---
            if " _ " not in display_word:
                st.success("sweetie u passed! ❤️")
                heart_rain()
                if st.button("start again??)"):
                    st.session_state.guessed_letters = set()
                    st.session_state.attempts = 6
                    st.rerun()
                    
            elif st.session_state.attempts <= 0:
                st.error(f"u lost r attemts! the word was: {word}. but actually its not that bad)😴")
                if st.button("give me one more chance!"):
                    st.session_state.guessed_letters = set()
                    st.session_state.attempts = 6
                    st.rerun()

        # 2. РЕТРИВЕР
    elif guess == 2:
        st.subheader("📸 i think i found ur photo!..")
        # Используем твою новую переменную
        st.image(image_dog, caption="the source: folder 'the most cutiest creature in the world'")
        
        heart_rain() # Сразу немного сердечек
        
        st.write("## is that u!?")
        
        # Создаем две колонки для кнопок, чтобы они были рядом
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("ofc its me!"):
                st.success("iknew that! u are embodiment of beauty.")
                st.balloons()
                
        with col2:
            if st.button("no thats not me! 🤨"):
                st.warning("не пизди")
                if st.button("all right its me.."):
                    st.write("### good boy ❤️")
                    heart_rain()

        # 3. ЦУ-Е-ФА
    elif guess == 3:
        st.subheader("some game?✊✌️✋")
        st.write("choose:")
        
        col_k, col_n, col_b = st.columns(3)
        user_choice = None

        if col_k.button("🪨"): user_choice = "rock"
        if col_n.button("✂️ "): user_choice = "scissors"
        if col_b.button("📄 "): user_choice = "paper"

        if user_choice:
            bot = random.choice(["rock", "scissors", "paper"])
            emoji_map = {"rock": "🪨", "scissors": "✂️", "paper": "📄"}
            
            st.write(f"ur choice: {emoji_map[user_choice]} VS my choice: {emoji_map[bot]}")
            
            if user_choice == bot:
                st.info("🤝 a draw! we think not that different")
            elif (user_choice == "rock" and bot == "scissors") or \
                (user_choice == "scissors" and bot == "paper") or \
                (user_choice == "paper" and bot == "rock"):
                st.success("u won honey! your luck !")
                st.balloons()
                heart_rain()
            else:
                st.warning("i won! but you are always first).")

        # 4. КОМПЛИМЕНТ
    elif guess == 4:
        st.subheader("just want to say ..")
        compliments = [
            "u r the reason why i laughed! ",
            "u made my world brighter. ✨",
            "u r the most fair person i ever met! ",
            "why its always so cozy around u?. ☕",
            "never forget that u r the wonder. "
        ]
        if st.button("ok say ur words"):
            st.success(random.choice(compliments))
            heart_rain()

    # 5. КРАСИВОЕ СЕРДЦЕ (Lottie)
    elif guess == 5:
        st.subheader("luv u!happy bday honey)")
        if lottie_heart:
            st_lottie(lottie_heart, height=300, key="heart")
        else:
            st.write("### ❤️❤️❤️") # Запасной вариант, если нет интернета
        st.write("u amazing")
        heart_rain()

    else:
            st.write("r u an asshole?just choose another number!")
