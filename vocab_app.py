import time
import streamlit as st

st.title("⏱️ guess the word")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

@st.dialog("📊 final result")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

    if u_ans1 == "apple":
        st.success("✅ quesution 1: correct")
        score += 1
    else:
        st.error(f"❌ quesution 1:incorrect (your answer: '{u_ans1}')")

    if u_ans2 == "fish":
        st.success("✅ quesution 2: correct")
        score += 1
    else:
        st.error(f"❌ quesution 2: incorrect (your answer: '{u_ans2}')")

    if u_ans3 == "paino":
        st.success("✅ quesution 3: correct")
        score += 1
    else:
        st.error(f"❌ quesution 3: incorrect (your answer: '{u_ans3}')")

    if u_ans3 == "paper":
        st.success("✅ quesution 4: correct")
        score += 1
    else:
        st.error(f"❌ quesution 4: incorrect (your answer: '{u_ans4}')")

    if u_ans3 == "lemon":
        st.success("✅ quesution 5: correct")
        score += 1
    else:
        st.error(f"❌ quesution 5: incorrect (your answer: '{u_ans5}')")

    st.info(f"🏆 final score: {score} point")

    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")

st.button("🎮 PLAY", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(90 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ time left: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "quesution 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "quesution 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "quesution 3: p_ _ no have 99 keys but cant open a single door",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "quesution 4:_ _ p _ e r is made with tree bou wight less that a gram",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "quesution 5:when life give you l _ m _ n you make a drink  ",
    value=st.session_state.ans5_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 finshish"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()
    
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1,ans2,ans3,ans4,ans5)

st.divider()
st.write("ณัฏฐกิตติ์ จันทร์ศิริ เลขที่ 10  ม.4/12")
