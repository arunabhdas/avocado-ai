from flexx import flx

class Avocado(flx.Widget):

    def init(self):
        with flx.HBox():
            flx.Button(text='hello', flex=1)
            flx.Button(text='world', flex=2)

app = flx.App(Avocado)
app.launch('app')  # to run as a desktop app
# app.launch('browser')  # to open in the browser
flx.run()  # mainloop will exit when the app is closed