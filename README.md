# 📊 Google Analytics A/B Testing & Dashboard  

This repository contains an **A/B testing analysis** for **Google Analytics data**, comparing conversion performance between **mobile and desktop users**. Data was extracted from **Google BigQuery**, processed and analyzed using Python, and visualized in **Tableau Public**.  

## 📂 **Project Files**  

- `google_analytics_big_query.sql` → SQL query used in **BigQuery** to extract data.  
- `google_analytics_data.csv` → CSV file with the exported data from BigQuery.  
- `google_analytics_test_T.py` → Python script performing the **A/B test** (T-Test) comparing conversion rates.  
- **Tableau Dashboard** → [Initial Tableau Public Visualization](https://public.tableau.com/views/google_analytics_analysis/Planilha1?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).  

## 📊 **Overview**  

1️⃣ **Data Extraction:** Collected Google Analytics data for January 2017 using BigQuery.  
2️⃣ **Statistical Analysis:** Applied a **T-Test** to compare conversion revenue between device categories.  
3️⃣ **Visualization:** Published an initial **Tableau Public** dashboard with the CSV data.  

## 🚀 **Next Steps**  

✅ Improve the **Tableau dashboard** by adding more KPIs and insights.  
✅ Explore additional **metrics**, such as **conversion rate and ARPU**.  
✅ Establish a direct connection between **BigQuery and Tableau Public**.  

🔹 **Feedback and contributions are welcome!** 🚀  
