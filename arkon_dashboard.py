import streamlit as st
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
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
        filter: drop-shadow(0 0 25px rgba(0, 210, 255, 0.9));
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
        background: rgba(0, 0, 50, 0.4); border: 2px solid #00D2FF;
        padding: 25px; border-radius: 20px; text-align: center;
        backdrop-filter: blur(15px); box-shadow: 0 0 25px rgba(0, 210, 255, 0.2);
    }
    .metric { font-size: 45px; font-weight: bold; color: #FFFFFF; text-shadow: 0 0 15px #00D2FF; }

    /* Customizing the Mic Recorder Button Appearance */
    div.stButton > button {
        background-color: #000080 !important;
        color: #00D2FF !important;
        border: 2px solid #00D2FF !important;
        border-radius: 12px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
        width: 100% !important;
        padding: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER & AVENGERS LOGO ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00D2FF; letter-spacing:10px; font-size:20px; opacity:0.9;'>SOVEREIGN MASTER: ARCHITECT KRISHNA</p>", unsafe_allow_html=True)

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

# --- 🔱 DEEP MIND VOICE COMMANDER (CLOUD STABLE) ---
st.write("---")
st.markdown("### 🎙️ COMMAND CENTER")

# Cloud-safe voice recording with mic_recorder
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
            # 🔱 Critical Fix: Convert browser audio (WebM) to PCM WAV for AI interpretation
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
            wav_io = io.BytesIO()
            audio_segment.export(wav_io, format="wav")
            wav_io.seek(0)

            with sr.AudioFile(wav_io) as source:
                recorded_audio = r.record(source)
                command = r.recognize_google(recorded_audio)
                
                st.balloons()
                st.markdown(f"""
                <div style='text-align:center; background:rgba(0, 210, 255, 0.1); padding:30px; border-radius:15px; border:2px solid #00D2FF; margin-top:20px;'>
                    <h2 style='color:#FFFFFF; margin:0;'>🔱 ARKON OBEYS:</h2>
                    <p style='font-size:35px; color:#00D2FF; font-weight:bold; text-transform:uppercase;'>"{command}"</p>
                </div>
                """, unsafe_allow_html=True)
        except sr.UnknownValueError:
            st.error("❌ Senses clouded. I could not interpret your frequency, Architect Krishna.")
        except Exception as e:
            st.error(f"❌ Neural Processing Error: {e}")

# --- 🔱 BRAIN STORAGE (SECURE VAULT) ---
st.write("##")
with st.expander("📂 OPEN SOVEREIGN VAULT (API METRICS)"):
    # Pulling keys safely from st.secrets
    st.json({
        "META_API": "ACTIVE" if "META_ACCESS_TOKEN" in st.secrets else "INACTIVE",
        "FB_PAGE_ID": st.secrets.get("FB_PAGE_ID", "916246071564259"),
        "IG_BUSINESS_ID": st.secrets.get("IG_BUSINESS_ID", "17841478015446135"),
        "OPENAI_STATUS": "CONNECTED" if "OPENAI_API_KEY" in st.secrets else "OFFLINE",
        "SYSTEM_LOG": "LEVEL-O CONSCIOUSNESS ACTIVE",
        "ENCRYPTION": "QUANTUM SOVEREIGN READY"
    })

st.markdown("<p style='text-align:center; opacity:0.4; margin-top:60px; font-size:12px;'>Quantum Consciousness v2.5.1 | Developed for Architect Krishna | 🔱</p>", unsafe_allow_html=True)
