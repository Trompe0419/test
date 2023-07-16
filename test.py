import streamlit as st

st.title("Calculater for Quiz")
# st.write("write")
# st.markdown("# Head1")
# st.markdown("## Head2")

seven_three = st.checkbox("7o3x")

if seven_three:
   
   if 'CC' not in st.session_state:
      st.session_state["CC"] = 0
   if st.button("o", key=0):
      st.session_state["CC"] += 1
   st.write("o", st.session_state["CC"])
   if 'inCC' not in st.session_state:
      st.session_state["inCC"] = 0
   if st.button("x", key=1):
      st.session_state["inCC"] += 1
   st.write("x", st.session_state["inCC"])

   
   # st.button("1") #引数に入れるとboolで返す
   # st.button("2") #引数に入れるとboolで返す
   # st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢
   # st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢、複数選択可
   # st.radio("ラジオボタン", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名（選択肢群の上に表示）、第二引数：選択肢
   # st.text_input("文字入力欄") #引数に入力内容を渡せる
   # st.text_area("テキストエリア")