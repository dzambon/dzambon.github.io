
def get_field(field, default=None):
    print(field)
    return input()

handler = get_field("handler")
date = get_field("YYYY-MM-dd")
typ = get_field("type {preprint/journal/conference}")

print("{}-{}.md".format(date, handler))
print("---")
print("collection: publications")
print("permalink: /publications/{}".format(handler))
print("label: {}".format(handler))
print("year: {}".format(date[:4]))
print("date: {}".format(date))

print("type: {}".format(typ))
print("title: ")
print("authors: ")
print("venue: ")
print("paper: ")
print("preprint: ")
print("bibtex: true")
print("code: ")
print("abstract: true")
print("doi: ")
print("pages: ")
print("thumbnail: false")

print("---")
