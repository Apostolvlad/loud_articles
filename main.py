from vk import Vk
from bs4 import BeautifulSoup
import csv
 
def csv_writer(data, path):
    with open(path, "w", encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)
    
def get_wall_ids(vk, owner_id, offset = 0):
    result = list()
    for offset in range(0, 100000, 100):
        response = vk.get_wall(owner_id, offset, "owner")
        items = response.get('items', {})
        if len(items) == 0: break
        for element in items:
            attachments = element.get('attachments')
            if type(attachments) is list and len(attachments) > 0:
                link = attachments[0].get('link', {})
                if link.get('description') == 'Article':
                    result.append(link.get('url'))
    return result

def get_article_info(vk, base_urls):
    client = vk.client
    result = list()
    for url in base_urls:
        result2 = list()
        response = client.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        result2.append(soup.title.text)
        element = soup.find(class_='articleView__content_list')
        text = element.get_text().replace('\n', '')
        text = text[:text.find('{"@context":')]
        result2.append(text)
        html_urls = soup.find_all("img", "article_object_sizer_inner")
        urls = list()
        result3 = list()
        for u in html_urls: 
            result3.append(u.get('src'))
            result3.append(',')
        result3 = result3[:-1]
        result2.append(''.join(result3))
        result.append(result2)
    return result

group_id = "-73519170"
def main():
    vk = Vk('7dd1fb5a7dd1fb5a7dd1fb5a397d8e54f877dd17dd1fb5a27c7084cec8da279527764d1')
    base_urls = get_wall_ids(vk, group_id)
    base_infos = get_article_info(vk, base_urls)
    csv_writer(base_infos, 'result.cvs')

if __name__ == "__main__":
    main()