# 🧪 Complete Blood Picture Analyzer

This Streamlit app helps users analyze their CBC (Complete Blood Count) reports easily by:
- Uploading blood reports (CSV, Excel, PDF, or images)
- Automatically interpreting values
- Highlighting low/high/normal ranges
- Displaying medical explanations and interactive graphs
- Downloading a PDF summary of the results

---

## ✅ Features
- 📥 Upload report (CSV, XLSX, Image, or PDF*)
- 📊 Visualizations: Bar chart colored by health status
- 📄 PDF Summary: Downloadable report
- 🩺 Medical insights and range-based flags

> ⚠️ Note: PDF and image upload only previews the file (OCR integration coming soon).

---

## 🔬 Parameters Interpreted
- Hemoglobin, RBC, WBC, Platelets, PCV, MCV, MCH, MCHC  
- RDW CV, RDW SD, PDW, MPV  
- Neutrophils, Lymphocytes, Eosinophils, Monocytes, Basophils

---

## 💻 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run cbp_analyzer.py
