import streamlit as st

st.title("⏱️guess the word")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.start = time.time() 
    st.session_state.is_ended = False

def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

st.button("🎮PLAY", on_click=reset_game)
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ timeleft: {time_left} s")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 finshish"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    
st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)

st.divider()
st.write("ณัฏฐกิตติ์ จันทร์ศิริ เลขที่ 10  ม.4/12")







