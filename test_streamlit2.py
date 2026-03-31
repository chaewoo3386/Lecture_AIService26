import streamlit as st
import time

st.title("사용자 입력")

# 입력 영역
with st.container():

    name = st.text_input("이름")
    age = st.number_input("나이", min_value=1)
    agree = st.checkbox("약관에 동의합니다")

    # 버튼
    submit = st.button("제출")

# 결과 출력
if submit:
    st.write(f"이름: {name}, 나이: {age}")

    msg = st.info("처리 중입니다...")
    time.sleep(1.0)

    if agree:
        msg.success("약관에 동의했습니다.")
    else:
        msg.error("약관에 동의해야 합니다.")