import unittest
import tempfile
import json
from pathlib import Path
from unittest.mock import patch
import n4_report_generator as report


class ReportPipelineTest(unittest.TestCase):
    def test_full_report_generates_reconcilable_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            charts = Path(directory) / 'charts'
            with patch.object(report, 'OUTPUT_DIR', directory), patch.object(report, 'CHART_DIR', str(charts)):
                report.main()
            manifests = list(Path(directory).glob('kpis_*.json'))
            self.assertEqual(len(manifests), 1)
            kpis = json.loads(manifests[0].read_text())
            self.assertEqual(kpis['total_containers'], 400)
            self.assertEqual(kpis['gate_total'], 1200)
            self.assertEqual(len(list(charts.glob('*.png'))), 3)
            import pandas as pd
            alerts = pd.read_csv(next(Path(directory).glob('dwell_alerts_*.csv')))
            self.assertEqual(len(alerts), kpis['sla_breach_count'])
            self.assertTrue((alerts['dwell_days'] > report.SLA_DWELL).all())


if __name__ == '__main__':
    unittest.main()
