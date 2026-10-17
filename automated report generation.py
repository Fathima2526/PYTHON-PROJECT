import os
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

# 1. Create a sample dataset and save it as CSV
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [30, 25, 35, 28],
    "Salary": [50000, 45000, 60000, 48000],
    "Department": ["HR", "IT", "Finance", "IT"],
}
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print("data.csv created successfully!")

# 2. Load the data and compute summary statistics
df = pd.read_csv("data.csv")
print("Data loaded successfully!\n")
print(df)

summary = df.describe()

# 3. Create the chart and SAVE it so it can go into the PDF
plt.figure(figsize=(6, 4))
df["Age"].hist(edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("chart.png")   # fix: the chart is now actually saved
plt.show()
plt.close()

# 4. Build the PDF report
pdf = canvas.Canvas("report.pdf", pagesize=A4)
width, height = A4

pdf.setFont("Helvetica-Bold", 22)
pdf.drawCentredString(width / 2, height - 50, "DATA ANALYSIS REPORT")

pdf.setFont("Helvetica", 12)
pdf.drawCentredString(width / 2, height - 80, "Automatically Generated Report")

# Summary table, now with row labels (count, mean, std, ...)
header = [""] + summary.columns.tolist()
rows = [[idx] + vals for idx, vals in zip(summary.index, summary.round(2).values.tolist())]
table_data = [header] + rows

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
]))

# Place the table below the title, using its real height
table_w, table_h = table.wrapOn(pdf, width, height)
table_y = height - 110 - table_h
table.drawOn(pdf, (width - table_w) / 2, table_y)

# Place the chart below the table
chart_y = table_y - 30 - 200
if os.path.exists("chart.png"):
    pdf.drawImage("chart.png", 80, chart_y, width=400, height=200)

pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(30, 30, "Generated using Python")

pdf.save()
print("PDF report created: report.pdf")
