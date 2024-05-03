import os
import subprocess


def convert_docx_to_pdf(input_docx, output_folder):
    try:
        output_pdf = os.path.join(output_folder, os.path.basename(input_docx)[:-4] + "pdf")
        command = ['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', output_folder, input_docx]
        subprocess.run(command)
        return output_pdf
    except Exception as e:
        print("Conversion failed:", e)
        return None
