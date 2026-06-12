from reportlab.pdfgen import canvas

# Create PDF
pdf = canvas.Canvas("sample.pdf")

# Add text
pdf.drawString(
    100,
    750,
    "Hello, Welcome to ReportLab!"
)

pdf.drawString(
    100,
    720,
    "This PDF was created using Python."
)

# Save PDF
pdf.save()

print("PDF Created Successfully ✅")