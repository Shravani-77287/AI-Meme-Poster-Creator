from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_poster(
    template_path,
    caption,
    output_path
):

    image = Image.open(
        template_path
    )

    draw = ImageDraw.Draw(
        image
    )

    font = ImageFont.load_default()

    draw.text(
        (50,50),
        caption,
        fill="white",
        font=font
    )

    image.save(
        output_path
    )