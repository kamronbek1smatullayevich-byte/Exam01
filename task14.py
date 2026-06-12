file_name = input("Fayl nomi: ")

if file_name.endswith(".pdf"):
    print("Fayl turi: pdf.")
elif file_name.endswith(".docx"):
    print("Fayl turi: docx")
elif file_name.endswith(".txt"):
    print("Fayl turi: txt")
else:
    print("Bu fayl .pdf, .docx yoki .txt bilan tugamaydi.")