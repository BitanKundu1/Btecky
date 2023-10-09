import pyqrcode 
s="https://bitan-kundu.github.io/my-portfolio-website.github.io/"
url = pyqrcode.create(s)
url.svg("Portfolio_website.svg",scale=5)
