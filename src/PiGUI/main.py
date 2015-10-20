from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class centeralLayout(Widget):
    def topLayout(self):
        pageLayout = GridLayout()
        menu = BoxLayout()
        pageLayout.add_widget(menu)
        menu1_3 = BoxLayout(cols = 5, rows = 1,size_hint=(1,1))
        menu2_3 = BoxLayout() #blank 2/3 of menu
        menu3_3 = BoxLayout() #blank 3/3 of menu
        menu.add_widget(menu1_3)
        menu.add_widget(menu2_3)
        menu.add_widget(menu3_3)
        
        fileButton = Button(text = "file")
        editButton = Button(text = "edit")
        helpButton = Button(text = "help")
    
        menu1_3.add_widget(fileButton)
        menu1_3.add_widget(editButton)
        menu1_3.add_widget(helpButton)
        
        page = GridLayout()
        pageLayout.add_widget(page)
        '''
        
        graphics attributes for main page goes here
        ...we should also learn some .kv for styling so we don't need to write attributes in file
        
        '''
        
        return pageLayout
        
        
    

class myApp(App,centeralLayout):
    def build(self):
        finalLayout = super(myApp,self).topLayout()
        return finalLayout
    
myApp().run()
    
