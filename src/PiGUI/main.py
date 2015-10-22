from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class centeralLayout(Widget):
    def topLayout(self):
        masterPageLayout = BoxLayout(orientation = 'vertical', rows = 2)
        
        menu = BoxLayout(cols = 3 )
        masterPageLayout.add_widget(menu)
        
        page = GridLayout()
        masterPageLayout.add_widget(page)
        
        menu1_3 = BoxLayout(cols = 5, rows = 1,size_hint=(1,.25))
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
        

        '''
        
        graphics attributes for main page goes here
        ...we should also learn some .kv for styling so we don't need to write attributes in file
        
        '''
        
        return masterPageLayout
        
        
    

class myApp(App,centeralLayout):
    def build(self):
        finalLayout = super(myApp,self).topLayout()
        return finalLayout
    
myApp().run()
    
