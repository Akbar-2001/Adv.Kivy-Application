screen_helper = """
ScreenManager:
    HomeScreen:
    SignScreen:
    MainScreen:
    CoursesScreen:
    AdmissionprocedureScreen:
    AdministrationScreen:
    FeeScreen:
    AboutScreen:
    

############################################################################################################
<HomeScreen>:
    name: 'home'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
    Image:
        source: "snti.png"
        pos_hint: {"center_x": .5, "center_y": .85}
        size_hint: .60, .60
    MDFloatLayout:
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .68}
        canvas:
            Color:
                rgb: 250/255, 250/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius:  [4]
        canvas.before:
            Color:
                rgb: 217/255, 217/255, 217/255, 1
            Line:
                width: 1.1
                rounded_rectangle: self.x, self.y, self.width, self.height, 4, 4, 4, 4, 100
        TextInput:
            hint_text: "Phone number, username or email"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            background_color: 1, 1, 1, 0
            font_size: "14sp"
            hint_text_color: 170/255, 170/255, 170/255, 1
            padding: 13    
            cursor_color: 0, 0, 0, 1
    MDFloatLayout:
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .59}
        canvas:
            Color:
                rgb: 250/255, 250/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius:  [4]
        canvas.before:
            Color:
                rgb: 217/255, 217/255, 217/255, 1
            Line:
                width: 1.1
                rounded_rectangle: self.x, self.y, self.width, self.height, 4, 4, 4, 4, 100
        TextInput:
            hint_text: "Password"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            background_color: 1, 1, 1, 0
            font_size: "14sp"
            password: True
            hint_text_color: 170/255, 170/255, 170/255, 1
            padding: 13    
            cursor_color: 0, 0, 0, 1
    Button:
        text: "Log In"
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .43}
        on_press: root.manager.current = 'main'
        background_color: 255, 0, 0, 
        font_size: "13sp"
        canvas.before:
            Color:
                rgb: 154/255, 203/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [4]
    MDTextButton:
        text: ">>SKIP>>"
        color: 172/255, 172/255, 172/255, 1
        pos_hint: {"center_x": .50, "center_y": .34}
        on_press: root.manager.current = 'main'
        font_size: "15sp"
    MDLabel:
        text: "OR"
        color: 172/255, 172/255, 172/255, 1
        pos_hint: {"center_y": .27}
        font_size: "15sp"
        halign: "center"
    MDFloatLayout:
        md_bg_color: 230/255, 230/255, 230/255, 1
        size_hint: .36, .001
        pos_hint: {"center_x": .24, "center_y": .268}
    MDFloatLayout:
        md_bg_color: 230/255, 230/255, 230/255, 1
        size_hint: .36, .001
        pos_hint: {"center_x": .76, "center_y": .268}
    MDLabel:
        text: "Don't have an account?"
        color: 172/255, 172/255, 172/255, 1
        pos_hint: {"center_x": .68, "center_y": .2}
        font_size: "13sp"
    MDTextButton:
        text: "Sign up."
        color: 98/255, 170/255, 243/255, 1
        pos_hint: {"center_x": .695, "center_y": .2}
        on_press: root.manager.current = 'sign'
        font_size: "13sp"
    MDLabel:
        text: "scient institute of technology"
        color: 172/255, 172/255, 172/255, 1
        pos_hint: {"center_x": .74, "center_y": .06}
        font_size: "13sp"
<SignScreen>:
    name: 'sign'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
    Image:
        source: "snti.png"
        pos_hint: {"center_x": .5, "center_y": .85}
        size_hint: .60, .60
    MDFloatLayout:
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .68}
        canvas:
            Color:
                rgb: 250/255, 250/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius:  [4]
        canvas.before:
            Color:
                rgb: 217/255, 217/255, 217/255, 1
            Line:
                width: 1.1
                rounded_rectangle: self.x, self.y, self.width, self.height, 4, 4, 4, 4, 100
        TextInput:
            hint_text: "Email address"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            background_color: 1, 1, 1, 0
            font_size: "14sp"
            hint_text_color: 170/255, 170/255, 170/255, 1
            padding: 13    
            cursor_color: 0, 0, 0, 1
    MDFloatLayout:
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .59}
        canvas:
            Color:
                rgb: 250/255, 250/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius:  [4]
        canvas.before:
            Color:
                rgb: 217/255, 217/255, 217/255, 1
            Line:
                width: 1.1
                rounded_rectangle: self.x, self.y, self.width, self.height, 4, 4, 4, 4, 100
        TextInput:
            hint_text: "Phone number"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            background_color: 1, 1, 1, 0
            font_size: "14sp"
            hint_text_color: 170/255, 170/255, 170/255, 1
            padding: 13    
            cursor_color: 0, 0, 0, 1      
    MDFloatLayout:
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .50}
        canvas:
            Color:
                rgb: 250/255, 250/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius:  [4]
        canvas.before:
            Color:
                rgb: 217/255, 217/255, 217/255, 1
            Line:
                width: 1.1
                rounded_rectangle: self.x, self.y, self.width, self.height, 4, 4, 4, 4, 100
        TextInput:
            hint_text: "Full name"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            background_color: 1, 1, 1, 0
            font_size: "14sp"
            hint_text_color: 170/255, 170/255, 170/255, 1
            padding: 13    
            cursor_color: 0, 0, 0, 1      
    MDFloatLayout:
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .41}
        canvas:
            Color:
                rgb: 250/255, 250/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius:  [4]
        canvas.before:
            Color:
                rgb: 217/255, 217/255, 217/255, 1
            Line:
                width: 1.1
                rounded_rectangle: self.x, self.y, self.width, self.height, 4, 4, 4, 4, 100
        TextInput:
            hint_text: "Password"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            background_color: 1, 1, 1, 0
            font_size: "14sp"
            password: True
            hint_text_color: 170/255, 170/255, 170/255, 1
            padding: 13    
            cursor_color: 0, 0, 0, 1        
    Button:
        text: "Sign up"
        size_hint: .9, .07
        pos_hint: {"center_x": .5, "center_y": .32}
        on_press: root.manager.current = 'home'
        background_color: 255, 0, 0, 
        font_size: "13sp"
        canvas.before:
            Color:
                rgb: 154/255, 203/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [4]
    MDLabel:
        text: "Already have an account?"
        color: 172/255, 172/255, 172/255, 1
        pos_hint: {"center_x": .65, "center_y": .2}
        font_size: "13sp"
    MDTextButton:
        text: "Sign in."
        color: 98/255, 170/255, 243/255, 1
        pos_hint: {"center_x": .695, "center_y": .2}
        on_press: root.manager.current = 'home'
        font_size: "13sp"
    MDLabel:
        text: "scient institute of technology"
        color: 172/255, 172/255, 172/255, 1
        pos_hint: {"center_x": .74, "center_y": .06}
        font_size: "13sp"

############################################################################################################   
<MainScreen>:
    name: 'main'
###########################################################################################################



################################################################################################################
    ScreenManager:
        Screen:
            MDBoxLayout:
                orientation:'vertical'
                MDToolbar:
                    title: 'SCIENT'
                    left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                    elevation:10
                Widget:
                
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Courses'
                        on_press: root.manager.current = 'course'
                        IconLeftWidget:
                            icon: 'book-education-outline'
                    OneLineIconListItem:
                        text: 'Admission Procedure'
                        on_press: root.manager.current = 'ap'
                        IconLeftWidget:
                            icon: 'briefcase-check'
                    OneLineIconListItem:
                        text: 'Administration'
                        on_press: root.manager.current = 'admin'
                        IconLeftWidget:
                            icon: 'account-tie'
                    OneLineIconListItem:
                        text: 'Fee Structure'
                        on_press: root.manager.current = 'fee'
                        IconLeftWidget:
                            icon: 'bank'
                    OneLineIconListItem:
                        text: 'About'
                        on_press: root.manager.current = 'about'
                        IconLeftWidget:
                            icon: 'alert-circle-outline'
                                
################################################################################################################

<CoursesScreen>:
    name: 'course'
    MDBoxLayout:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "SCIENT INSTITUTE OF TECHNOLOGY"
    MDFloatingActionButton:
        id: button
        icon: "keyboard-backspace"
        pos: 245, 10
        on_press: root.manager.current = 'main'
            
################################################################################################################

<AdmissionprocedureScreen>:
    name: 'ap'
    MDBoxLayout:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "SCIENT INSTITUTE OF TECHNOLOGY"
    MDFloatingActionButton:
        id: button
        icon: "keyboard-backspace"
        pos: 245, 10
        on_press: root.manager.current = 'main'
            
################################################################################################################

<AdministrationScreen>:
    name: 'admin'
    MDBoxLayout:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "SCIENT INSTITUTE OF TECHNOLOGY"
    MDFloatingActionButton:
        id: button
        icon: "keyboard-backspace"
        pos: 245, 10
        on_press: root.manager.current = 'main'
            
################################################################################################################

<FeeScreen>:
    name: 'fee'
    MDBoxLayout:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "SCIENT INSTITUTE OF TECHNOLOGY"
    MDFloatingActionButton:
        id: button
        icon: "keyboard-backspace"
        pos: 245, 10
        on_press: root.manager.current = 'main'
            
################################################################################################################

<AboutScreen>:
    name: 'about'
    MDBoxLayout:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "SCIENT INSTITUTE OF TECHNOLOGY"
    MDFloatingActionButton:
        id: button
        icon: "keyboard-backspace"
        pos: 245, 10
        on_press: root.manager.current = 'main'
        
################################################################################################################

  
    
"""
