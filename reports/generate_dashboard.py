import pandas as pd
import json

# Load the dataset
df = pd.read_excel("data/raw/oecd_ai_incidents.xlsx.xlsx")
df['date'] = pd.to_datetime(df['date'])
df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')

# Prepare data for the dashboard
country_counts = df['country'].value_counts().to_dict()
date_counts = df.groupby('date_str').size().to_dict()

incidents_list = df[['title', 'date_str', 'country', 'summary']].to_dict(orient='records')

# Build the HTML dashboard
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Frontier AI Safety Policy Monitor - Dashboard</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<style>
    body {{
        font-family: 'Segoe UI', Arial, sans-serif;
        background-color: #0f172a;
        color: #e2e8f0;
        margin: 0;
        padding: 30px;
    }}
    h1 {{
        color: #38bdf8;
        text-align: center;
        margin-bottom: 5px;
    }}
    p.subtitle {{
        text-align: center;
        color: #94a3b8;
        margin-top: 0;
        margin-bottom: 40px;
    }}
    .container {{
        max-width: 1100px;
        margin: 0 auto;
    }}
    .charts {{
        display: flex;
        gap: 30px;
        flex-wrap: wrap;
        justify-content: center;
        margin-bottom: 40px;
    }}
    .chart-box {{
        background-color: #1e293b;
        border-radius: 12px;
        padding: 20px;
        flex: 1;
        min-width: 400px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    .chart-box h2 {{
        color: #38bdf8;
        font-size: 18px;
        margin-top: 0;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        background-color: #1e293b;
        border-radius: 12px;
        overflow: hidden;
    }}
    th, td {{
        padding: 12px 15px;
        text-align: left;
        border-bottom: 1px solid #334155;
    }}
    th {{
        background-color: #0ea5e9;
        color: #0f172a;
    }}
    tr:hover {{
        background-color: #334155;
    }}
    .stats {{
        display: flex;
        gap: 20px;
        justify-content: center;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }}
    .stat-card {{
        background-color: #1e293b;
        border-radius: 12px;
        padding: 20px 30px;
        text-align: center;
        min-width: 150px;
    }}
    .stat-card .number {{
        font-size: 32px;
        font-weight: bold;
        color: #38bdf8;
    }}
    .stat-card .label {{
        color: #94a3b8;
        font-size: 14px;
    }}
</style>
</head>
<body>
<div class="container">
    <h1>Frontier AI Safety Policy Monitor</h1>
    <p class="subtitle">Tracking AI safety incidents, security risks, and policy developments</p>

    <div class="stats">
        <div class="stat-card">
            <div class="number">{len(df)}</div>
            <div class="label">Total Incidents Tracked</div>
        </div>
        <div class="stat-card">
            <div class="number">{df['country'].nunique()}</div>
            <div class="label">Countries Involved</div>
        </div>
        <div class="stat-card">
            <div class="number">{df['date'].nunique()}</div>
            <div class="label">Days Covered</div>
        </div>
    </div>

    <div class="charts">
        <div class="chart-box">
            <h2>Incidents by Country</h2>
            <canvas id="countryChart"></canvas>
        </div>
        <div class="chart-box">
            <h2>Incidents Over Time</h2>
            <canvas id="timeChart"></canvas>
        </div>
    </div>

    <h2 style="color:#38bdf8;">Incident Log</h2>
    <table>
        <tr><th>Date</th><th>Title</th><th>Country</th></tr>
        {"".join(f"<tr><td>{row['date_str']}</td><td>{row['title']}</td><td>{row['country']}</td></tr>" for row in incidents_list)}
    </table>
</div>

<script>
const countryLabels = {json.dumps(list(country_counts.keys()))};
const countryData = {json.dumps(list(country_counts.values()))};

new Chart(document.getElementById('countryChart'), {{
    type: 'bar',
    data: {{
        labels: countryLabels,
        datasets: [{{
            label: 'Incidents',
            data: countryData,
            backgroundColor: '#38bdf8'
        }}]
    }},
    options: {{
        plugins: {{ legend: {{ display: false }} }},
        scales: {{
            x: {{ ticks: {{ color: '#94a3b8' }} }},
            y: {{ ticks: {{ color: '#94a3b8' }} }}
        }}
    }}
}});

const timeLabels = {json.dumps(list(date_counts.keys()))};
const timeData = {json.dumps(list(date_counts.values()))};

new Chart(document.getElementById('timeChart'), {{
    type: 'line',
    data: {{
        labels: timeLabels,
        datasets: [{{
            label: 'Incidents',
            data: timeData,
            borderColor: '#f87171',
            backgroundColor: 'rgba(248,113,113,0.2)',
            tension: 0.3,
            fill: true
        }}]
    }},
    options: {{
        plugins: {{ legend: {{ display: false }} }},
        scales: {{
            x: {{ ticks: {{ color: '#94a3b8' }} }},
            y: {{ ticks: {{ color: '#94a3b8' }} }}
        }}
    }}
}});
</script>
</body>
</html>
"""

with open("dashboard/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Dashboard generated successfully at dashboard/index.html")