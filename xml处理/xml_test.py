import xml.etree.ElementTree as ET

tree = ET.parse("first_xml")
root = tree.getroot()

print(root)

for i in root:
    # print(i)
    print("    ", end="")
    print(i.tag)
    print("    ", end="")
    print(i.attrib, end="---\n")
    print("    ", end="")
    print(i.text)
    for m in i:
        # print(m)
        print("        ", end="")
        print(m.tag.strip())
        print("        ", end="")
        print(m.attrib)
        print("        ", end="")
        print(m.text.strip())

# for i in root:
#
#     # aaa = root.iter("string")
#     # print(aaa)
#     for m in i.iter("food"):
#         print(m.text)

