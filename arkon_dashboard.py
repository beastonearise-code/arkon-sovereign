import streamlit as st
import speech_recognition as sr
import threading
import time

# --- 🔱 SOVEREIGN HUD CONFIGURATION ---
st.set_page_config(page_title="ARKON: JARVIS SUPREMACY", layout="wide", initial_sidebar_state="collapsed")

# --- 🔱 SUPREME CSS (AVENGERS STYLE & NAVY OBSIDIAN) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    .stApp { background-color: #050510; color: #00D2FF; font-family: 'Orbitron', sans-serif; }
    
    /* 🔱 AVENGERS METALLIC LOGO */
    .arkon-logo {
        font-size: 120px; font-weight: 900; text-align: center;
        background: linear-gradient(135deg, #f0f0f0 0%, #4682B4 25%, #000080 50%, #1E90FF 75%, #f0f0f0 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(0, 210, 255, 0.9));
        letter-spacing: 25px; margin-bottom: -20px; text-transform: uppercase;
        transform: skew(-10deg); font-style: italic;
    }

    /* 🔱 PULSING ARC REACTOR (HEARTBEAT) */
    .heart-core {
        width: 180px; height: 180px; border-radius: 50%;
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
</style>
""", unsafe_allow_html=True)

# --- 🔱 HEADER & AVENGERS LOGO ---
st.markdown('<div class="arkon-logo">ARKON</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00D2FF; letter-spacing:8px; font-size:20px; opacity:0.8;'>LEVEL-O MASTER: ARCHITECT KRISHNA</p>", unsafe_allow_html=True)

# --- 🔱 CENTRAL HUD DISPLAY ---
st.write("##")
c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    st.markdown('<div class="hud-card"><h3>🧠 BRAIN STORAGE</h3><div class="metric">99.9%</div><p>Sovereign Synapses: STABLE</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="heart-core"></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; margin-top:20px; font-weight:bold; letter-spacing:2px;'>SOVEREIGN HEARTBEAT</p>", unsafe_allow_html=True)

with c3:
    st.markdown('<div class="hud-card"><h3>⚡ SYSTEM SPEED</h3><div class="metric">4.2 ms</div><p>Quantum Latency: OPTIMAL</p></div>', unsafe_allow_html=True)

# --- 🔱 DEEP MIND VOICE COMMANDER ---
st.write("---")
st.markdown("### 🎙️ COMMAND CENTER")

if st.button("🔱 INITIALIZE SOVEREIGN SENSES"):
    r = sr.Recognizer()
    # Deep Focus: High sensitivity settings
    r.energy_threshold = 300 
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8
    
    with sr.Microphone() as source:
        status = st.empty()
        status.info("🔱 JARVIS SENSES CALIBRATING... (Stay Silent for 3 Seconds)")
        r.adjust_for_ambient_noise(source, duration=3) # Improved calibration
        status.success("🔱 SENSES ACTIVE. Speak now, Architect.")
        
        try:
            # Listening with deep focus
            audio = r.listen(source, timeout=7, phrase_time_limit=10)
            status.warning("🔱 PROCESSING NEURAL INPUT...")
            command = r.recognize_google(audio)
            st.balloons()
            st.markdown(f"<h2 style='text-align:center; color:#FFFFFF; background:#00D2FF33; padding:20px; border-radius:10px;'>🔱 ARKON OBEYS: '{command}'</h2>", unsafe_allow_html=True)
        except sr.UnknownValueError:
            st.error("❌ Senses clouded. I could not interpret your frequency, Architect.")
        except sr.RequestError:
            st.error("❌ Vocal servers unreachable. Check network integrity.")
        except Exception as e:
            st.error(f"❌ System Error: {e}")

# --- 🔱 BRAIN STORAGE (SECURE VAULT) ---
with st.expander("📂 OPEN SOVEREIGN VAULT"):
    st.json({
        "META_API": "ACTIVE (60-DAY TOKEN)",
        "IG_ID": "17841478015446135",
        "FB_PAGE": "Honey Bite (916246071564259)",
        "ELEVENLABS": "PREMIUM VOCAL READY"
    })

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:50px;'>Quantum Consciousness v2.5.1</p>", unsafe_allow_html=True)
