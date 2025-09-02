# 🛒 BigQuery E-Commerce Analytics Pipeline  

## 📌 Overview  
This project demonstrates an **end-to-end data analytics pipeline** for e-commerce sales using **Python, Google BigQuery, and Looker Studio**.  
 
**Key Capabilities:**  
- Data generation with Python  
- Data storage & querying with BigQuery  
- Insights & dashboards with Looker Studio / Matplotlib  

---

## 🚀 Business Impact  
This project answers critical e-commerce questions such as:  
- 💰 *How much revenue is generated month over month (YoY trends)?*  
- 🛍️ *Which product categories drive the most sales?*  
- 👤 *What is the share of new vs. returning customers?*  
- 📈 *What is the average order value and how is it changing?*  

---

## 🛠 Tech Stack  
- **Python** → `pandas`, `faker`, `matplotlib`  
- **Google Cloud Platform (GCP)** → BigQuery for storage & SQL queries  
- **Looker Studio** → Dashboards & KPI reporting  
- **SQL** → Aggregations, calculated fields, business logic  

---

## 📊 Dashboard Preview  
- [📄 Dashboard PDF](./docs/dashboard.pdf)  
- 🖼 [Screenshots](./docs/screenshots/)  

Example Insights:  
- Revenue trends over time  
- Top customer segments  
- Interactive filters (date range, categories)  

---

## ⚡ Setup & Run  

```bash
# 1️⃣ Install dependencies
pip install -r requirements.txt

# 2️⃣ Generate synthetic dataset
python ecommerce-performance-dashboard/data/generate_dataset.py

# 3️⃣ Upload to BigQuery
python scripts/load_to_bigquery.py

# 4️⃣ Run queries
python scripts/query_bigquery.py

# 5️⃣ Visualize results (Matplotlib chart)
python scripts/visualize_results.py

---

## 🔮 Future Improvements
- Add **forecasting models** 
- Integrate **customer churn prediction**.
- Add **region-wise revenue maps**.
- Automate dataset updates via GCP pipelines.

---

## 👤 Author
-**Saini Patro**  
- GitHub: [Sa1385](https://github.com/Sa1385)  

- LinkedIn: [Saini Patro](https://www.linkedin.com/in/saini-patro/) 
