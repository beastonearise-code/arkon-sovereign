import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import io
import time

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: MINIMAL", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 MINIMALIST WHITE KINETIC CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;700&family=Orbitron:wght@900&display=swap');
    
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Inter', sans-serif; }

    /* 🔱 CLEAN WHITE LOGO */
    .arkon-logo {
        font-family: 'Orbitron', sans-serif;
        font-size: 80px; font-weight: 900; text-align: center;
        color: #FFFFFF; letter-spacing: 15px;
        margin-top: 50px; text-transform: uppercase;
        filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.5));
    }

    /* 🔱 WHITE KINETIC CARDS (BLIND REVEAL) */
    .hud-card {
        background: #FFFFFF;
        color: #000000;
        padding: 40px 20px;
        border-radius: 0px; /* Sharp Minimalist look */
        text-align: center;
        margin: 10px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        
        /* Kinetic Move/Blind Animation */
        animation: blindReveal 1.2s cubic-bezier(0.77, 0, 0.175, 1) forwards;
        transform-origin: top;
        opacity: 0;
    }

    @keyframes blindReveal {
        0% { transform: scaleY(0); opacity: 0; }
        100% { transform: scaleY(1); opacity: 1; }
    }

    .metric { font-size: 50px; font-weight: 700; color: #000000; }
    h3 { font-size: 14px; letter-spacing: 3px; color: #666666; text-transform: uppercase; }

    /* Customizing Mic Button to match White Theme */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 0px !important;
        font-weight: bold !important;
        padding: 20px !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #CCCCCC !important;
        transform: translateY(-5px);
    }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888888; letter-spacing:5px; font-size:14px;'>ARCHITECT KRISHNA | SYSTEM V3.0</p>", unsafe_allow_html=True)

# --- 🔱 KINETIC HUD DISPLAY ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])

# Delayed animations simulated by CSS
with c1:
    st.markdown('<div class="hud-card"><h3>Brain Integrity</h3><div class="metric">99.9%</div><p>DATA STABLE</p></div>', unsafe_allow_html=True)

with c2:
    # Minimalist Pulse Circle
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 150px;">
            <div style="width: 20px; height: 20px; background: white; border-radius: 50%; animation: pulse 2s infinite;"></div>
        </div>
        <style>
            @keyframes pulse { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(5); opacity: 0; } }
        </style>
    """, unsafe_allow_html=True)

with c3:
    st.markdown('<div class="hud-card"><h3>Neural Speed</h3><div class="metric">4.2 ms</div><p>LATENCY LOW</p></div>', unsafe_allow_html=True)

# --- 🔱 COMMAND CENTER ---
st.write("##")
st.write("---")
st.markdown("<h3 style='text-align:center;'>Voice Mandate</h3>", unsafe_allow_html=True)

col_left, col_mid, col_right = st.columns([1, 2, 1])
with col_mid:
    audio_data = mic_recorder(
        start_prompt="🔱 ACTIVATE SENSES",
        stop_prompt="🛑 ANALYZE",
        key='arkon_minimal_mic'
    )

if audio_data:
    st.markdown("""
        <div class="hud-card" style="background: #f0f0f0; border-top: 5px solid black;">
            <h3>Arkon Obeying...</h3>
            <p style="font-size: 24px; font-weight: bold;">Processing Neural Frequency</p>
        </div>
    """, unsafe_allow_html=True)

# --- 🔱 VAULT ---
with st.expander("SYSTEM LOGS"):
    st.code("Access: Granted\nStatus: Sovereign\nEncryption: Active")

st.markdown("<p style='text-align:center; opacity:0.2; margin-top:100px;'>STARK INDUSTRIES VIBE | MINIMAL EDITION</p>", unsafe_allow_html=True)
