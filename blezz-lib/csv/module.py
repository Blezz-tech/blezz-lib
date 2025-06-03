import re
import csv


START_HTML_DOCUMENT = """
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
    It will be read and overwritten.
    DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
"""


END_HTML_DOCUMENT = """
</DL><p>
"""


def extract_links(markdown_text):
    pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    return pattern.findall(markdown_text)


def md2csv(from_file, to_file):

    with open(from_file, 'r', encoding='utf-8') as file:
        content = file.read()

    links = extract_links(content)

    with open(to_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['text', 'url'])
        writer.writerows(links)

    print(f"Извлечено и сохранено {len(links)} ссылок в {to_file}")


def csv2html(from_file, to_file):
    with open(from_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        text = ""
        text += START_HTML_DOCUMENT

        for row in reader:
            text += f"""   <DT><A HREF="{row['url']}">{row['text']}</A>\n"""
        
        text += END_HTML_DOCUMENT

        with open(to_file, "w", encoding="utf-8") as f:
            f.write(text)
