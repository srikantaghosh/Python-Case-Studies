# Python-Case-Studies

## ETL-Demo-1 — Python Data Engineering Prototyp
This project is a hands-on prototype for learning data engineering with Python. It covers building modular, testable ETL components step-by-step, using a synthetic dataset.

##  What’s Covered 
1. Sample Dataset Creation
	•	Used Faker and random libraries to generate a CSV with 50 rows.
	•	Columns: id, name, email, signup_date, country, age, purchase_amount.
	•	Saved as sample_customers.csv.

2. Ingestion Function
	•	Created a reusable function load_data(file_path) to load the dataset using pandas.
	•	Includes error handling for missing or incorrect paths.

3. First Transformation Function
	•	convert_data_types(df) converts:
	•	signup_date → datetime
	•	age → numeric
	•	purchase_amount → numeric
	•	Handles invalid or malformed values with coercion.
	•	Added a safeguard to skip transformation if loading fails.
To be Continued
