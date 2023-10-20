# Решение задачи №4 / Системное программирование
- Ткачик Андрей Артурович
- 4
- Решение представляет собой единственный файл files_check.py. Перед запуском программы требуется наличие Levenshtein в python того, кто будет тестировать данную программу. При ее остуствии достаточно написать в терминал:
```pip install levenstein```. Файл запускатеся через стандартные инструкции: ```python3 file_check.py```.
- Код выполняет поставленные задачи, а именно отсеивает по порогу схожести файлы, сама программа также exception-safety. Реализация происходит через общий блок для всех функций, который позже используется при поиске индентичных файлов и схожих файлов. Для работы с директориями и самими файлами используется библиотека os, а для поиска различий Leneshtein. 
