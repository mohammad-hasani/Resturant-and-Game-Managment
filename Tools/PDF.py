from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

class PDF(object):
    def __init__(self):
        pass

    def create_pdf(self, data):
        max_row_in_page = 10
        width, height = letter
        counter = 0
        pdf = None
        tmp_data = list()
        for i in data:
            for j in i:
                tmp_data.append(j)
        data = tmp_data
        for i, item in enumerate(data):
            food = item[2]
            count = item[1]
            price = item[3]
            total_price_of_row = float(count) * float(price)
            if i % max_row_in_page == 0:
                counter += 1
                if pdf is not None:
                    pdf.save()
                filename = 'pdf' + str(counter) + '.pdf'
                pdf = canvas.Canvas(filename, pagesize=letter)
            pdf.drawCentredString((width / 5) * 1, ((height / max_row_in_page) * (max_row_in_page - i - 1)), str(food))
            pdf.drawCentredString((width / 5) * 2, ((height / max_row_in_page) * (max_row_in_page - i - 1)), str(price))
            pdf.drawCentredString((width / 5) * 3, ((height / max_row_in_page) * (max_row_in_page - i - 1)), str(count))
            pdf.drawCentredString((width / 5) * 4, ((height / max_row_in_page) * (max_row_in_page - i - 1)), str(total_price_of_row))
            if i == len(data) - 1 and i % max_row_in_page != 0:
                pdf.save()