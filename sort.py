import xml.etree.ElementTree as ET
#don't work. Sad

def sortchildrenby(parent, attr):
    parent[:] = sorted(parent, key=lambda child: child.get(attr))


if __name__ == "__main__":
    tree = ET.parse('output.xml')
    root = tree.getroot()
    for child in root:
        sortchildrenby(child, child[1].text)
    tree.write('output.xml', encoding='windows-1251')
