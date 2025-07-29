# 🧪 Complete Blood Picture (CBP) Analyzer

This Streamlit app analyzes uploaded blood reports (CSV/XLSX) for 17+ key CBC parameters and provides:
- Color-coded interpretation (Low / Normal / High)
- Medical insights for each result
- Interactive bar chart for visual analysis
- Downloadable PDF summary

## ✅ Features
- Upload any CBP report in `.csv` or `.xlsx` format
- Checks against medical reference ranges
- Highlights abnormal values with clinical comments
- Graphical bar chart of blood parameters
- PDF summary download

## 🧬 Parameters Analyzed
Hemoglobin, RBC, WBC, Platelets, PCV, MCV, MCH, MCHC, RDW-CV, RDW-SD, PDW, MPV, Neutrophils, Lymphocytes, Eosinophils, Monocytes, Basophils

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run cbp_analyzer.py
