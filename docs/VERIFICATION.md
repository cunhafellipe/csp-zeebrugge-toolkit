# Verification record

Portfolio refresh · 8 November 2026

- `gradle test --console=plain`: all 28 Spock specifications passed locally.
- Python regression test generates three PNG charts, a dwell-alert CSV and KPI
  JSON, and reconciles alert rows with the breach count. Passed.
- Fixed the report generator's unnormalised hourly weights, which previously
  caused NumPy to reject the distribution before generating any report.
- Inline dashboard JavaScript syntax check passed.
- Chromium: blocked-booking filter, empty search and filtered CSV passed.
- Landing page links and actual preview image checked. VBS desktop/mobile fit
  and zero uncaught JavaScript errors checked.
- Oracle SQL and licensed Navis production integration were not executed.

## Browser evidence

Desktop screenshots use a 1440 × 1040 viewport; mobile screenshots use 390 × 844.
These are actual Chromium captures of the built applications, not design mockups.
Screenshots show sample data. External map, chart-library or weather availability
can vary independently of the application.

- [Desktop capture](screenshots/desktop.png)
- [Mobile capture](screenshots/mobile.png)
- [Local commands and demo boundary](PORTFOLIO.md)

The public deployment is built from the committed source by
`.github/workflows/portfolio-pages.yml`. Review its Actions run for the exact
commit and deployment result; this note is not a claim of production integration
certification, a full accessibility audit or a penetration test.
