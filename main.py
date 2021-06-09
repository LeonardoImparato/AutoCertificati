from kivymd.app import MDApp 
from kivy.lang import Builder

#componenti 
#se come parametri metto centrer il bottone si orienta in base al centro - mettere solo x e y se vuoi orientarlo in base ai bordi

KV = """
Screen: 

    GridLayout:
        rows: 2

        ScrollView
            MDLabel:
                id: mdlab
                text: "Crea qui la tua autocertificazione veloce"
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None

        MDRaisedButton:
            id:mdbu
            text: "Compila"
            size_hint_x: 1
            size_hint_y: 0.2
            #on_press: app.nome_metodo

"""

class MainApp(MDApp):
    def build(self):
        self.title = "AutoCertificati" #titolo applicazione
        self.theme_cls.theme_style = "Light" #Dark --> tema dell'applicazione
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "900"
        return Builder.load_string(KV)

    #scrivere metodo da associare al click del bottone

MainApp().run()
