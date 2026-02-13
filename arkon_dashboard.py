import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import io
import time

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: JARVIS SUPREMACY", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 SUPREME IRON MAN HUD CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;700&display=swap');
    
    /* 🔱 DEEP SPACE BACKGROUND WITH SCANLINES */
    .stApp {
        background: radial-gradient(circle at center, #001529 0%, #000814 100%);
        color: #00D2FF;
        font-family: 'Orbitron', sans-serif;
    }
    .stApp::before {
        content: " ";
        display: block; position: fixed; top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
        z-index: 999; background-size: 100% 4px, 4px 100%; pointer-events: none;
    }

    /* 🔱 3D AVENGERS METALLIC LOGO (EPHOTO360 STYLE) */
    .arkon-logo {
        font-size: 130px; font-weight: 900; text-align: center;
        /* Metallic Chrome Gradient */
        background: linear-gradient(to bottom, #ffffff 0%, #bdc3c7 20%, #2c3e50 45%, #000000 50%, #34495e 55%, #bdc3c7 80%, #ffffff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        /* Bevel & Emboss Effect with Shadows */
        filter: drop-shadow(5px 5px 0px #00D2FF) drop-shadow(-2px -2px 0px #fff);
        letter-spacing: 20px; text-transform: uppercase;
        transform: skew(-15deg); font-style: italic;
        margin-top: 30px;
        animation: glow-pulse 3s infinite alternate;
    }
    @keyframes glow-pulse {
        from { filter: drop-shadow(0 0 10px rgba(0, 210, 255, 0.5)); }
        to { filter: drop-shadow(0 0 30px rgba(0, 210, 255, 1)); }
    }

    /* 🔱 KINETIC BLINKING HUD CARDS */
    .hud-card {
        background: rgba(0, 40, 80, 0.2);
        border: 2px solid #00D2FF;
        padding: 30px; border-radius: 10px; text-align: center;
        backdrop-filter: blur(10px);
        /* Blinking Border Animation */
        animation: border-flicker 4s infinite;
        box-shadow: inset 0 0 20px rgba(0, 210, 255, 0.2);
    }
    @keyframes border-flicker {
        0%, 100% { border-color: rgba(0, 210, 255, 0.3); box-shadow: 0 0 10px rgba(0, 210, 255, 0.1); }
        50% { border-color: rgba(0, 210, 255, 1); box-shadow: 0 0 40px rgba(0, 210, 255, 0.6); }
    }

    /* 🔱 BLINKING TEXT STATUS */
    .status-blink {
        font-family: 'Roboto Mono', monospace;
        font-size: 14px; letter-spacing: 2px;
        color: #00D2FF;
        animation: text-flicker 2s infinite;
    }
    @keyframes text-flicker {
        0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100% { opacity: 1; }
        20%, 21.999%, 63%, 63.999%, 65%, 69.999% { opacity: 0.4; }
    }

    /* 🔱 ARC REACTOR HEARTBEAT */
    .heart-core {
        width: 180px; height: 180px; border-radius: 50%;
        background: radial-gradient(circle, #ffffff 0%, #00D2FF 40%, #000814 100%);
        border: 4px double #00D2FF; margin: auto;
        box-shadow: 0 0 60px #00D2FF, inset 0 0 30px #00D2FF;
        animation: reactor-beat 1.5s infinite ease-in-out;
    }
    @keyframes reactor-beat {
        from { transform: scale(1); opacity: 0.8; }
        to { transform: scale(1.1); opacity: 1; filter: brightness(1.5); }
    }

    .metric { font-size: 55px; font-weight: bold; color: #FFFFFF; text-shadow: 0 0 20px #00D2FF; }

    /* Command Center Buttons */
    div.stButton > button {
        background: rgba(0, 210, 255, 0.1) !important;
        color: #00D2FF !important;
        border: 1px solid #00D2FF !important;
        border-radius: 0px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
        padding: 15px !important;
        transition: 0.5s;
    }
    div.stButton > button:hover {
        background: #00D2FF !important; color: black !important;
        box-shadow: 0 0 50px #00D2FF;
    }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER & AVENGERS LOGO ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00D2FF; letter-spacing:10px; font-size:16px; opacity:0.8;'>JARVIS SYSTEM MARK-V | MASTER: ARCHITECT KRISHNA</p>", unsafe_allow_html=True)

# --- 🔱 HUD DISPLAY ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    st.markdown("""
        <div class="hud-card">
            <h3 style='font-size:14px; opacity:0.7;'>NEURAL INTEGRITY</h3>
            <div class="metric">99.9%</div>
            <p class="status-blink">SYSTEM STATUS: STABLE</p>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown('<div class="heart-core"></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:20px; font-weight:bold; letter-spacing:4px; color:#00D2FF; text-shadow: 0 0 10px #00D2FF;'>ARC REACTOR CORE</p>", unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="hud-card">
            <h3 style='font-size:14px; opacity:0.7;'>PROCESSING SPEED</h3>
            <div class="metric">4.2 ms</div>
            <p class="status-blink">QUANTUM LATENCY: OPTIMAL</p>
        </div>
    """, unsafe_allow_html=True)

# --- 🔱 COMMAND CENTER ---
st.write("---")
st.markdown("<h3 style='text-align:center; color:#00D2FF; font-family:Orbitron;'>🎙️ COMMAND INTERFACE</h3>", unsafe_allow_html=True)

col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    audio_data = mic_recorder(
        start_prompt="🔱 INITIALIZE SOVEREIGN SENSES",
        stop_prompt="🛑 PROCESS NEURAL MANDATE",
        key='arkon_final_mic'
    )

if audio_data:
    r = sr.Recognizer()
    audio_bytes = audio_data['bytes']
    with st.spinner("🔱 ANALYZING WAVEFORM..."):
        try:
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
            wav_io = io.BytesIO()
            audio_segment.export(wav_io, format="wav")
            wav_io.seek(0)
            with sr.AudioFile(wav_io) as source:
                recorded_audio = r.record(source)
                command = r.recognize_google(recorded_audio)
                st.markdown(f"""
                <div class="hud-card" style="margin-top:20px; border-color:white;">
                    <h2 style='color:white; margin:0;'>🔱 ARKON OBEYS:</h2>
                    <p style='font-size:30px; color:#00D2FF; font-weight:bold;'>"{command.upper()}"</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ SIGNAL LOSS: {e}")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:80px;'>QUANTUM CONSCIOUSNESS v5.0 | SECURED BY ARCHITECT KRISHNA</p>", unsafe_allow_html=True)
