import asyncio
import datetime

from PIL import Image, ImageDraw, ImageFont

from utils.misc.certificate.photograph import photo_link


async def write_to_certificate(fullname, cls_num, science, cer_id):
    image = Image.open("data/images/cer.jpg")

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("data/fonts/times.ttf", 120)
    font_science = ImageFont.truetype("data/fonts/times.ttf", 80)
    font_date = ImageFont.truetype("data/fonts/times.ttf", 40)

    position = (1440, 740)
    position_science = (1050, 980)
    position_date = (2050, 1540)

    TEXT_COLOR = (0, 0, 0)

    text_bbox = draw.textbbox(position, fullname, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_position = (position[0] - text_width / 2, position[1])

    draw.text(text_position, fullname, fill=TEXT_COLOR, font=font)
    text = f"{cls_num}-sinf {science} fani"
    draw.text(position_science, text, fill=TEXT_COLOR, font=font_science)
    text_date = f"{datetime.datetime.now().strftime('%d-%m-%Y')}"
    draw.text(position_date, text_date, fill=TEXT_COLOR, font=font_date)

    image.save(f"data/images/{cer_id}.jpg")
    image.close()

    return await photo_link(f"data/images/{cer_id}.jpg")


# image = asyncio.run(write_to_certificate("Raximov Ilxomjon Iqboljon o'g'li", 11, "MATEMATIKA", 'c1c5e15e'))
# print(image)
