
with open('result.txt', 'w', encoding="utf-8") as output_file:
    with open('WikiMatrix.ru.txt', 'r', encoding="utf-8") as input_file:
        for line in input_file:  # Обработка и запись в новый файл
            if len(line.split(' ')) <= 10:
                output_file.write(line)