from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

class dashboard(Widget):
    pass


'''
class centeralLayout(Widget):
    def topLayout(self):
        masterPageLayout = BoxLayout(orientation = 'vertical', rows = 2)
        
        menu = BoxLayout(cols = 3,size = (500,30), size_hint=(None,None))
        masterPageLayout.add_widget(menu)
        
        page = GridLayout()
        masterPageLayout.add_widget(page)
        
        menuLeft = BoxLayout(cols = 5, rows = 1)
        menu.add_widget(menuLeft)
        
        menuMiddle = BoxLayout()
        menu.add_widget(menuMiddle)
         
        menuRight = BoxLayout() 
        menu.add_widget(menuRight)
        
        fileButton = Button(text = "file")
        editButton = Button(text = "edit")
        helpButton = Button(text = "help")
        
      
            10/22/2015 6:50 PM
                Test buttons, not sure of function response yet   

        fileButton2 = Button(text='Value %d' % 1, size_hint_y=None, height=44)
        fileButton3 = Button(text='Value %d' % 2, size_hint_y=None, height=44)
        
        fileDropDown = DropDown()
        fileDropDown.add_widget(fileButton2)
        fileDropDown.add_widget(fileButton3)

        fileButton.bind(on_release=fileDropDown.open)
        
        #fileButton2.bind(on_release=lambda fileButton2: fileDropDown.select(fileButton2.text))
        #fileButton3.bind(on_release=lambda fileButton3: fileDropDown.select(fileButton3.text))
        
        
        menuLeft.add_widget(fileButton)
        menuLeft.add_widget(editButton)
        menuLeft.add_widget(helpButton)
        
        
        graphics attributes for main page goes here
        ...we should also learn some .kv for styling so we don't need to write attributes in file
        
        
        
        return masterPageLayout
        '''
        
finalLayout = Builder.load_file("my.kv")

class myApp(App):
    def build(self):
        #finalLayout = super(myApp,self).topLayout()
        return finalLayout
    
myApp().run()
    
