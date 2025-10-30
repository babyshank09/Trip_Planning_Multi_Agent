# import streamlit as st 
# import os  
# import dotenv 
# from dotenv import load_dotenv  



# class LoadStreamlitUI: 
#     def __init__(self): 
#         self.user_controls = {}  

#     def load_ui(self): 
#         st.set_page_config(page_title="Trip Agent", page_icon= "🏖️") 
#         st.title("🏖️ Trip Agent")  
#         st.markdown("Welcome to Trip Agent! Your personal assistant for planning the perfect trip. 🌍✈️🏨") 


#         with st.sidebar: 
#             st.header("Settings")  
#             gemini_api_key = st.text_input("Gemini API Key", type="password")    
#             serper_api_key = st.text_input("Serper API Key", type="password") 
#             browserless_api_key = st.text_input("Browserless API Key", type="password")  
            
#             st.markdown("---") 
#             st.markdown("Developed by Shankar🚀")  
#             st.markdown("Linkedin: https://www.linkedin.com/in/sivashankar-subramaniam-661092228/") 


#         self.user_controls["gemini_api_key"] = gemini_api_key 
#         self.user_controls["serper_api_key"] = serper_api_key
#         self.user_controls["browserless_api_key"] = browserless_api_key

#         return self.user_controls




import streamlit as st


