import streamlit as st 
import random

st.title("письмо от князя") 

# Загадываем число (сохраняем в сессии, чтобы не менялось при перезагрузке) 
if 'number' not in st.session_state: 
  st.session_state.number = random.randint(1, 10)

guess = st.number_input("загадывай число от 1 до 10;", min_value=1, max_value=10)

if st.button("Проверить"):
     if guess == st.session_state.number: 
        st.balloons() # Эффект шариков на экране 
        st.header("молодец чучело") 
        st.write(":P")
        # Рисуем сердечко текстом или эмодзи 
        st.code(""" 
            ******         ******
          **********    ***********
         ************  *************
         ****************************
         ****************************
          **************************
           ************************
            **********************
             ********************
               ****************
                 ************
                   ********
         """, language="text")
else: st.write("Почти! Попробуй еще раз")
