

🧪 Complete Blood Picture Analyzer

A Streamlit-based web app that analyzes Complete Blood Picture (CBP) reports, interprets each parameter, and provides personalized diet and doctor consultation suggestions.


🔗 Live App:

[https://complete-blood-picture-analyzer-jij7kfjshcbx98ldc9dkqx.streamlit.app/](https://complete-blood-picture-analyzer-jij7kfjshcbx98ldc9dkqx.streamlit.app/)

💡 Project Overview

This app aims to assist patients and healthcare professionals by offering:

* ✅ Medical interpretation of CBP reports
* ✅ Dietary recommendations for abnormal values
* ✅ Doctor consultation alerts for concerning deviations
* ✅ Graphical summaries for each row/patient
* ✅ PDF downloads for diet and medical suggestions

📁 Features

* Accepts **CSV** or **Excel** files containing one or more patient reports.
* Detects and highlights **High**, **Low**, and **Normal** values.
* Provides **dietary advice and medical suggestions** only for abnormal values.
* Visualizes blood parameters using interactive **Plotly bar charts**.
* Allows downloading **PDF summaries** for each report.

📊 Sample Data Format

```csv
Hemoglobin,RBC,WBC,Platelets,PCV,MCV,MCH,MCHC,RDW CV,RDW SD,PDW,MPV,Neutrophils,Lymphocytes,Eosinophils,Monocytes,Basophils
11.2,4.1,5000,160000,37,82,28,33,12.5,30,10,8.2,50,30,2,3,0
13.5,4.5,8700,230000,40,95,31,35,14.0,45,13,9.5,65,35,4,8,1
...
```

Each row = one patient report.

🧑‍⚕️ How to Use

1. Click the app link above.
2. Upload your CBP report in `.csv` or `.xlsx` format.
3. The app displays a visual and tabular summary.
4. For abnormal parameters, view:

   * Diet advice 🍽️
   * Doctor consultation guidance 🩺
5. Download a clean PDF summary for each patient.

 ⚙️ Technologies Used

* **Python**
* **Streamlit**
* **Pandas**
* **Plotly**
* **FPDF**

👩‍💻 Developed By

**Sai Preethi Ananya Naidu**
📧(mailto:preethiananyanaidu@gmail.com)

---
