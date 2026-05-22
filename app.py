import streamlit as st
import datetime

# 1. 設定網頁標題與圖示
st.set_page_config(page_title="我的個人空間", page_icon="🌟")

# 2. 網頁大標題
st.title("🚀 歡迎來到我的第一支網頁程式！")
st.write("這是完全用 Python 打造的互動式網站。")

# 3. 側邊欄（Sidebar）
st.sidebar.header("個人設定")
user_name = st.sidebar.text_input("輸入你的名字：", "學習者")

# 4. 主畫面歡迎詞
st.subheader(f"👋 你好，{user_name}！今天想寫點什麼？")

# 5. 互動組件：心情選擇器
mood = st.select_slider(
    "選擇你今天的心情分數：",
    options=["累翻了 🥱", "還可以 😐", "不錯 🙂", "動力滿滿 🔥", "超級開心 🎉"]
)
st.write(f"你今天的心情是：**{mood}**")

# 6. 互動組件：輸入每天的進度
st.markdown("---")
st.subheader("📚 今日學習與目標追蹤")

today = datetime.date.today()
st.date_input("今天是：", today)

study_topic = st.text_input("今天學習了什麼主題？", "例如：Python 網頁開發入門")
study_hours = st.number_input("預計學習幾小時？", min_value=0.0, max_value=24.0, value=1.0, step=0.5)

# 7. 提交按鈕與結果顯示
if st.button("儲存今日紀錄"):
    st.success(f"✅ 紀錄成功！{user_name} 在 {today} 學習了「{study_topic}」共 {study_hours} 小時！")
    st.balloons()  # 畫面會噴出慶祝氣球！