from bs4 import element


def get_as_list(obj, extstyle=None):
    alldata = []

    style = {"color": None, "font-weight": None,
             "font-style": None, "text-decoration": None}
    if extstyle != None:
        style = extstyle
    if 'style' in obj.attrs:
        spanstyleaslist = obj.attrs['style'].split(":")
        style[spanstyleaslist[0]] = spanstyleaslist[1]

    stuffaslist = list(obj.children)
    for x in stuffaslist:
        if type(x) == element.NavigableString:
            alldata.append({'text': str(x), 'styles': style})
        else:
            alldata.extend(get_as_list(x, style))
    return alldata
