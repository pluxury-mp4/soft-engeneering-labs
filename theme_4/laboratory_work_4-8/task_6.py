# Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные имена файлов c расширением .png, независимо от регистра имен и расширений.

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

png_files = {file.lower() for file in files if file.lower().endswith('.png')}
print(*sorted(png_files))