# Zeebrugge toolkit portfolio walkthrough

1. Open the project landing page to see how the three modules connect.
2. Open VBS analytics, compare the hourly bookings and weekly pressure heatmap.
3. Search or filter the sample bookings, and export the current selection.
4. Inspect the Groovy gate interceptor and its Spock specifications.
5. Run the Python reporting pipeline to produce real CSV/JSON/PNG artifacts.

## Run the browser demo

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000/`. Chart.js is pinned to 4.4.8 and requires internet.
Summary charts describe a synthetic day; the seven booking examples are a
separate illustrative sample, not the population behind every summary total.

## Run code verification

```sh
gradle test
python3 -m pip install -r bi-reporting/requirements.txt
python3 -m unittest discover -s bi-reporting/python -p 'test_*.py'
python3 bi-reporting/python/n4_report_generator.py
```

Reports are written to ignored `reports/`. The regression test generates and
reconciles all five output artifacts in a temporary directory. Groovy tests run
against local fixtures; production deployment requires the licensed Navis SDK,
real terminal configuration and integration validation. Oracle SQL is a design
example and was not executed against a live N4/Oracle warehouse.
