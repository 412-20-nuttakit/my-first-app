import steamlit as st
ss.title("แอปพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")

b_y=st.number_input("กรอกปีพ.ศ.ที่ต่องการเเปลง",value=2569)
c_y=b_y-543
st.header(f"ปี ค.ศ. คือ : {c_y}")

         
