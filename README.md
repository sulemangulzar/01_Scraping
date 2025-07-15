# 🏢 US Largest Companies by Revenue – Web Scraper

This Python project scrapes data from a Wikipedia table that lists the **largest companies in the United States by revenue**.

It collects the data using `requests` and `BeautifulSoup`, stores it in a `pandas` DataFrame, and then saves it to a `.txt` file.

---

## 📚 What This Project Does

- Connects to [this Wikipedia page](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)
- Finds the table of companies ranked by revenue
- Extracts the table data: Rank, Name, Industry, Revenue, etc.
- Stores the data in a pandas DataFrame
- Writes the data to a file called `data.txt` for viewing
- (Optional) Also saves as `data.csv` for Excel/analysis

---

## 📁 Files Included

| File        | Description                                      |
|-------------|--------------------------------------------------|
| `main.py`   | The Python script that scrapes the data          |
| `data.txt`  | Text file with the scraped data in table format  |
| `data.csv`  | *(Optional)* CSV file version of the data        |

---

## ✅ Requirements

Before running the script, make sure you have Python installed.  
You also need to install the following Python libraries:

```bash
pip install requests beautifulsoup4 pandas
