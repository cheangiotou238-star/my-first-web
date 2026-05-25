import streamlit as st

# 1. 網頁基本設定（讓網站變寬、變專業的魔法）
st.set_page_config(
    page_title="SmartVest 智能理財投資平台",
    page_icon="💰",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. 側邊欄標題
st.sidebar.markdown("# 🧭 平台導航")
st.sidebar.info("歡迎使用 SmartVest！請在左側選擇您要使用的理財模組。")

# 3. 主頁面標題與介紹
st.title("💰 SmartVest 智能理財投資平台")
st.subheader("一站式管好錢包、監控全球資產，開啟您的被動收入之旅。")

st.markdown("---")

# 4. 平台核心優勢
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👛 錢包管家")
    st.write("每日收支輕鬆記，圖表化分析您的消費盲點，卡緊您的預算防線。")

with col2:
    st.markdown("### 📊 全球市場更新")
    st.write("零延遲對接全球金融數據，每日自動更新股票、指數、基金與債券行情。")

with col3:
    st.markdown("### 🛡️ 軍事級保安")
    st.write("架設於頂級雲端防護網後，配合代碼層級的反暴力破解，守護您的資產隱私。")

st.markdown("---")
st.info("💡 **系統提示**：目前平台架構已成功搭建。接下來，我們將逐步解鎖「每日金融數據對接」與「個人記帳功能」。")
