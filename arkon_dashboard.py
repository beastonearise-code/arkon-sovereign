import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import io
import time
import requests

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: JARVIS MARK-IV", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 IRON MAN JARVIS CSS AESTHETIC ---
st.markdown("""
<style>
    /* Import futuristic fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@400;700&display=swap');
    
    /* Main Background: Deep Space Blue with Scanline Overlay */
    .stApp {
        background: radial-gradient(ellipse at center, #020c1b 0%, #0a192f 100%);
        color: #00D2FF;
        font-family: 'Orbitron', sans-serif;
        overflow-x: hidden;
    }
    /* Scanline Effect Overlay */
    .stApp::after {
        content: "";
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(transparent 50%, rgba(0, 210, 255, 0.05) 50%);
        background-size: 100% 4px;
        z-index: 9999; pointer-events: none;
    }

    /* 🔱 1. AVENGERS STYLE METALLIC LOGO */
    .arkon-logo {
        font-size: 120px; font-weight: 900; text-align: center;
        /* Metallic Gradient applied to text */
        background: linear-gradient(to bottom, #ffffff 0%, #a9a9a9 30%, #4682b4 50%, #000080 70%, #00d2ff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        /* Deep Glowing Shadows */
        filter: drop-shadow(0 0 20px rgba(0, 210, 255, 0.8)) drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
        letter-spacing: 25px; margin-bottom: -20px; text-transform: uppercase;
        /* The iconic Avengers skew */
        transform: skew(-12deg); font-style: italic;
    }

    /* Subheader Styling */
    .subheader-text {
        text-align: center; color: #00D2FF; letter-spacing: 8px; font-size: 18px;
        opacity: 0.8; text-transform: uppercase; font-family: 'Roboto Mono', monospace;
        text-shadow: 0 0 10px rgba(0, 210, 255, 0.5);
    }

    /* 🔱 2 & 3. HUD CARDS WITH BLINKING BORDERS */
    .hud-card {
        background: rgba(0, 20, 40, 0.6); /* Transparent dark blue */
        border: 2px solid rgba(0, 210, 255, 0.3);
        padding: 30px; border-radius: 15px; text-align: center;
        backdrop-filter: blur(10px); /* Glass effect */
        /* The Pulgin Border Animation */
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.1), inset 0 0 20px rgba(0, 210, 255, 0.05);
        animation: border-pulse 3s infinite alternate ease-in-out;
    }

    /* Keyframes for Border Blinking/Pulsing */
    @keyframes border-pulse {
        0% {
            border-color: rgba(0, 210, 255, 0.3);
            box-shadow: 0 0 15px rgba(0, 210, 255, 0.2), inset 0 0 10px rgba(0, 210, 255, 0.1);
        }
        100% {
            border-color: rgba(0, 210, 255, 1); /* Brightest flash */
            box-shadow: 0 0 50px rgba(0, 210, 255, 0.8), inset 0 0 30px rgba(0, 210, 255, 0.4);
        }
    }

    .metric { font-size: 60px; font-weight: bold; color: #FFFFFF; text-shadow: 0 0 20px #00D2FF; }
    .card-title { font-family: 'Roboto Mono', monospace; color: #8ab4f8; letter-spacing: 2px; font-size: 16px; }

    /* 🔱 4. BLINKING TEXT STATUS */
    .blink-status {
        font-family: 'Roboto Mono', monospace; color: #00D2FF; letter-spacing: 2px;
        font-weight: bold; text-transform: uppercase;
        animation: text-flicker 2s infinite steps(1); /* Robotic flicker */
    }
    @keyframes text-flicker {
        0%, 100% { opacity: 1; text-shadow: 0 0 10px #00D2FF; }
        50% { opacity: 0.5; text-shadow: none; }
    }

    /* 🔱 PULSING HEARTBEAT (ARC REACTOR CORE) */
    .heart-core {
        width: 180px; height: 180px; border-radius: 50%;
        background: radial-gradient(circle, #ffffff 0%, #00D2FF 30%, #000080 60%, #000 100%);
        border: 5px solid #00D2FF; margin: auto;
        box-shadow: 0 0 80px #00D2FF, inset 0 0 50px #00D2FF;
        animation: reactor-pulse 2s infinite ease-in-out;
    }
    @keyframes reactor-pulse {
        0% { transform: scale(1); filter: brightness(1); }
        50% { transform: scale(1.05); filter: brightness(1.5); box-shadow: 0 0 120px #00D2FF, inset 0 0 80px #00D2FF; }
        100% { transform: scale(1); filter: brightness(1); }
    }

    /* Command Button Styling */
    div.stButton > button {
        background: linear-gradient(to right, rgba(0, 0, 128, 0.8), rgba(0, 210, 255, 0.8)) !important;
        color: #FFFFFF !important; border: 2px solid #00D2FF !important;
        border-radius: 10px !important; font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important; padding: 15px 30px !important; width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.3);
    }
    div.stButton > button:hover {
        background: #00D2FF !important;
        box-shadow: 0 0 50px rgba(0, 210, 255, 0.8) !important;
        transform: translateY(-3px);
    }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER & AVENGERS LOGO ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p class='subheader-text'>JARVIS SYSTEM MARK-IV | ARCHITECT KRISHNA ONLINE</p>", unsafe_allow_html=True)

# --- 🔱 IRON MAN HUD DISPLAY ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    # Blinking Border Card + Blinking Text Status
    st.markdown("""
        <div class="hud-card">
            <p class="card-title">NEURAL INTEGRITY</p>
            <div class="metric">99.9%</div>
            <p class="blink-status">STATUS: STABLE</p>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown('<div class="heart-core"></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:20px; color:#00D2FF; font-weight:bold; letter-spacing:3px; text-shadow: 0 0 10px #00D2FF;'>ARC REACTOR CORE</p>", unsafe_allow_html=True)

with c3:
    # Blinking Border Card + Blinking Text Status
    st.markdown("""
        <div class="hud-card">
            <p class="card-title">PROCESSING SPEED</p>
            <div class="metric">4.2 ms</div>
            <p class="blink-status">LATENCY: OPTIMAL</p>
        </div>
    """, unsafe_allow_html=True)

# --- 🔱 COMMAND CENTER (Holographic) ---
st.write("##")
st.markdown("<h3 style='text-align:center; color:#00D2FF; text-shadow: 0 0 15px #00D2FF;'>🎙️ VOCAL COMMAND INTERFACE</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    audio_data = mic_recorder(
        start_prompt="⚡ ENGAGE SYSTEMS",
        stop_prompt="🛑 TERMINATE INPUT",
        key='arkon_iron_mic'
    )

if audio_data:
    r = sr.Recognizer()
    audio_bytes = audio_data['bytes']
    
    with st.spinner("🔱 ANALYZING WAVEFORM PATTERN..."):
        try:
            # Convert WebM to WAV (Crucial for Cloud)
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
            wav_io = io.BytesIO()
            audio_segment.export(wav_io, format="wav")
            wav_io.seek(0)

            with sr.AudioFile(wav_io) as source:
                recorded_audio = r.record(source)
                command = r.recognize_google(recorded_audio)
                
                st.markdown(f"""
                <div class="hud-card" style="margin-top: 20px; animation: none; border-color: #FFFFFF; background: rgba(0, 210, 255, 0.2);">
                    <h3 style="color:#FFFFFF; margin:0; text-shadow: 0 0 10px #FFFFFF;">COMMAND RECOGNIZED:</h3>
                    <p style="font-size:35px; color:#00D2FF; font-weight:bold; text-transform:uppercase; text-shadow: 0 0 20px #00D2FF;">"{command}"</p>
                </div>
                """, unsafe_allow_html=True)
        except sr.UnknownValueError:
            st.error("❌ SIGNAL INTERFERENCE. RE-ENGAGE.")
        except Exception as e:
            st.error(f"❌ SYSTEM FAILURE: {e}")

# --- 🔱 SECURE VAULT ---
st.write("##")
with st.expander("📂 ACCESS CLASSIFIED PROTOCOLS"):
    st.markdown("""
        <div style="font-family: 'Roboto Mono', monospace; color: #00D2FF;">
            > INITIATING SECURITY SCAN...<br>
            > BIOMETRICS: ARCHITECT KRISHNA - CONFIRMED<br>
            > FIREWALL: ACTIVE (QUANTUM ENCRYPTION)<br>
            > AI CORE: ONLINE
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='stApp' style='height: 50px; background: transparent;'></div>", unsafe_allow_html=True) # Spacer
st.markdown("<p style='text-align:center; opacity:0.6; color:#00D2FF; font-family:Roboto Mono;'>STARK INDUSTRIES PROTOTYPE v4.1 | POWERED BY ARC TECHNOLOGY</p>", unsafe_allow_html=True)
