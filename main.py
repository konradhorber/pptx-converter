from pptx import Presentation

prs = Presentation("data/test_slide_bcg.pptx")
slides = prs.slides

for slide in slides:
    shapes = slide.shapes
    for shape in shapes:
        if not shape.has_text_frame:
            continue
        paragraphs = shape.text_frame.paragraphs
        for paragraph in paragraphs:
            print(paragraph.text)
        print()
    print()

# print(shapes.title.text)
# print(shapes[3].text_frame.paragraphs[0].text)
