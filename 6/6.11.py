def main():
    name = input('input your name: ')
    descr = input('write down a few sentences about you: ')
    make_html(name, descr)

def make_html(h1, hr):
    tempfile = open('main.html', 'w')
    tempfile.write(f'''
        <html>
            <head>
            </head>
            <body>
                <center>
                    <h1>{h1}</h1>
                </center>
                <hr />
                    {hr}
                <hr />
            </body>
        </html>
        ''')


main()
