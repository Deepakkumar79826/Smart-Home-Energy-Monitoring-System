from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import pandas as pd

from config.settings import (
    CSV_FILE,
    PDF_FILE
)


def generate_pdf():

    df = pd.read_csv(
        CSV_FILE
    )

    document = SimpleDocTemplate(
        PDF_FILE
    )

    styles = (
        getSampleStyleSheet()
    )

    story = []

    story.append(

        Paragraph(
            "Smart Home Energy Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(
            1,
            20
        )
    )

    story.append(

        Paragraph(
            f"Total Records: {len(df)}",
            styles["BodyText"]
        )
    )

    story.append(

        Paragraph(
            f"Maximum Power: "
            f"{df['power'].max():.2f} W",
            styles["BodyText"]
        )
    )

    story.append(

        Paragraph(
            f"Total Energy: "
            f"{df['energy'].max():.4f} kWh",
            styles["BodyText"]
        )
    )

    story.append(

        Paragraph(
            f"Total Cost: ₹"
            f"{df['cost'].max():.2f}",
            styles["BodyText"]
        )
    )

    document.build(
        story
    )

    print(
        "PDF Generated Successfully"
    )


if __name__ == "__main__":

    generate_pdf()