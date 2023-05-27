## Лабораторна робота №4
Це скрипт, який надає статистику щодо заданого файлу.
#### Використання
1.Відкрийте командний рядок або термінал. 
2.Виконайте наступну команду:
```
python lab_4.py
```
3.Після чого команда видасть таку стрічку:
```
Enter the file path (or 'q' to quit): 
```
4.Варіанти введення:
- шлях до файлу який потрібно проаналізувати.
- символ 'q' для виходу з програми.

5.Якщо ввести шлях до файлу, отримаєте результат такого вигляду:
```
File: "path"
total lines: 9
empty lines: 3
lines with 'z': 4
'z' count: 32
lines with 'and': 3
```
6.Модуль буде продовжувати запитувати вас про нові файли для аналізу, поки ви не введете символ 'q' для виходу.