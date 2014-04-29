import mechanize
import cookielib

# Browser
br = mechanize.Browser()

r = br.open('http://google.com')
html = r.read()

 # Show the source
print html
 # or
print br.response().read()

 # Show the html title
print br.title()

 # Show the response headers
print r.info()
 # or
print br.response().info()

 # Show the available forms
for f in br.forms():
    print f

     # Select the first (index zero) form
    br.select_form(nr=0)

     # Let's search
    br.form['q']='weekend codes'
    br.submit()
    print br.response().read()

     # Looking at some results in link format
    for l in br.links(url_regex='stockrt'):
        print l
