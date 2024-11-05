def get_file_type(filename):
    extensions = {
        'Image': ['.jpg', '.jpeg', '.png' ],
        'Document': [ '.pdf', '.doc', '.docx'],
        'Spreadsheet': ['.xls', '.csv'],
        'Presentation': ['.ppt', '.pptx'],
        'Audio': ['.mp3', '.wav'],
        'Video': ['.mp4', '.mkv']
    }
    
    ext = '.' + filename.split('.')[-1].lower()
    return next((ftype for ftype, exts in extensions.items() if ext in exts), 'Unknown file type')

filename = input("Enter filename: ")
print(f"File type: {get_file_type(filename)}")
