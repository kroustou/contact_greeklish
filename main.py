from slugify import slugify

INPUT = 'contacts.csv'

out = ''
slugify.safe_chars = ','
with open(INPUT, 'rb') as csvfile:
    for contact in csvfile.readlines():
        if contact.split(',')[0]:
            greeklish = slugify(contact).replace('-', ' ')
            print greeklish
            out += greeklish + '\n'

with open('output.csv', 'w') as res:
    res.write(out)
