import os 

def generate():
    os.system('auto-py-to-exe')
    # os.system('pyinstaller --noconfirm --onefile --console --icon "D:/Personal_projects/Oxford-Dictionary-API-CLI-Utility/dictionary.ico"  "D:/Personal_projects/Oxford-Dictionary-API-CLI-Utility/dictionary.py"')

if __name__=="__main__":
    generate()