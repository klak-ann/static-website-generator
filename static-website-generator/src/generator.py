import os
import markdown2
from pathlib import Path

def main():
    """
    Головна функція для генерації статичного сайту.
    """
    # Визначаємо шляхи до папок
    content_dir = Path('content')
    output_dir = Path('output')
    template_file = Path('templates/base.html')

    # Створюємо папку output, якщо її не існує
    output_dir.mkdir(exist_ok=True)
    print(f"Папку '{output_dir}' створено або вона вже існує.")

    # 1. Читаємо базовий HTML-шаблон
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_html = f.read()
    except FileNotFoundError:
        print(f"Помилка: Файл шаблону '{template_file}' не знайдено.")
        print("Будь ласка, створіть файл 'base.html' у папці 'templates'.")
        return

    # 2. Шукаємо всі markdown-файли у папці content
    markdown_files = list(content_dir.glob('*.md'))

    if not markdown_files:
        print(f"У папці '{content_dir}' не знайдено файлів з розширенням .md")
        return

    print(f"Знайдено {len(markdown_files)} markdown-файлів для обробки...")

    # 3. Обробляємо кожен знайдений файл
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Конвертуємо markdown в HTML
        html_content = markdown2.markdown(markdown_content)

        # Вставляємо згенерований HTML у шаблон
        # Замінюємо спеціальний маркер {{ content }} на наш контент
        final_html = template_html.replace('{{ content }}', html_content)

        # Визначаємо ім'я для вихідного HTML-файлу
        output_filename = md_file.stem + '.html'
        output_path = output_dir / output_filename

        # Записуємо фінальний HTML у файл
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)

        print(f"-> Створено сторінку: {output_path}")

    print("\nГенерацію сайту завершено успішно! ✨")

if name == "main":
    main()
