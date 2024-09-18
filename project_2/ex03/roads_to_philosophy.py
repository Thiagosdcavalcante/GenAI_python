import requests
from bs4 import BeautifulSoup
import sys

def is_valid_link(link, current_title):
    parent = link.find_parent()
    if parent and (parent.name == 'i' or parent.name == 'em'):
        return False
    if '(' in link.text or ')' in link.text:
        return False
    href = link.get('href', '')
    if href.startswith('/wiki/') and not any(sub in href for sub in [':', '#', 'search']):
        link_title = link.get('title', '')
        if link_title.lower() == current_title.lower():
            return False
        return True
    return False

def navigate(title):
    visited_titles = set()
    start_url = "https://en.wikipedia.org"

    while title != "Philosophy":
        if title not in visited_titles:
            visited_titles.add(title)
            print(title)
            new_url = f"{start_url}/wiki/{title.replace(' ', '_')}"

            try:
                req = requests.get(new_url)
                soup = BeautifulSoup(req.text, 'html.parser')

                first_paragraph = soup.find(id="mw-content-text")
                if first_paragraph:
                    links = first_paragraph.select('p>a')
                    for link in links:
                        if is_valid_link(link, title):
                            title = link['title']
                            break
                    else:
                        print("It leads to a dead end!")
                        return None
                else:
                    print("Nenhum parágrafo encontrado.")
                    return None
                
            except Exception as e:
                print(f"Erro ao processar {new_url}: {str(e)}")
                return None
        else:
            print("It leads to an infinite loop!")
            return None

    return visited_titles

def main():
    user_input = sys.argv
    if len(user_input) != 2:
        print("\033[31mERROR: Você precisa passar exatamente um argumento.\033[0m")
        return None
    first_title =user_input[1] 
    result = navigate(user_input[1])

    if not result:
        return
    else:
        print(f"{len(result) - 1} caminhos de {first_title} para Philosophy!")

main()
