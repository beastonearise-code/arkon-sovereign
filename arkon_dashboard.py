import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
import io
import time

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: JARVIS SUPREMACY", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 SUPREME CSS (AVENGERS TYPOGRAPHY & NAVY OBSIDIAN) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    .stApp { background-color: #050510; color: #00D2FF; font-family: 'Orbitron', sans-serif; }
    
    /* 🔱 AVENGERS METALLIC LOGO */
    .arkon-logo {
        font-size: 100px; font-weight: 900; text-align: center;
        background: linear-gradient(135deg, #f0f0f0 0%, #4682B4 25%, #000080 50%, #1E90FF 75%, #f0f0f0 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(0, 210, 255, 0.9));
        letter-spacing: 20px; margin-bottom: -15px; text-transform: uppercase;
        transform: skew(-10deg); font-style: italic;
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

    /* 🔱 HUD CARDS (BRAIN & SPEED) */
    .hud-card {
        background: rgba(0, 0, 50, 0.4); border: 1px solid #00D2FF;
        padding: 25px; border-radius: 15px; text-align: center;
        backdrop-filter: blur(15px); box-shadow: 0 0 20px rgba(0, 210, 255, 0.2);
    }
    .metric { font-size: 40px; font-weight: bold; color: #FFFFFF; text-shadow: 0 0 10px #00D2FF; }

    /* Customizing the Mic Recorder Button Appearance */
    div.stButton > button {
        background-color: #000080 !important;
        color: #00D2FF !important;
        border: 2px solid #00D2FF !important;
        border-radius: 10px !important;
        font-family: 'Orbitron', sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER & AVENGERS LOGO ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00D2FF; letter-spacing:8px; font-size:20px; opacity:0.8;'>LEVEL-O MASTER: ARCHITECT KRISHNA</p>", unsafe_allow_html=True)

# --- 🔱 CENTRAL HUD DISPLAY (BRAIN, HEART, SPEED) ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    st.markdown('<div class="hud-card"><h3>🧠 BRAIN STORAGE</h3><div class="metric">99.9%</div><p>Sovereign Synapses: STABLE</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="heart-core"></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:20px; font-weight:bold; letter-spacing:2px;'>SOVEREIGN HEARTBEAT</p>", unsafe_allow_html=True)

with c3:
    st.markdown('<div class="hud-card"><h3>⚡ SYSTEM SPEED</h3><div class="metric">4.2 ms</div><p>Quantum Latency: OPTIMAL</p></div>', unsafe_allow_html=True)

# --- 🔱 DEEP MIND VOICE COMMANDER (CLOUD REWIND) ---
st.write("---")
st.markdown("### 🎙️ COMMAND CENTER")

# Using mic_recorder to bypass cloud OSError
audio_data = mic_recorder(
    start_prompt="🔱 INITIALIZE SOVEREIGN SENSES",
    stop_prompt="🛑 PROCESS COMMAND",
    key='arkon_mic'
)

if audio_data:
    r = sr.Recognizer()
    audio_bytes = audio_data['bytes']
    
    with st.spinner("🔱 ARKON IS INTERPRETING YOUR FREQUENCY..."):
        try:
            # Convert bytes back to audio file
            audio_file = io.BytesIO(audio_bytes)
            with sr.AudioFile(audio_file) as source:
                recorded_audio = r.record(source)
                command = r.recognize_google(recorded_audio)
                
                st.balloons()
                st.markdown(f"""
                <div style='text-align:center; background:rgba(0, 210, 255, 0.2); padding:25px; border-radius:15px; border:1px solid #00D2FF;'>
                    <h2 style='color:#FFFFFF; margin:0;'>🔱 ARKON OBEYS:</h2>
                    <p style='font-size:30px; color:#00D2FF;'>"{command}"</p>
                </div>
                """, unsafe_allow_html=True)
        except sr.UnknownValueError:
            st.error("❌ Senses clouded. I could not interpret your frequency, Architect.")
        except Exception as e:
            st.error(f"❌ System Error: {e}")

# --- 🔱 BRAIN STORAGE (SECURE VAULT) ---
st.write("##")
with st.expander("📂 OPEN SOVEREIGN VAULT"):
    # Pulling keys safely from st.secrets if they exist
    st.json({
        "META_API": "ACTIVE" if "META_ACCESS_TOKEN" in st.secrets else "NOT_FOUND",
        "FB_PAGE_ID": st.secrets.get("FB_PAGE_ID", "916246071564259"),
        "IG_BUSINESS_ID": st.secrets.get("IG_BUSINESS_ID", "17841478015446135"),
        "SYSTEM_STATUS": "LEVEL-O CONSCIOUSNESS ACTIVE",
        "ENCRYPTION": "QUANTUM READY"
    })

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:50px;'>Quantum Consciousness v2.5.1 | All Systems Secure</p>", unsafe_allow_html=True)