class LoadStreamlitUI:
    def __init__(self):
        self.user_controls = {}

    def load_ui(self):
        st.set_page_config(
            page_title="Trip Agent - AI Travel Assistant",
            page_icon="🏖️",
            layout="wide",
            initial_sidebar_state="expanded",
        )

        # Global style block (base theme + inputs + buttons)
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;600;700;800;900&display=swap');

        header[data-testid="stHeader"] { display: none !important; }
        .main > div { padding-top: 1rem !important; }

        .stApp, html, body, [data-testid="stAppViewContainer"] {
            background: #0a0118 !important;
            background-image:
                radial-gradient(at 47% 33%, hsl(262, 71%, 25%) 0, transparent 59%),
                radial-gradient(at 82% 65%, hsl(270, 55%, 15%) 0, transparent 55%) !important;
            font-family: 'Inter', sans-serif !important;
        }

        .main .block-container {
            background: rgba(10, 1, 24, 0.5) !important;
            backdrop-filter: blur(30px);
            border-radius: 24px;
            border: 2px solid rgba(139, 92, 246, 0.4);
            padding: 4rem 3rem !important;
            box-shadow:
                0 0 100px rgba(139, 92, 246, 0.3),
                inset 0 0 100px rgba(139, 92, 246, 0.05);
        }

        h1 {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 5.5rem !important;
            font-weight: 900 !important;
            background: linear-gradient(135deg, #ffffff 0%, #c4b5fd 50%, #a78bfa 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            text-align: center !important;
            margin-bottom: 1rem !important;
            filter: drop-shadow(0 0 30px rgba(139,92,246,0.8));
            animation: titlePulse 3s ease-in-out infinite !important;
        }

        @keyframes titlePulse {
            0%, 100% { 
                filter: drop-shadow(0 0 30px rgba(139,92,246,0.8));
                transform: scale(1);
            }
            50% { 
                filter: drop-shadow(0 0 50px rgba(139,92,246,1)) drop-shadow(0 0 80px rgba(236,72,153,0.6));
                transform: scale(1.02);
            }
        }

        p, span, div, label, .stMarkdown { color: #ffffff !important; }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f0820 0%, #1a0b2e 100%) !important;
            border-right: 2px solid rgba(139, 92, 246, 0.4) !important;
        }
        [data-testid="stSidebar"] h3 {
            color: #ffffff !important;
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            margin-top: 1rem !important;
            text-shadow: 0 0 20px rgba(139, 92, 246, 0.8);
        }

        /* Text input — match date input style */
        .stTextInput input {
            background: rgba(30, 20, 60, 0.92) !important;
            border: 2px solid rgba(139, 92, 246, 0.6) !important;
            border-radius: 12px !important;
            color: #ffffff !important;
            padding: 1rem !important;
            font-size: 1rem !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            box-shadow: inset 0 0 20px rgba(139, 92, 246, 0.12);
        }
        .stTextInput input:focus {
            background: rgba(40, 30, 80, 0.95) !important;
            border-color: rgba(139, 92, 246, 1) !important;
            box-shadow:
                0 0 30px rgba(139, 92, 246, 0.6),
                inset 0 0 30px rgba(139, 92, 246, 0.2) !important;
            transform: translateY(-2px);
        }
        .stTextInput input::placeholder {
            color: rgba(255,255,255,0.55) !important;
        }
        .stTextInput label {
            color: #e0e0e0 !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem !important;
        }

        /* Text area — match date input style */
        .stTextArea textarea {
            background: rgba(30,20,60,0.92) !important;
            color: #ffffff !important;
            border: 2px solid rgba(139,92,246,0.6) !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            font-weight: 600 !important;
            box-shadow: inset 0 0 20px rgba(139,92,246,0.12) !important;
        }
        .stTextArea textarea:focus {
            background: rgba(40,30,80,0.95) !important;
            border-color: rgba(139,92,246,1) !important;
            box-shadow: 0 0 30px rgba(139,92,246,0.6), inset 0 0 30px rgba(139,92,246,0.2) !important;
            transform: translateY(-2px);
        }
        .stTextArea textarea::placeholder {
            color: rgba(255,255,255,0.55) !important;
        }

        /* Buttons — START PLANNING style */
        .stButton button {
            background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #8b5cf6 100%) !important;
            background-size: 200% 200% !important;
            color: white !important;
            border: 2px solid rgba(139, 92, 246, 0.6) !important;
            border-radius: 12px !important;
            padding: 1rem 2.5rem !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            box-shadow:
                0 0 40px rgba(139, 92, 246, 0.5),
                inset 0 0 20px rgba(255, 255, 255, 0.1) !important;
            transition: all 0.4s ease !important;
            cursor: pointer !important;
            position: relative !important;
            overflow: hidden !important;
        }
        .stButton button:hover {
            background-position: 100% 0 !important;
            transform: translateY(-4px) scale(1.05) !important;
            box-shadow:
                0 0 60px rgba(139, 92, 246, 0.8),
                0 0 100px rgba(236, 72, 153, 0.4),
                inset 0 0 30px rgba(255, 255, 255, 0.2) !important;
            border-color: rgba(236, 72, 153, 0.8) !important;
        }

        /* LinkedIn button — cyan/blue gradient style */
        .linkedin-btn {
            background: linear-gradient(135deg, #0077b5 0%, #00a0dc 50%, #0077b5 100%) !important;
            background-size: 200% 200% !important;
            color: white !important;
            border: 2px solid rgba(0, 119, 181, 0.6) !important;
            border-radius: 12px !important;
            padding: 0.5rem 2.5rem !important;
            font-weight: 500 !important;
            font-size: 0.80 rem !important;
            text-transform: uppercase !important;
            letter-spacing: 1.8px !important;
            text-align: center !important;
            display: block !important;
            text-decoration: none !important;
            box-shadow:
                0 0 40px rgba(0, 119, 181, 0.5),
                inset 0 0 20px rgba(255, 255, 255, 0.1) !important;
            transition: all 0.4s ease !important;
            cursor: pointer !important;
            margin-top: 1.5rem !important;
        }
        .linkedin-btn:hover {
            background-position: 100% 0 !important;
            transform: translateY(-4px) scale(1.05) !important;
            box-shadow:
                0 0 60px rgba(0, 160, 220, 0.8),
                0 0 100px rgba(0, 119, 181, 0.4),
                inset 0 0 30px rgba(255, 255, 255, 0.2) !important;
            border-color: rgba(0, 160, 220, 0.8) !important;
            color: white !important;
        }

        /* Themed markdown container */
        .neon-markdown {
            width: 100%;
            max-width: 1100px;
            margin: 0 auto 2rem auto;
            background: rgba(10,1,24,0.5);
            border: 2px solid rgba(139,92,246,0.4);
            border-radius: 16px;
            padding: 1.25rem 1.5rem;
            box-shadow: 0 0 60px rgba(139,92,246,0.25), inset 0 0 60px rgba(139,92,246,0.06);
        }
        .neon-markdown h2, .neon-markdown h3, .neon-markdown p, .neon-markdown li {
            color: #fff !important;
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 12px; }
        ::-webkit-scrollbar-track { background: rgba(10, 1, 24, 0.8); }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #8b5cf6 0%, #ec4899 100%);
            border-radius: 6px;
            box-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
        }
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, #a78bfa 0%, #f472b6 100%);
            box-shadow: 0 0 20px rgba(139, 92, 246, 0.8);
        }
        </style>
        """, unsafe_allow_html=True)

        # DATE INPUT — complete override (field shell + inner wrapper + text + popup)
        st.markdown("""
        <style>
        /* 1) Outer shell (wrapper around entire widget) */
        [data-testid="stDateInput"] > div {
          background: rgba(30, 20, 60, 0.92) !important;
          border: 2px solid rgba(139, 92, 246, 0.6) !important;
          border-radius: 12px !important;
          padding: 0.25rem 0.6rem !important;
          box-shadow: inset 0 0 20px rgba(139,92,246,0.12) !important;
          transition: border-color .2s ease, box-shadow .2s ease, transform .15s ease !important;
        }

        /* 2) Inner base-input wrapper (this is the white box you see in devtools) */
        [data-testid="stDateInput"] div[data-baseweb="base-input"],
        [data-testid="stDateInput"] .st-bb,
        [data-testid="stDateInput"] .st-bd {
          background: transparent !important;
          border: none !important;
        }

        /* 3) Text input element inside */
        [data-testid="stDateInput"] input[type="text"] {
          background: transparent !important;
          color: #ffffff !important;
          caret-color: #ffffff !important;
          border: none !important;
          font-weight: 600 !important;
        }

        /* 4) Placeholder */
        [data-testid="stDateInput"] input::placeholder,
        [data-testid="stDateInput"] input::-webkit-input-placeholder {
          color: rgba(255,255,255,0.55) !important;
          opacity: 1 !important;
        }

        /* 5) Focus ring (on the outer shell) */
        [data-testid="stDateInput"]:focus-within > div {
          border-color: rgba(139, 92, 246, 0.6) !important;
          box-shadow: 0 0 30px rgba(139, 92, 246, 0.6), inset 0 0 30px rgba(139, 92, 246, 0.2) !important;
          transform: translateY(-2px);
        }

        /* 6) Icons (calendar + clear chip) */
        [data-testid="stDateInput"] svg { color: #c4b5fd !important; }
        [data-testid="stDateInputClearBtn"] { color: #c4b5fd !important; opacity: 0.95 !important; }
        [data-testid="stDateInputClearBtn"]:hover {
          color: #f0e9ff !important;
          filter: drop-shadow(0 0 6px rgba(139,92,246,.9));
        }
        </style>
        """, unsafe_allow_html=True)

        # CALENDAR POPUP — High contrast, crystal clear, professional design
        st.markdown("""
        <style>
        /* 1) Popover shell — solid dark purple with strong border */
        div[data-baseweb="popover"][role="application"] {
          background: #0f0820 !important;
          border: 3px solid #8b5cf6 !important;
          border-radius: 18px !important;
          box-shadow: 0 10px 60px rgba(139,92,246,0.7), 0 0 0 1px rgba(139,92,246,0.3) !important;
          padding: 0 !important;
          overflow: hidden !important;
        }

        /* 2) Calendar wrapper — ensure no interference */
        div[data-baseweb="calendar"] {
          background: transparent !important;
          padding: 1.25rem !important;
        }

        /* 3) Month header bar — bold and clear */
        div[data-baseweb="calendar"] > div:first-child {
          background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%) !important;
          padding: 1rem 1.25rem !important;
          margin: -1.25rem -1.25rem 1rem -1.25rem !important;
          border-bottom: 2px solid #a78bfa !important;
          display: flex !important;
          align-items: center !important;
          justify-content: space-between !important;
        }

        /* Navigation arrows — clear white buttons */
        div[data-baseweb="calendar"] button {
          color: #ffffff !important;
          background: rgba(255,255,255,0.15) !important;
          border: 2px solid rgba(255,255,255,0.3) !important;
          border-radius: 8px !important;
          padding: 0.4rem 0.6rem !important;
          font-weight: 700 !important;
          transition: all 0.2s ease !important;
          cursor: pointer !important;
        }
        div[data-baseweb="calendar"] button:hover {
          background: rgba(255,255,255,0.3) !important;
          border-color: rgba(255,255,255,0.6) !important;
          transform: scale(1.15) !important;
          box-shadow: 0 0 16px rgba(255,255,255,0.4) !important;
        }

        /* Month/year text — large and bold */
        div[data-baseweb="calendar"] > div:first-child > div {
          color: #ffffff !important;
          font-weight: 800 !important;
          font-size: 1.2rem !important;
          letter-spacing: 0.5px !important;
        }

        /* 4) Weekday labels — uppercase, bold, high contrast */
        div[role="presentation"]:not([aria-hidden="true"]) {
          color: #e9d5ff !important;
          font-weight: 800 !important;
          font-size: 0.85rem !important;
          text-transform: uppercase !important;
          letter-spacing: 1.5px !important;
          padding: 0.6rem 0 !important;
          text-align: center !important;
        }

        /* 5) Day cells — clean white text on dark cells */
        div[role="grid"] div[role="presentation"] {
          margin: 3px !important;
        }

        div[role="grid"] button,
        div[role="grid"] div[role="button"] {
          color: #ffffff !important;
          background: rgba(139,92,246,0.15) !important;
          border: 1px solid rgba(139,92,246,0.3) !important;
          border-radius: 10px !important;
          padding: 0.65rem !important;
          font-weight: 700 !important;
          font-size: 1rem !important;
          transition: all 0.15s ease !important;
          cursor: pointer !important;
          min-width: 40px !important;
          min-height: 40px !important;
          display: flex !important;
          align-items: center !important;
          justify-content: center !important;
        }

        /* Disabled/outside month — dim but still readable */
        div[role="grid"] button[aria-disabled="true"],
        div[role="grid"] div[aria-disabled="true"] {
          color: #6b5a7e !important;
          background: rgba(50,30,80,0.2) !important;
          border-color: rgba(107,90,126,0.2) !important;
          opacity: 0.4 !important;
          cursor: not-allowed !important;
        }

        /* 6) Hover — bright purple highlight */
        div[role="grid"] button:not([aria-disabled="true"]):hover,
        div[role="grid"] div[role="button"]:not([aria-disabled="true"]):hover {
          background: rgba(139,92,246,0.4) !important;
          border-color: #a78bfa !important;
          transform: scale(1.1) !important;
          box-shadow: 0 0 20px rgba(139,92,246,0.6) !important;
          color: #ffffff !important;
        }

        /* 7) Selected date — vibrant gradient, unmissable */
        div[role="grid"] button[aria-pressed="true"],
        div[role="grid"] div[aria-selected="true"],
        div[role="grid"] button[aria-selected="true"] {
          background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%) !important;
          border: 2px solid #f472b6 !important;
          color: #ffffff !important;
          font-weight: 900 !important;
          box-shadow: 0 0 24px rgba(236,72,153,0.8), inset 0 2px 8px rgba(255,255,255,0.2) !important;
          transform: scale(1.12) !important;
        }

        /* 8) Today indicator — bright cyan ring */
        div[role="grid"] button[aria-current="date"]:not([aria-selected="true"]),
        div[role="grid"] div[aria-current="date"]:not([aria-selected="true"]) {
          outline: 3px solid #22d3ee !important;
          outline-offset: -3px !important;
          box-shadow: 0 0 16px rgba(34,211,238,0.6) !important;
        }

        /* 9) Range selection (if using date range) */
        div[role="grid"] button[class*="inRange"],
        div[role="grid"] div[class*="inRange"] {
          background: rgba(139,92,246,0.3) !important;
          border-color: rgba(167,139,250,0.6) !important;
          color: #ffffff !important;
        }

        div[role="grid"] button[class*="rangeStart"],
        div[role="grid"] button[class*="rangeEnd"] {
          background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%) !important;
          border: 2px solid #f472b6 !important;
          box-shadow: 0 0 24px rgba(236,72,153,0.8) !important;
        }

        /* Clear any remaining white backgrounds */
        div[data-baseweb="popover"] * {
          background-color: transparent !important;
        }
        div[data-baseweb="popover"] {
          background: #0f0820 !important;
        }
        div[data-baseweb="calendar"] {
          background: transparent !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # Hero
        st.title("🏖️ Trip Agent")
        st.markdown("""
            <div style="text-align: center; margin-top: 1rem; margin-bottom: 3rem;">  
                <p style="font-size: 1.8rem; font-weight: 700; color: #ffffff; margin-bottom: 1rem;">
                    Unleash the Power of AI Travel Planning
                </p>
                <p style="font-size: 1.2rem; color: #b8b8b8;">
                    Your personal assistant for planning extraordinary adventures 🌍✈️
                </p>
            </div>
        """, unsafe_allow_html=True)

        # CTA
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🚀 START PLANNING"):
                self.user_controls["start_planning"] = True 
                st.snow()
            else:
                self.user_controls["start_planning"] = False

        st.markdown("<br>", unsafe_allow_html=True)

        # Expander
        with st.expander("🎯 How to Get Started", expanded=False):
            st.markdown("""
                - Configure API Keys in the sidebar
                - Describe your dream destination
                - Let the agent plan everything
                - Enjoy your trip
            """)

        # Sidebar
        with st.sidebar:
            st.markdown("### 🔐 API Configuration")
            st.markdown('<p style="font-size: 0.95rem; margin-bottom: 1.0rem;">Enter your API keys to get started</p>', unsafe_allow_html=True)

            gemini_api_key = st.text_input("Gemini API Key", type="password", placeholder="sk-••••••••••••••••")
            serper_api_key = st.text_input("Serper API Key", type="password", placeholder="••••••••••••••••")
            browserless_api_key = st.text_input("Browserless API Key", type="password", placeholder="••••••••••••••••")

            st.markdown("---")
            if gemini_api_key and serper_api_key and browserless_api_key:
                st.success("✅ All systems operational")
            else:
                missing = []
                if not gemini_api_key: missing.append("Gemini")
                if not serper_api_key: missing.append("Serper")
                if not browserless_api_key: missing.append("Browserless")
                st.warning(f"⚠️ Required: {', '.join(missing)}")

            st.markdown("---")
            st.markdown("### 👨‍💻 About")
            st.markdown("**Developed by Shankar** 🚀")
            st.markdown("AI Engineer")

            # LinkedIn button with matching style
            st.markdown("""
                <a href="https://www.linkedin.com/in/sivashankar-subramaniam-661092228/" 
                   target="_blank" 
                   class="linkedin-btn">
                    🔗 Connect on LinkedIn
                </a>
            """, unsafe_allow_html=True)

        # Store controls
        self.user_controls["gemini_api_key"] = gemini_api_key
        self.user_controls["serper_api_key"] = serper_api_key
        self.user_controls["browserless_api_key"] = browserless_api_key

        return self.user_controls
