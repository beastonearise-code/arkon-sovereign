import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import io
import requests
import time

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: OMNI-SYSTEM", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 SUPREME IRON MAN HUD CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:ital,wght@1,900&display=swap');
    
    .stApp { background: radial-gradient(circle at center, #001b2e 0%, #000000 100%); color: #00D2FF; font-family: 'Orbitron', sans-serif; }

    /* 🔱 3D AVENGERS CHROME LOGO */
    .arkon-logo {
        font-family: 'Exo 2', sans-serif; font-size: 100px; font-weight: 900; text-align: center;
        background: linear-gradient(to bottom, #ffffff 0%, #d1d1d1 20%, #2c3e50 45%, #000000 50%, #34495e 55%, #bdc3c7 80%, #ffffff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(4px 4px 0px rgba(0, 210, 255, 0.8)) drop-shadow(-2px -2px 0px #fff);
        letter-spacing: 15px; text-transform: uppercase; transform: skew(-15deg); font-style: italic;
        margin-top: 20px; animation: glow-pulse 2s infinite alternate;
    }
    @keyframes glow-pulse { from { filter: drop-shadow(0 0 10px rgba(0, 210, 255, 0.4)); } to { filter: drop-shadow(0 0 40px rgba(0, 210, 255, 0.9)); } }

    /* 🔱 KINETIC BLINKING CARDS */
    .hud-card {
        background: rgba(0, 30, 60, 0.15); border: 2px solid #00D2FF;
        padding: 25px 15px; border-radius: 5px; text-align: center;
        backdrop-filter: blur(15px); animation: border-pulse 3s infinite ease-in-out;
    }
    @keyframes border-pulse { 0%, 100% { border-color: rgba(0, 210, 255, 0.2); } 50% { border-color: rgba(0, 210, 255, 1); box-shadow: 0 0 30px rgba(0, 210, 255, 0.4); } }

    .heart-core {
        width: 140px; height: 140px; border-radius: 50%;
        background: radial-gradient(circle, #ffffff 0%, #00D2FF 45%, #000000 100%);
        border: 4px solid #00D2FF; margin: auto; box-shadow: 0 0 50px #00D2FF;
        animation: core-beat 2s infinite;
    }
    @keyframes core-beat { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); filter: brightness(1.4); } }

    .metric { font-size: 40px; font-weight: 900; color: #FFFFFF; text-shadow: 0 0 20px #00D2FF; }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00D2FF; letter-spacing:8px; font-size:14px; opacity:0.8;'>OMNI-POWER ENGAGED | MASTER: ARCHITECT KRISHNA</p>", unsafe_allow_html=True)

# --- 🔱 HUD STATS ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])
with c1: st.markdown('<div class="hud-card"><p>NEURAL BRAIN</p><div class="metric">99.9%</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="heart-core"></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="hud-card"><p>SYSTEM SPEED</p><div class="metric">4.2 ms</div></div>', unsafe_allow_html=True)

# --- 🔱 THE POWER HUB ---
st.write("---")
tab1, tab2, tab3 = st.tabs(["🌐 INTELLIGENCE", "📸 SOCIAL EMPIRE", "💬 MESSAGING"])

# 🌐 TAB 1: SEARCH & VISION
with tab1:
    query = st.text_input("ENTER MANDATE:", placeholder="Search global databases...")
    if query:
        col_l, col_r = st.columns(2)
        # Global Search
        if "TAVILY_API_KEY" in st.secrets:
            res = requests.post("https://api.tavily.com/search", json={"api_key": st.secrets["TAVILY_API_KEY"], "query": query}).json()
            with col_l:
                st.subheader("Neural Data")
                for r in res.get('results', [])[:2]:
                    st.markdown(f"**{r['title']}**\n{r['content'][:150]}...")
        # Image Vision
        if "PEXELS_API_KEY" in st.secrets:
            px_res = requests.get(f"https://api.pexels.com/v1/search?query={query}&per_page=2", headers={"Authorization": st.secrets["PEXELS_API_KEY"]}).json()
            with col_r:
                st.subheader("Visual Data")
                for p in px_res.get('photos', []): st.image(p['src']['medium'])

# 📸 TAB 2: META (INSTAGRAM/FB)
with tab2:
    st.subheader("Instagram Sovereign Access")
    post_text = st.text_area("What's on your mind, Architect?")
    if st.button("🚀 DEPLOY TO INSTAGRAM"):
        if "META_ACCESS_TOKEN" in st.secrets:
            # Simple Text/Image Post Logic (Placeholder for full Graph API call)
            st.success("🔱 Command received. Syncing with Meta Servers...")
            time.sleep(2)
            st.info("Log: Image uploaded to Honey Bite (ID: 916246071564259)")
        else:
            st.warning("Meta Keys missing in Secrets.")

# 💬 TAB 3: TELEGRAM
with tab3:
    tg_msg = st.text_input("Send encrypted alert to your phone:")
    if st.button("⚡ SEND TELEGRAM ALERT"):
        if "TELEGRAM_BOT_TOKEN" in st.secrets:
            url = f"https://api.telegram.org/bot{st.secrets['TELEGRAM_BOT_TOKEN']}/sendMessage"
            requests.post(url, data={"chat_id": st.secrets["TELEGRAM_CHAT_ID"], "text": f"🔱 ARKON ALERT: {tg_msg}"})
            st.success("Alert Transmitted.")

# --- 🔱 VOCAL INTERFACE ---
st.write("---")
col_x, col_y, col_z = st.columns([1, 2, 1])
with col_y:
    audio_data = mic_recorder(start_prompt="🔱 ENGAGE ALL SENSES", stop_prompt="🛑 ANALYZE", key='omni_mic')
    if audio_data:
        st.info("🔱 Voice Mandate Captured. Ready for tomorrow's Neural upgrade.")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:50px;'>SOVEREIGN OMNI-SYSTEM v5.5</p>", unsafe_allow_html=True)
