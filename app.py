import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader

# Load environment variables from the secure .env file
load_dotenv()

# Initialize the Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("Missing GROQ_API_KEY in your .env file!")
    st.stop()

client = Groq(api_key=api_key)

# 1. Page Configuration for a modern, wide UX
st.set_page_config(
    page_title="Enterprise Compliance Agent",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom injection for a clean, professional dark mode UI
# Custom injection for a modern, Apple/Microsoft inspired dark mode UI
st.markdown("""
    <style>
        /* Global Background and Font */
        .stApp {
            background-color: #000000;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        
        /* Headers */
        h1, h2, h3 { 
            color: #f5f5f7 !important; 
            font-weight: 600; 
            letter-spacing: -0.5px;
        }
        
        /* The Upload and Select Boxes */
        .stFileUploader, .stSelectbox {
            background-color: #1c1c1e;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #333336;
        }

        /* Modern Pill-Shaped Button */
        .stButton>button { 
            background: linear-gradient(135deg, #007aff, #005bb5);
            color: white; 
            border: none; 
            width: 100%; 
            border-radius: 24px; 
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 122, 255, 0.3);
        }
        .stButton>button:hover { 
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0, 122, 255, 0.5);
            color: white; 
        }

        /* The Output Report Box (Glassmorphism effect) */
        .report-box { 
            background-color: rgba(28, 28, 30, 0.8); 
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1); 
            border-radius: 16px; 
            padding: 25px; 
            margin-top: 20px; 
            color: #d2d2d7;
            font-size: 15px;
            line-height: 1.6;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
    </style>
""", unsafe_allow_html=True)

# 2. Main Dashboard Header
st.title("🛡️ Enterprise GenAI Compliance Agent")
st.subheader("Automated Ingestion & Legal Risk Extraction for UK Regulations")
st.markdown("---")

# Split layout: Upload on the left, Insights on the right
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📥 Document Ingestion")
    uploaded_file = st.file_uploader("Drag and drop your UK regulatory PDF here", type=["pdf"])
    
    st.markdown("### 🎯 Analysis Target")
    analysis_type = st.selectbox(
        "Select compliance filter:",
        ["High-Risk Liabilities", "Operational Obligations", "Executive Summary", "Breach Penalties"]
    )

with col2:
    st.markdown("### 📋 Audit Insights")
    
    if uploaded_file is not None:
        with st.spinner("Surgically extracting text from document..."):
            try:
                # Ingestion Engine: Read and stitch PDF text together
                reader = PdfReader(uploaded_file)
                pdf_text = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        pdf_text += text + "\n"
                
                # Truncate text context safely if it's massive
                context_window = pdf_text[:25000] 
                
            except Exception as e:
                st.error(f"Error parsing PDF file: {str(e)}")
                st.stop()
        
        st.success(f"Successfully processed {len(reader.pages)} pages.")
        
        # Crafting the compliance query payload
        system_prompt = (
            "You are an elite enterprise compliance auditor specializing in UK commercial regulations. "
            "Your task is to analyze the provided legal text context and extract clean, factual insights based strictly "
            "on the user's requested filter. Do not speculate or hallucinate. Use professional, clear, human language."
        )
        
        user_prompt = f"Analyze this regulatory text and extract the following: {analysis_type}.\n\nContext:\n{context_window}"
        
        # Trigger the analysis when button is pressed
        if st.button("Run Compliance Audit"):
            with st.spinner("Streaming context to Groq Cloud Platform..."):
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        model="llama-3.1-8b-instant",
                        temperature=0.1,  # Low temp avoids creative AI hallucinations
                    )
                    
                    # Display the audit output inside a styled container
                    st.markdown('<div class="report-box">', unsafe_allow_html=True)
                    st.markdown(chat_completion.choices[0].message.content)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Groq API Error: {str(e)}")
    else:
        st.info("Awaiting document upload to begin auditing process.")