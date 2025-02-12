from reportlab.pdfgen import canvas
import random

# Create a new PDF file
def create_pdf(output_filename, text_content):
    # Initialize the canvas
    pdf = canvas.Canvas(output_filename)

    # Set font and size
    pdf.setFont("Helvetica", 30)

    # Write text at a specific position (x, y)
    pdf.drawString(100, 750, text_content)

    # Save the PDF
    pdf.save()

# Example usage
text_to_write = "Hello, this is a sample text in the PDF!"
output_file = f"voter_id_card{random.randint(1,1000)}.pdf"
create_pdf(output_file, text_to_write)

print(f"PDF created: {output_file}")
