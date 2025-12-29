import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [30, 25, 35, 28],
    "Salary": [50000, 45000, 60000, 48000],
    "Department": ["HR", "IT", "Finance", "IT"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print("data.csv created successfully!")


df = pd.read_csv("data.csv")
print("Data loaded successfully!\n")
print(df)



summary = df.describe()

plt.figure(figsize=(6,4))
df["Age"].hist(edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
plt.close()


pdf = canvas.Canvas("report.pdf", pagesize=A4)
width, height = A4


pdf.setFont("Helvetica-Bold", 22)
pdf.drawCentredString(width/2, height - 50, "DATA ANALYSIS REPORT")


pdf.setFont("Helvetica", 12)
pdf.drawCentredString(width/2, height - 80, "Automatically Generated Report")

table_data = [summary.columns.tolist()] + summary.round(2).values.tolist()

table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.gray),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black)
]))

table.wrapOn(pdf, width, height)
table.drawOn(pdf, 30, height - 350)


if os.path.exists("chart.png"):
    pdf.drawImage("chart.png", 80, height - 550, width=400, height=200)


pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(30, 30, "Generated using Python")

pdf.save()
print("PDF report created: report.pdf")
