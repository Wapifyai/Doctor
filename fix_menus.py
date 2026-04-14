import os, re
files = ['about.html', 'contact.html', 'Facilities.html', 'testimonial.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace href="index.html#services" with href="index.html#tour" and Services -> Tour
    content = re.sub(r'(href=\"index\.html#)services(\".*?>\s*)Services(\s*</a)', r'\g<1>tour\g<2>Tour\g<3>', content, flags=re.DOTALL|re.IGNORECASE)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Done!')
