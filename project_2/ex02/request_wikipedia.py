import sys
import requests
import wikipedia
import re

wikipedia.set_lang("pt")

def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text.strip()

def convert_wiki_markdown(text):
    return text.replace('[[', '[').replace(']]', ']')

def get_title_from_wiki(search_input):
    wiki_results = wikipedia.search(search_input)
    if not wiki_results:
        print("No results found.\n")
        return None
    wiki_return_title = wiki_results[0]
    wiki_return_title = remove_html_tags(wiki_return_title)
    return wiki_return_title.strip()

def get_content_from_wiki(search_content_by_title):
    try:
        wiki_page = wikipedia.page(search_content_by_title)
    except:
        print("NOT FOUND!")
        return None
    wiki_return_content = wiki_page.content
    if wiki_return_content is None:
        return None
    wiki_return_content = remove_html_tags(wiki_return_content)
    wiki_return_content = convert_wiki_markdown(wiki_return_content)
    return wiki_return_content.strip()

def create_wiki_file(title, content):
    title = title.replace(' ', '_')
    with open(title, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    user_input = sys.argv
    if (len(user_input) != 2):
        print("ERROR: You need to pass at least and at most one argument.\n")
        return None
    wiki_title = get_title_from_wiki(user_input)
    wiki_content = get_content_from_wiki(wiki_title)
    if wiki_title and wiki_content:
        create_wiki_file(wiki_title, wiki_content)
    else:
        print("No valid content retrieved.")
        return None

main()
