from bs4 import BeautifulSoup, element
from re import sub
from src import styleandtextretriver
from src import toimage


def getmotdtoimg(html, icon, players, servername=None):
    html = html.split("\n")
    for i in range(0, len(html)):
        html[i] = html[i].replace("\/", "/")
        html[i] = html[i].replace(";", "")
        # Truck, cause bs4 removes extra spacs, which is important in motds
        html[i] = sub(r"( )\1+", lambda m: "⛟" *
                      (m.end()-m.start()), html[i])
    alltextandstyles = []
    for i in range(0, len(html)):
        alltextandstyles.append([])
        soup = BeautifulSoup(html[i], 'html.parser')
        all_elements = list(soup.children)
        for x in all_elements:
            if type(x) == element.NavigableString:
                alltextandstyles[i].append(
                    {'text': str(x), 'styles': {
                        "color": None, "font-weight": None, "font-style": None, "text-decoration": None}}
                )
            else:
                stuff = styleandtextretriver.get_as_list(x)
                alltextandstyles[i].extend(stuff)

    for x in alltextandstyles:
        for y in x:
            y['text'] = y['text'].replace("⛟", " ")

    return toimage.toImage(alltextandstyles, icon, players, servername)
