import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO
import plotly.express as px

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
💉 **Welcome to the digital lab!** This tool helps you interpret your Complete Blood Picture (CBP) report with clear medical insights, colorful charts, and downloadable summaries.
""")

file = st.file_uploader("📤 Upload Blood Report (CSV or Excel)", type=["csv", "xlsx"])

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

interpretation_notes = {
    "Hemoglobin": "Low: Anemia, High: Polycythemia",
    "RBC": "Low: Anemia, High: Dehydration or Polycythemia",
    "WBC": "Low: Leukopenia, High: Infection or Leukemia",
    "Platelets": "Low: Thrombocytopenia, High: Risk of clotting",
    "PCV": "Low: Anemia, High: Dehydration",
    "MCV": "Low: Microcytic anemia, High: Macrocytic anemia",
    "MCH": "Low: Hypochromic anemia, High: Macrocytosis",
    "MCHC": "Low: Iron deficiency anemia, High: Spherocytosis",
    "RDW CV": "High: Mixed anemia or B12/iron deficiency",
    "RDW SD": "High RDW SD may indicate anisocytosis (RBC size variation)",
    "PDW": "High PDW suggests platelet anisocytosis",
    "MPV": "High MPV indicates larger platelets, common in thrombocytopenia recovery",
    "Neutrophils": "High: Bacterial infection, Low: Bone marrow suppression",
    "Lymphocytes": "High: Viral infections, Low: Immunodeficiency",
    "Eosinophils": "High: Allergies or parasitic infections",
    "Monocytes": "High: Chronic inflammation or infection",
    "Basophils": "High: Allergic response or chronic myeloid leukemia"
}

def analyze_value(val, norm_range):
    if val < norm_range[0]:
        return "🔻 Low"
    elif val > norm_range[1]:
        return "🔺 High"
    else:
        return "✅ Normal"

if file:
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    df.columns = [c.strip() for c in df.columns]
    st.subheader("📋 Uploaded Blood Report")
    st.dataframe(df.head(), use_container_width=True)

    result = []
    for param, (low, high) in normal_ranges.items():
        if param in df.columns:
            value = df[param].iloc[0]
            status = analyze_value(value, (low, high))
            comment = interpretation_notes.get(param, "")
            result.append({"Parameter": param, "Value": value, "Status": status, "Interpretation": comment})

    result_df = pd.DataFrame(result)
    st.subheader("🩸 Interpretation of Blood Report")
    st.dataframe(result_df, use_container_width=True)

    fig = px.bar(result_df, x="Parameter", y="Value", color="Status",
                 color_discrete_map={"✅ Normal": "green", "🔻 Low": "red", "🔺 High": "orange"},
                 title="🔬 Blood Parameter Levels", height=500)
    st.plotly_chart(fig, use_container_width=True)

    def create_pdf(results):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Complete Blood Picture Report Summary", ln=1, align='C')
        pdf.ln(5)
        pdf.set_font("Arial", '', 12)
        for item in results:
            pdf.cell(0, 10, f"{item['Parameter']}: {item['Value']} - {item['Status']} - {item['Interpretation']}", ln=1)
        return pdf.output(dest='S').encode('latin1')

    st.download_button("📄 Download Report (PDF)", data=create_pdf(result), file_name="cbp_report_summary.pdf")

    st.markdown("""
    <hr style="border:1px solid #ccc;"/>
    <p style="text-align:center; font-size:14px;">
    🧑‍⚕️ Created by <strong>Sai Preethi Ananya Naidu</strong> | 📧 <a href="mailto:preethiananyanaidu@gmail.com">preethiananyanaidu@gmail.com</a>
    </p>
    """, unsafe_allow_html=True)

else:
    st.info("Please upload your Complete Blood Picture (CBP) file to begin analysis.")
