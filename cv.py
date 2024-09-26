import mammoth
from flask import Flask, render_template_string

app = Flask(__name__)

def convert_docx_to_html_mammoth(docx_path):
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html_content = result.value  # The generated HTML
        return html_content

@app.route('/cv')
def display_cv():
    # Path to your Word document
    docx_path = r'C:\Users\Ashraf Ali\Documents\Ashraf Ali BA.CV.docx'
    
    # Convert the Word document to HTML using Mammoth
    cv_html = convert_docx_to_html_mammoth(docx_path)
    
    # Render the HTML on the webpage
    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My CV</title>
    </head>
    <body>
        <h1>My CV</h1>
        {cv_html}
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
