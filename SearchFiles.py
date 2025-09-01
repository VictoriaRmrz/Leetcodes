class Folder(object):
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subfolders = []
# Folder: Project
# -- Victoria.pdf
# -- ProjectVictoria.txt
# -- Documents : Folder
#    -- ProjectDocuments.txt
#    -- Python : Folder
#       -- PythonVic.py

class SearchFiles(object):
    def __init__(self):
        self.result = []

    def searching(self, folder: Folder, nameOfFile):
        nameOfFile = nameOfFile.lower()
        for file in folder.files:
            if nameOfFile in file.lower():
                self.result.append(file)
        for subfolder in folder.subfolders:
            self.searching(subfolder, nameOfFile) # recursividad
        return self.result

def main():
    root = Folder("Project")
    root.files = ["Victoria.pdf", "ProjectVictoria.txt"]
    documents = Folder("Documents")
    documents.files = ["ProjectDocuments.txt", "actaVictoria.docx"]
    root.subfolders.append(documents)
    Python = Folder("Python")
    Python.files = ["PythonVic.py"]
    documents.subfolders.append(Python)
    search = SearchFiles()
    solution = search.searching(root, "victoria")
    print(solution)

if __name__ == "__main__":
    main()

