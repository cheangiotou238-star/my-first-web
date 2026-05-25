import streamlit as st
import yfinance as yf

# 1. 網頁基本設定
st.set_page_config(
    page_title="SmartVest 智能理財投資平台",
    page_icon="💰",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. 側邊欄安全提示
st.sidebar.markdown("# 🧭 平台導航")
st.sidebar.info("歡迎使用 SmartVest！請在左側選單切換不同功能模組。")
st.sidebar.markdown("---")
st.sidebar.caption("🔒 系統已啟用底層安全防護網")

# 3. 主頁面標題
st.title("💰 SmartVest 智能理財投資平台")
st.subheader("一站式管好錢包、監控全球資產。")

st.markdown("---")

# 4. 【新增】首頁全球大盤即時天氣預報
st.markdown("### 🌍 全球核心市場快訊")

@st.cache_data(ttl=1800) # 每半小時更新一次
def get_homepage_data():
    tickers = {"美股 S&P 500": "^GSPC", "美股 NASDAQ": "^IXIC", "香港恆生指數": "^HSI"}
    data = {}
    for name, sym in tickers.items():
        try:
            hist = yf.Ticker(sym).history(period="2d")
            close_t = hist['Close'].iloc[-1]
            change = close_t - hist['Close'].iloc[-2]
            pct = (change / hist['Close'].iloc[-2]) * 100
            data[name] = (close_t, change, pct)
        except:
            data[name] = (0.0, 0.0, 0.0)
    return data

market_data = get_homepage_data()
col_m1, col_m2, col_m3 = st.columns(3)

market_list = list(market_data.items())

with col_m1:
    name, (p, c, pct) = market_list[0]
    st.metric(label=name, value=f"{p:,.2f}", delta=f"{c:+.2f} ({pct:+.2f}%)")
with col_m2:
    name, (p, c, pct) = market_list[1]
    st.metric(label=name, value=f"{p:,.2f}", delta=f"{c:+.2f} ({pct:+.2f}%)")
with col_m3:
    name, (p, c, pct) = market_list[2]
    st.metric(label=name, value=f"{p:,.2f}", delta=f"{c:+.2f} ({pct:+.2f}%)")

st.markdown("---")

# 5. 平台核心功能導覽
st.markdown("### 🛠️ 平台核心模組")
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True): # 加上邊框，讓排版像一張卡片
        st.markdown("#### 👛 錢包管家")
        st.write("每日收支輕鬆記，圖表化分析您的消費盲點，卡緊您的預算防線。")

with col2:
    with st.container(border=True):
        st.markdown("#### 📊 全球市場更新")
        st.write("零延遲對接全球金融數據，每日自動更新股票、指數、基金與債券行情。")

with col3:
    with st.container(border=True):
        st.markdown("#### 🛡️ 安全防護")
        st.write("配合代碼層級的反暴力破解，隱藏後端 IP，守護您的資產隱私。")
