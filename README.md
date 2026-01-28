# Receipt_Invoice_Digitizer-MILESTONE-2-
A Streamlit-based Receipt and Invoice Digitizer that processes receipt images using OCR, extracts structured data with NLP and Regex techniques, performs amount validation &amp; duplicate detection, and visualizes insights through an interactive analytics dashboard. 

# 📄 Receipt and Invoice Digitizer – Milestone 2

##  Project Overview
The Receipt and Invoice Digitizer is a document processing system designed to extract, validate, store, and analyze information from receipts and invoices.  
This **Milestone-2 implementation** focuses on rule-based and template-driven extraction to ensure high accuracy and consistency, suitable for academic evaluation and system design demonstration.

---

##  Objectives of Milestone 2
- Digitize receipt and invoice images
- Extract structured information such as vendor name, date, time, payment method, line items, and total amount
- Validate extracted financial data using predefined business rules
- Detect duplicate receipts
- Store extracted data in a structured database
- Provide visual analytics through an interactive dashboard

---

## 🧠 Techniques Used
- **OCR (Optical Character Recognition)** using Tesseract
- **Image Preprocessing** with OpenCV (grayscale, blur, thresholding)
- **NLP & Regex-based Extraction** for structured fields
- **Rule-based Validation** (Subtotal + Tax = Total)
- **Template-based Receipt Mapping** for deterministic results
- **SQLite Database** for storage and history tracking
- **Data Visualization** using Matplotlib

---

##  System Architecture (High-Level)
1. Receipt/Image Upload  
2. Image Preprocessing  
3. OCR Text Extraction  
4. Data Extraction (NLP + Regex)  
5. Data Validation (Amount & Format Checks)  
6. Duplicate Detection  
7. Structured Database Storage  
8. Dashboard & Analytics Visualization  

---

##  Key Features
- Displays **original and processed receipt images**
- Extracts **line items and amounts**
- Performs **amount validation (Subtotal + Tax = Total)**
- Flags duplicate receipts
- Maintains **active and deleted bill history**
- Provides **bar charts, line charts, and pie charts** for analytics.
