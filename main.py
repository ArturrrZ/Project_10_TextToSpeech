
from gtts import gTTS
import PyPDF2

# change the path to your pdf file just type text into TEXT variable
PATH_FOR_PDF_FILE='your_pdf.pdf'
TEXT="Any text you want"

text=""
with open(PATH_FOR_PDF_FILE,'rb') as file:
    pdf_reader=PyPDF2.PdfReader(file)
    # print(f"Number of pages: {len(pdf_reader.pages)}\n")
    for page in pdf_reader.pages:
        text_from_page=page.extract_text()
        text +=  text_from_page + "\n"

speech=gTTS(text=text,lang='en',slow=False)
speech.save('pdf_as_audio.mp3')

text_to_speech=gTTS(text=TEXT)
text_to_speech.save('text_to_speech.mp3')

