from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class centeralLayout(Widget):
    def topLayout(self):
        pageLayout = GridLayout(cols= 1 , rows = 2 , orientation = "vertical")
        menu = BoxLayout(cols = 5, rows = 1, size_hint = [0.3,0.20])
        fileButton = Button(text = "file")
        editButton = Button(text = "edit")
        menu.add_widget(fileButton)
        menu.add_widget(editButton)
        page = GridLayout()
        
        pageLayout.add_widget(menu)
        pageLayout.add_widget(page)
        return pageLayout
        
        
    

class myApp(App,centeralLayout):
    def build(self):
        finalLayout = super(myApp,self).topLayout()
        return finalLayout
    
myApp().run()
        
