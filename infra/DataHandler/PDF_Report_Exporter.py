from fpdf import FPDF
from fpdf.fonts import FontFace

class PDF(FPDF):
    def __init__(self, title, author):
        super().__init__()
        self.title = title
        self.author = author
        self.chapter_num = 1

    def header(self):
        self.set_font("helvetica", "B", 15)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(1)
        # Printing title:
        self.cell(
            width,
            9,
            self.title,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=False,
        )
        # Performing a line break:
        self.ln(10)

    def footer(self):
        # Setting position at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Setting text color to gray:
        self.set_text_color(128)
        # Printing page number
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def __ChepterTile(self, num, label):
        self.set_font("helvetica", "", 13)
        self.set_text_color(255)
        # Setting background color
        self.set_fill_color(20, 20, 55)
        # Printing chapter name:
        self.cell(
            0,
            6,
            f"{label}",
            new_x="LMARGIN",
            new_y="NEXT",
            align="L",
            fill=True,
        )
        # Performing a line break:
        self.ln(4)

    def __ReportByAsset(self, asset_report):
        self.set_font("Times", size=12)

        self.chapter_num = 1
        for asset in asset_report:
            self.__ChepterTile(self.chapter_num, "Asset: " + asset['Asset'])
            self.set_text_color(0)
            self.chapter_num += 1
            
            self.set_fill_color(255, 255, 255)

            headings_style = FontFace(emphasis="BOLD", color=0, fill_color=(200, 220, 255))
            with self.table(headings_style=headings_style) as table:
                row = table.row()
                row.cell("Data")
                row.cell("Lucro/Prejuízo")
                for date, profit in asset["Profit"].items():
                    row = table.row()
                    row.cell(str(date))
                    row.cell(f"R$ {profit:.2f}")

            self.ln()
            qnt = asset["Holding"].Amount
            price = asset["Holding"].Average_Price

            headings_style = FontFace(emphasis="italics",color=0, fill_color=(210, 255, 210))
            with self.table(headings_style=headings_style) as table:
                row = table.row()
                row.cell("Quantidade")
                row.cell("Preço médio")
                row = table.row()
                row.cell(str(qnt))
                row.cell(f"R$ {price:.2f}")

            self.ln()

    def __ReportByMonth(self, monthly_report):
        for date, assets in monthly_report.items():
            self.__ChepterTile(self.chapter_num, "Month: " +\
                               date.strftime("%B-%Y") +\
                               "   -   " + "Result: " +\
                               f"R$ {assets['Total']:.2f}")
            self.set_text_color(0)
            self.chapter_num += 1

            self.set_fill_color(255, 255, 255)

            headings_style = FontFace(emphasis="BOLD", color=0, fill_color=(200, 220, 255))
            with self.table(headings_style=headings_style) as table:
                row = table.row()
                row.cell("Ativo")
                row.cell("Lucro/Prejuízo")
                for asset, profit in assets.items():
                    if asset != "Total":
                        row = table.row()
                        row.cell(asset)
                        row.cell(f"R$ {profit:.2f}")

            self.ln()

    def PrintReportByAsset(self, info):
        self.add_page()
        self.__ReportByAsset(info)

    def PrintReportByMonth(self, info):
        self.add_page()
        self.__ReportByMonth(info)