import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import io
import time

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: JARVIS CLEAR", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 CLEAR CINEMATIC HUD CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:ital,wght@1,900&display=swap');
    
    /* 🔱 DEEP OBSIDIAN BACKGROUND (CLEAN - NO LINES) */
    .stApp {
        background: radial-gradient(circle at center, #001b2e 0%, #000000 100%);
        color: #00D2FF;
        font-family: 'Orbitron', sans-serif;
    }

    /* 🔱 3D AVENGERS CHROME LOGO (REFINED) */
    .arkon-logo {
        font-family: 'Exo 2', sans-serif; /* Avengers style thick italic font */
        font-size: 140px; font-weight: 900; text-align: center;
        /* Ultimate 3D Metallic Chrome Gradient */
        background: linear-gradient(to bottom, #ffffff 0%, #d1d1d1 20%, #2c3e50 45%, #000000 50%, #34495e 55%, #bdc3c7 80%, #ffffff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        /* Bevel & Emboss with Neon Blue Glow */
        filter: drop-shadow(4px 4px 0px rgba(0, 210, 255, 0.8)) drop-shadow(-2px -2px 0px #fff);
        letter-spacing: 15px; text-transform: uppercase;
        transform: skew(-15deg); font-style: italic;
        margin-top: 40px;
        animation: glow-pulse 2s infinite alternate;
    }
    @keyframes glow-pulse {
        from { filter: drop-shadow(0 0 10px rgba(0, 210, 255, 0.4)); }
        to { filter: drop-shadow(0 0 40px rgba(0, 210, 255, 0.9)); }
    }

    /* 🔱 KINETIC BLINKING NEON HUD CARDS */
    .hud-card {
        background: rgba(0, 30, 60, 0.15); /* Ultra Transparent Jarvis Feel */
        border: 2px solid #00D2FF;
        padding: 35px 20px; border-radius: 5px; text-align: center;
        backdrop-filter: blur(15px);
        /* The Pulsing Border you liked */
        animation: border-pulse 3s infinite ease-in-out;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.1);
    }
    @keyframes border-pulse {
        0%, 100% { border-color: rgba(0, 210, 255, 0.2); box-shadow: 0 0 5px rgba(0, 210, 255, 0.1); }
        50% { border-color: rgba(0, 210, 255, 1); box-shadow: 0 0 40px rgba(0, 210, 255, 0.5); }
    }

    /* 🔱 FUTURISTIC STATUS TEXT */
    .status-text {
        font-size: 14px; letter-spacing: 4px; color: #FFFFFF;
        text-transform: uppercase; font-weight: bold;
        text-shadow: 0 0 10px #00D2FF;
        animation: text-blink 1.5s infinite;
    }
    @keyframes text-blink {
        0%, 100% { opacity: 1; } 50% { opacity: 0.5; }
    }

    /* 🔱 THE ARC REACTOR HEARTBEAT */
    .heart-core {
        width: 190px; height: 190px; border-radius: 50%;
        background: radial-gradient(circle, #ffffff 0%, #00D2FF 45%, #000000 100%);
        border: 4px solid #00D2FF; margin: auto;
        box-shadow: 0 0 70px #00D2FF, inset 0 0 40px #00D2FF;
        animation: core-beat 2s infinite;
    }
    @keyframes core-beat {
        0% { transform: scale(1); filter: brightness(1); }
        50% { transform: scale(1.08); filter: brightness(1.6); }
        100% { transform: scale(1); filter: brightness(1); }
    }

    .metric { font-size: 60px; font-weight: 900; color: #FFFFFF; text-shadow: 0 0 30px #00D2FF; }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00D2FF; letter-spacing:12px; font-size:16px; opacity:0.8; font-weight:bold;'>JARVIS PROTOCOL ACTIVE | MASTER: ARCHITECT KRISHNA</p>", unsafe_allow_html=True)

# --- 🔱 CLEAR HUD DISPLAY ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    st.markdown("""
        <div class="hud-card">
            <p style='color:#8ab4f8; letter-spacing:3px;'>NEURAL BRAIN STORAGE</p>
            <div class="metric">99.9%</div>
            <p class="status-text">SYNAPSES: STABLE</p>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown('<div class="heart-core"></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:20px; font-weight:bold; letter-spacing:5px; color:#00D2FF; text-shadow: 0 0 10px #00D2FF;'>ARC REACTOR CORE</p>", unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="hud-card">
            <p style='color:#8ab4f8; letter-spacing:3px;'>QUANTUM PROCESSING</p>
            <div class="metric">4.2 ms</div>
            <p class="status-text">LATENCY: OPTIMAL</p>
        </div>
    """, unsafe_allow_html=True)

# --- 🔱 COMMAND INTERFACE ---
st.write("---")
st.markdown("<h3 style='text-align:center; color:#00D2FF; letter-spacing:5px;'>🎙️ SOVEREIGN COMMAND CENTER</h3>", unsafe_allow_html=True)

col_x, col_y, col_z = st.columns([1, 2, 1])
with col_y:
    audio_data = mic_recorder(
        start_prompt="🔱 ENGAGE JARVIS SENSES",
        stop_prompt="🛑 ANALYZE MANDATE",
        key='arkon_clear_mic'
    )

if audio_data:
    r = sr.Recognizer()
    audio_bytes = audio_data['bytes']
    with st.spinner("🔱 DECODING NEURAL FREQUENCY..."):
        try:
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
            wav_io = io.BytesIO()
            audio_segment.export(wav_io, format="wav")
            wav_io.seek(0)
            with sr.AudioFile(wav_io) as source:
                recorded_audio = r.record(source)
                command = r.recognize_google(recorded_audio)
                st.markdown(f"""
                <div class="hud-card" style="border-color:#FFFFFF; background:rgba(255,255,255,0.1);">
                    <h2 style='color:#FFFFFF; margin:0;'>🔱 ARKON OBEYS:</h2>
                    <p style='font-size:35px; color:#00D2FF; font-weight:900;'>"{command.upper()}"</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ SIGNAL ERROR: {e}")

st.markdown("<p style='text-align:center; opacity:0.4; margin-top:100px;'>PROTOTYPE MARK-V | SECURED BY ARCHITECT KRISHNA</p>", unsafe_allow_html=True)
