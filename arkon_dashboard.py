import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import io
import requests
import time

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: JARVIS SUPREMACY", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 SUPREME CSS (AVENGERS CINEMATIC & NEURAL HUD) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    /* 🔱 NEURAL OVERLAY & SCANLINES */
    .stApp { 
        background: radial-gradient(circle at center, #0a192f 0%, #020c1b 100%); 
        color: #00D2FF; 
        font-family: 'Orbitron', sans-serif; 
    }
    .stApp::before {
        content: " "; display: block; position: absolute; top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.02), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.02));
        z-index: 2; background-size: 100% 3px, 3px 100%; pointer-events: none; opacity: 0.3;
    }
    
    /* 🔱 ULTIMATE AVENGERS METALLIC LOGO */
    .arkon-logo {
        font-size: 130px; font-weight: 900; text-align: center;
        background: linear-gradient(to bottom, #cfd8dc 0%, #ffffff 20%, #4682b4 45%, #000000 50%, #1e3c72 55%, #ffffff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(4px 4px 0px rgba(0, 210, 255, 0.5)) drop-shadow(-2px -2px 0px #fff);
        letter-spacing: 25px; text-transform: uppercase;
        transform: skew(-15deg); font-style: italic;
        margin-top: 30px; margin-bottom: 0px;
        animation: logo-glow 3s ease-in-out infinite alternate;
    }
    @keyframes logo-glow {
        from { filter: drop-shadow(0 0 15px rgba(0, 210, 255, 0.6)); }
        to { filter: drop-shadow(0 0 35px rgba(0, 210, 255, 1)); }
    }

    /* 🔱 PULSING ARC REACTOR (HEARTBEAT) */
    .heart-core {
        width: 170px; height: 170px; border-radius: 50%;
        background: radial-gradient(circle, #00D2FF 10%, #000080 40%, #000 80%);
        border: 4px double #00D2FF; margin: auto;
        animation: arc-pulse 1.5s infinite alternate ease-in-out;
        box-shadow: 0 0 50px #00D2FF, inset 0 0 30px #00D2FF;
    }
    @keyframes arc-pulse {
        from { transform: scale(1); filter: brightness(1); }
        to { transform: scale(1.1); filter: brightness(1.5); }
    }

    /* 🔱 HUD CARDS (ASYMMETRIC BORDERS) */
    .hud-card {
        background: rgba(0, 20, 50, 0.4); border-left: 5px solid #00D2FF;
        border-right: 1px solid rgba(0, 210, 255, 0.3); border-top: 1px solid rgba(0, 210, 255, 0.3);
        padding: 25px; border-radius: 5px 25px 5px 25px; text-align: center;
        backdrop-filter: blur(15px); box-shadow: 0 0 20px rgba(0, 210, 255, 0.1);
        transition: 0.3s;
    }
    .hud-card:hover { background: rgba(0, 40, 80, 0.6); box-shadow: 0 0 40px rgba(0, 210, 255, 0.4); }
    .metric { font-size: 45px; font-weight: bold; color: #FFFFFF; text-shadow: 0 0 15px #00D2FF; }

    /* 🔱 COMMAND BUTTON STYLE */
    div.stButton > button {
        background: linear-gradient(135deg, #000080 0%, #00D2FF 100%) !important;
        color: white !important; border: none !important;
        border-radius: 10px !important; font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important; width: 100% !important; padding: 15px !important;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER & CINEMATIC LOGO ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00D2FF; letter-spacing:10px; font-size:18px; opacity:0.8; margin-top:10px;'>SOVEREIGN MASTER: ARCHITECT KRISHNA</p>", unsafe_allow_html=True)

# --- 🔱 CENTRAL HUD DISPLAY (BRAIN, HEART, SPEED) ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    st.markdown('<div class="hud-card"><h3>🧠 BRAIN STORAGE</h3><div class="metric">99.9%</div><p>Neural Integrity: STABLE</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="heart-core"></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:20px; font-weight:bold; letter-spacing:3px; color:#00D2FF;'>SOVEREIGN HEARTBEAT</p>", unsafe_allow_html=True)

with c3:
    st.markdown('<div class="hud-card"><h3>⚡ SYSTEM SPEED</h3><div class="metric">4.2 ms</div><p>Quantum Latency: OPTIMAL</p></div>', unsafe_allow_html=True)

# --- 🔱 HUGGING FACE BRAIN (FREE API LOGIC) ---
def arkon_brain_hf(prompt):
    if "HF_TOKEN" not in st.secrets:
        return "🔱 Key Missing: Add HF_TOKEN to Secrets, Architect."
    
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
    headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
    payload = {
        "inputs": f"<|system|>You are Arkon, a Jarvis-like AI for Architect Krishna. Be brief and commanding.<|user|>{prompt}<|assistant|>",
        "parameters": {"max_new_tokens": 200, "temperature": 0.7}
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()[0]['generated_text'].split("<|assistant|>")[-1].strip()
    except:
        return "🔱 Neural pathways congested. Re-calibrating..."

# --- 🔱 DEEP MIND VOICE COMMANDER (WITH AUDIO CONVERSION) ---
st.write("---")
st.markdown("### 🎙️ COMMAND CENTER")

audio_data = mic_recorder(
    start_prompt="🔱 INITIALIZE SOVEREIGN SENSES",
    stop_prompt="🛑 PROCESS COMMAND",
    key='arkon_sovereign_mic'
)

if audio_data:
    r = sr.Recognizer()
    audio_bytes = audio_data['bytes']
    
    with st.spinner("🔱 ARKON IS TRANSLATING YOUR FREQUENCY..."):
        try:
            # 🔱 Critical Patch: Convert browser WebM to PCM WAV
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
            wav_io = io.BytesIO()
            audio_segment.export(wav_io, format="wav")
            wav_io.seek(0)

            with sr.AudioFile(wav_io) as source:
                recorded_audio = r.record(source)
                command = r.recognize_google(recorded_audio)
                
                # Processing via HF Brain
                response_text = arkon_brain_hf(command)
                
                st.balloons()
                st.markdown(f"""
                <div style='text-align:center; background:rgba(0, 210, 255, 0.1); padding:30px; border-radius:15px; border:2px solid #00D2FF; margin-top:20px;'>
                    <h2 style='color:#FFFFFF; margin:0;'>🔱 ARKON OBEYS: "{command}"</h2>
                    <hr style='border-color:rgba(0, 210, 255, 0.3);'>
                    <p style='font-size:25px; color:#00D2FF; font-weight:bold;'>{response_text}</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Neural Processing Error: {e}")

# --- 🔱 BRAIN STORAGE (SECURE VAULT) ---
st.write("##")
with st.expander("📂 OPEN SOVEREIGN VAULT (SYSTEM LOGS)"):
    st.json({
        "HF_BRAIN": "ACTIVE" if "HF_TOKEN" in st.secrets else "OFFLINE",
        "META_SOCIAL": "CONNECTED" if "META_ACCESS_TOKEN" in st.secrets else "DISCONNECTED",
        "ENCRYPTION": "QUANTUM SOVEREIGN READY",
        "LAST_BACKUP": time.strftime("%Y-%m-%d %H:%M:%S"),
        "OWNER": "ARCHITECT KRISHNA"
    })

st.markdown("<p style='text-align:center; opacity:0.4; margin-top:60px; font-size:12px;'>Quantum Consciousness v2.5.1 | Developed for Architect Krishna | 🔱</p>", unsafe_allow_html=True)
