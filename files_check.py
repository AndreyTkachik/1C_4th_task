import os

# Для корректной работы нужно подгрузить Levenshtein
import Levenshtein


# Общий блок сравнивания внутренностей файлов 
def compare_files(file1, file2, threshold):
    try:
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            content1 = f1.read()
            content2 = f2.read()

        # Использование возможностей Levenshtein для сравнивания бинарных файлов
        similarity = Levenshtein.ratio(content1, content2) * 100

        return similarity >= threshold, similarity
    except Exception as e:
        print(f"Произошла ошибка при сравнении файлов: {e}")
        return False, 0

# Поиск полностью одинаковых
def find_identical_files(dir1, dir2):
    try:
        # Не учитываются директории
        files1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
        files2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]

        for file1 in files1:
            for file2 in files2:
                if compare_files(os.path.join(dir1, file1), os.path.join(dir2, file2), 100)[0]:
                    print(f"{dir1}/{file1} - {dir2}/{file2}")
    except Exception as e:
        print(f"Произошла ошибка при поиске идентичных файлов: {e}")

# Поиск похожих файлов
def find_similar_files(dir1, dir2, threshold):
    try:
        # Не учитываются директории
        files1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
        files2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]

        for file1 in files1:
            for file2 in files2:
                is_similar, percent_similarity = compare_files(os.path.join(dir1, file1), os.path.join(dir2, file2), threshold)
                if is_similar:
                    print(f"{dir1}/{file1} - {dir2}/{file2} - {percent_similarity:.2f}% сходства")
    except Exception as e:
        print(f"Произошла ошибка при поиске похожих файлов: {e}")

# Поиск уникальный файлов
def find_unique_files(dir1, dir2):
    try:
        # Не учитываются директории
        files1 = set([f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))])
        files2 = set([f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))])

        unique_files_dir1 = files1 - files2
        unique_files_dir2 = files2 - files1

        for file in unique_files_dir1:
            print(f"Файл {file} присутствует в {dir1}, но отсутствует в {dir2}")

        for file in unique_files_dir2:
            print(f"Файл {file} присутствует в {dir2}, но отсутствует в {dir1}")
    except Exception as e:
        print(f"Произошла ошибка при поиске уникальных файлов: {e}")

# Основной блок выполнения
try:
    threshold = float(input("Введите пороговое значение процента сходства: "))
    dir1 = input("Введите название первой директории: ")
    dir2 = input("Введите название второй директории: ")

    find_identical_files(dir1, dir2)
    find_similar_files(dir1, dir2, threshold)
    find_unique_files(dir1, dir2)
except Exception as e:
    print(f"Произошла ошибка: {e}")