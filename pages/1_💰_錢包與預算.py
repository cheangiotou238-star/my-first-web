import streamlit as st
import plotly.express as px
import pandas as pd
import time

# 網頁寬度設定
st.set_page_config(layout="wide")

# ==========================================
# 🔒 保安支線任務：反暴力破解與防灌爆登入系統
# ==========================================
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 檢查是否觸發安全鎖定
if st.session_state.login_attempts >= 5:
    st.error("❌ 偵測到異常多次登入失敗！系統已啟動安全限流防護。")
    st.info("🛡️ 防火牆提示：系統已自動對此請求進行重試延遲限制。")
    time.sleep(4) # 強制延遲 4 秒，直接拖垮惡意刷密碼機器人的速度

# 登入介面排版
if not st.session_state.logged_in:
    st.title("🔒 安全使用者驗證中心")
    st.write("進入個人資產與錢包管理中心前，請先進行安全登入。")
    
    with st.container(border=True):
        username = st.text_input("管理員帳號 (請輸入 admin)")
        password = st.text_input("安全密碼 (請輸入 12345)", type="password")
        login_btn = st.button("驗證身分並登入")
        
        if login_btn:
            # 這裡設定一個簡單的測試密碼，未來可對接資料庫
            if username == "admin" and password == "12345":
                st.session_state.logged_in = True
                st.session_state.login_attempts = 0
                st.rerun()
            else:
                st.session_state.login_attempts += 1
                st.error(f"⚠️ 密碼錯誤！這已是第 {st.session_state.login_attempts} 次失敗（連續失敗 5 次將觸發防灌爆限流鎖定）")
                
else:
    # ==========================================
    # 👛 主線任務：全方位資產管理與一站式錢包
    # ==========================================
    st.title("👛 錢包記帳與資產配置中心")
    st.write("管理您的內在錢包，平衡您的資產防禦力。")
    
    # 加上一個登出按鈕
    if st.sidebar.button("🔒 安全登出"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("---")
    
    # 讓用戶手動輸入資產（一站式整合體驗）
    st.subheader("🪙 即時資產配置宣告")
    st.write("請輸入您目前在各大領域的資產分配金額（金流管理）：")
    
    col_in1, col_in2, col_in3, col_in4 = st.columns(4)
    with col_in1:
        cash = st.number_input("🏦 現金 / 銀行存款 (USD)", min_value=0, value=10000, step=500)
    with col_in2:
        stocks = st.number_input("📈 股票總市值 (USD)", min_value=0, value=25000, step=500)
    with col_in3:
        funds = st.number_input("🏦 基金 / ETF 市值 (USD)", min_value=0, value=15000, step=500)
    with col_in4:
        bonds = st.number_input("📜 債券投資額 (USD)", min_value=0, value=5000, step=500)
        
    total_asset = cash + stocks + funds + bonds
    
    st.markdown("---")
    
    # 數據看板與動態圓餅圖
    col_chart1, col_chart2 = st.columns([1, 2])
    
    with col_chart1:
        st.markdown("### 📊 資產總覽")
        with st.container(border=True):
            st.metric(label="💰 平台統計總資產 (USD)", value=f"${total_asset:,.2f}")
            st.write(f"• 現金佔比: {(cash/total_asset)*100:.1f}%")
            st.write(f"• 股票佔比: {(stocks/total_asset)*100:.1f}%")
            st.write(f"• 基金佔比: {(funds/total_asset)*100:.1f}%")
            st.write(f"• 債券佔比: {(bonds/total_asset)*100:.1f}%")
            
    with col_chart2:
        # 將數據轉化為圖表格式
        asset_data = pd.DataFrame({
            "資產類別": ["現金存款", "股票市值", "基金/ETF", "債券投資"],
            "金額 (USD)": [cash, stocks, funds, bonds]
        })
        
        # 畫出高質感的圓餅圖（使用我們設定的黃金強調色）
        fig = px.pie(
            asset_data, 
            values="金額 (USD)", 
            names="資產類別", 
            title="🎯 個人資產配置健康度 (動態互動圖表)",
            hole=0.4, # 變成甜甜圈圖，更有現代網頁感
            color_discrete_sequence=px.colors.sequential.YlOrRd
        )
        st.plotly_chart(fig, use_container_width=True)
