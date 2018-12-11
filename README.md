# CurlyBracesRemover
Small tool to change all the {"XXXX"} to "XXXX" in the choose text file. I use it because C++ doesn't treat {"XX"} as char*, but C does.
------------------------------------------

# Methods lookup:
<main.py>
  1. Load and use Qt .ui file directly which is produced from QtCreator.
      And few buttons clicked events are handled.
  2. New my own dialog to inherit QDialog. And show it under a QApplication.
  3. Use QFileDialog to select the existing file.
  4. Use ntpath to split the dir_name and file_name.
  5. Use os.path.splitext to split the file extension.
  6. Use QMessageBox.information or QMessageBox.warning to pop msg box.
  7. Invoke method in another python module. Which is remove_curly_brasces.

<curly_braces_remover.py>  
  1. Open(), readline(), write() and close() to manipulate a text file.
  2. Use str.find() to locate the index of the specified character.
  3. Few basic list operations.
    3-1. Check if is empty
    3-2. Init an empty list.
    3-3. Use append() to add a new element.
    3-4. Use enumerate() to iterate. Which is able to grab index and value
        at the same time.
  4. Few basic str operations:
    4-1. Init a empty str.
    4-2. Copy a partial str with given start_idx and end_idx.
   
