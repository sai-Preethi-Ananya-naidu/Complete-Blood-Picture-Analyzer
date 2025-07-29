import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO
import plotly.express as px
from PIL import Image
import tempfile

st.set_page_config(page_title="Complete Blood Picture Analyzer", layout="wide")

st.markdown("""
<style>
    .main {background-color: #f2f7f5;}
    h1 {color: #006d77; text-align: center; font-size: 36px; font-family: 'Trebuchet MS';}
    .stButton>button, .stDownloadButton>button {
        background-color: #006d77;
        color: white;
        font-size: 16px;
        padding: 8px 20px;
        border-radius: 10px;
    }
    .block-container {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🧪 Complete Blood Picture Analyzer</h1>", unsafe_allow_html=True)

st.markdown("""
💉 **Welcome to the digital lab!** This tool helps you interpret your Complete Blood Picture (CBP) report with clear medical insights, colorful charts, dietary suggestions, and downloadable summaries.
""")

file = st.file_uploader("📤 Upload Blood Report (CSV, Excel, PDF, or Image)", type=["csv", "xlsx", "pdf", "png", "jpg", "jpeg"])

normal_ranges = {
    "Hemoglobin": (11.0, 15.0),
    "RBC": (3.8, 4.8),
    "WBC": (4000, 11000),
    "Platelets": (150000, 450000),
    "PCV": (36, 46),
    "MCV": (80, 100),
    "MCH": (27, 33),
    "MCHC": (32, 36),
    "RDW CV": (11.5, 14.5),
    "RDW SD": (29, 46),
    "PDW": (9, 17),
    "MPV": (7, 11),
    "Neutrophils": (45, 75),
    "Lymphocytes": (20, 40),
    "Eosinophils": (1, 6),
    "Monocytes": (2, 10),
    "Basophils": (0, 2)
}

diet_suggestions = {
    "Hemoglobin": "Include iron-rich foods like spinach, red meat, lentils, and fortified cereals.",
    "RBC": "Eat iron and vitamin B12-rich foods like eggs, dairy, poultry, and beans.",
    "WBC": "Boost immunity with citrus fruits, garlic, and probiotic-rich foods.",
    "Platelets": "Consume papaya leaf extract, pomegranate, and vitamin C-rich foods.",
    "PCV": "Stay hydrated if high; if low, increase iron-rich food intake.",
    "MCV": "If low, add iron; if high, focus on folate and B12 (leafy greens, liver, eggs).",
    "MCH": "Add lean meat, legumes, and green vegetables.",
    "MCHC": "Consume eggs, fish, and green leafy vegetables.",
    "RDW CV": "Balance iron and vitamin B12 intake.",
    "RDW SD": "Include whole grains, meat, and vegetables.",
    "PDW": "Ensure a healthy diet with antioxidants and omega-3s.",
    "MPV": "Balance vitamin B12 and folate levels.",
    "Neutrophils": "Consume zinc-rich foods like seeds and shellfish.",
    "Lymphocytes": "Eat berries, turmeric, and green tea.",
    "Eosinophils": "Reduce allergens; eat anti-inflammatory foods like ginger and turmeric.",
    "Monocytes": "Add garlic, mushrooms, and leafy greens.",
    "Basophils": "Avoid allergens and processed foods."
}

def analyze_value(val, norm_range):
    if val < norm_range[0]:
        return "Low"
    elif val > norm_range[1]:
        return "High"
    else:
        return "Normal"

def consult_doctor_advice(status):
    if status == "Low":
        return "Consider consulting a physician for possible deficiency."
    elif status == "High":
        return "Elevated levels detected. Medical consultation is advised."
    return "Within normal range."

def create_pdf(diet_advice):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "CBP Report Summary: Diet & Medical Advice", ln=1, align='C')
    pdf.ln(5)
    pdf.set_font("Arial", '', 12)
    for item in diet_advice:
        pdf.cell(0, 10, f"{item['Parameter']}", ln=1)
        pdf.multi_cell(0, 10, f"Diet Suggestion: {item['Diet Suggestion']}")
        pdf.multi_cell(0, 10, f"Doctor Advice: {item['Doctor Advice']}")
        pdf.ln(2)
    return pdf.output(dest='S').encode('latin1')

if file:
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    elif file.name.endswith("xlsx"):
        df = pd.read_excel(file)
    elif file.name.endswith("pdf"):
        st.warning("🔒 PDF parsing is currently not supported. Please upload a CSV, Excel, or Image file.")
        st.stop()
    elif file.name.lower().endswith((".png", ".jpg", ".jpeg")):
        st.image(file, caption="Uploaded Image", use_column_width=True)
        st.info("📷 OCR for image extraction coming soon! Please upload a CSV or Excel for now.")
        st.stop()
    else:
        st.error("Unsupported file type.")
        st.stop()

    df.columns = [c.strip() for c in df.columns]
    st.subheader("📋 Uploaded Blood Report")
    st.dataframe(df.head(), use_container_width=True)

    for index, row in df.iterrows():
        st.markdown(f"### 🧾 Report for Row {index+1}")
        result = []
        diet_advice = []
        for param, (low, high) in normal_ranges.items():
            if param in row:
                value = row[param]
                status = analyze_value(value, (low, high))
                if status != "Normal":
                    diet = diet_suggestions.get(param, "")
                    advice = consult_doctor_advice(status)
                    diet_advice.append({"Parameter": param, "Diet Suggestion": diet, "Doctor Advice": advice})
                result.append({"Parameter": param, "Value": value, "Status": status})

        result_df = pd.DataFrame(result)
        st.dataframe(result_df, use_container_width=True)

        if diet_advice:
            st.markdown("#### 🍽️ Diet & Medical Advice (Only for Abnormal Values)")
            advice_df = pd.DataFrame(diet_advice)
            st.dataframe(advice_df, use_container_width=True)
            st.download_button(f"📄 Download Advice PDF (Row {index+1})", data=create_pdf(diet_advice), file_name=f"cbp_advice_row_{index+1}.pdf")

        fig = px.bar(result_df, x="Parameter", y="Value", color="Status",
                     color_discrete_map={"Normal": "green", "Low": "red", "High": "orange"},
                     title=f"🧬 Blood Levels for Row {index+1}", height=500)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <hr style="border:1px solid #ccc;"/>
    <p style="text-align:center; font-size:14px;">
    🧑‍⚕️ Created by <strong>Sai Preethi Ananya Naidu</strong> | 📧 <a href="mailto:preethiananyanaidu@gmail.com">preethiananyanaidu@gmail.com</a>
    </p>
    """, unsafe_allow_html=True)

else:
    st.info("Please upload your Complete Blood Picture (CBP) file to begin analysis.")
