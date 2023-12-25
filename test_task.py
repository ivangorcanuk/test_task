csv_gen = (row for row in open('WikiMatrix.ru.txt', 'r', encoding="utf-8"))
with open('result.txt', 'w', encoding="utf-8") as output_file:
    for line in csv_gen:  # Обработка и запись в новый файл
        if len(line.split(' ')) <= 10:
            output_file.write(line)
