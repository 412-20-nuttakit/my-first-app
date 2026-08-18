import streamlit as st

st.markdown("# :red[🏋️คำนวณหาค่าดัชนีมวลกาย BMI 🏃]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูง")

wig_kg = st.number_input("กรอกข้อมูลน้ำหนักของคุน (กิโลกรัม):",min_value=1.0,value=1.0)
hig_cm = st.number_input("กรอกข้อมูลน้ส่วนสูงของคุน (เซนติเมตร):",min_value=1.0,value=1.0)

if st.button("🔥คำนวณหาค่า BMI⚖️"):
    hig_m=hig_cm/100
    bmi=wig_kg/(hig_m**2)

    st.write("_____")
    st.header(f"ค่า BMI ของคุน**{bmi:.2f}**")

if bmi <18.5:
    st.warning("คุนมีน้ำหนักน้อยกว่าเกณ์ (ผอม)")
    elif 18.5 <=bmi< 23:
        st.success("คุนมีน้ำหนักอยู่ในเกณ์ (สุขภาพดี)")
    elif 23 <=bmi< 25:
        st.info("คุนมีน้ำหนักเกินเกณ์ (ท้วม)")
    else:
        st.error("⚠️อ้วน🚨")

st.divider()
st.write("ณัฏฐกิตติ์ จันทร์ศิริ เลขที่ 10  ม.4/12")
