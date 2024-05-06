from django.core.files.temp import NamedTemporaryFile

def save_file_tpm(file):
    try:
        with NamedTemporaryFile(delete=False) as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name
        return temp_file_path
    finally:
        pass
