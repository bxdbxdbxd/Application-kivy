from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout


from kivy.core.window import Window


Window.clearcolor = (196/255, 196/255, 196/255, 1)
Window.title = "Application"

#color_but_press = (46 / 255, 40 / 255, 40 / 255, 1)

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        btn_1 = GridLayout(cols=2, padding=[.2, .3], spacing=3, size_hint=(.7, .5))
        set_btn = AnchorLayout()
        schedule = Button(background_normal="", text="Распорядок дня",
                                background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        timetable = Button(background_normal="", text="Расписание",
                                font_size="15sp",
                                background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        homework = Button(background_normal="", text="Д/З",
                                font_size="15sp",
                                background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        exit = Button(background_normal="", text="Выход",
                                font_size="15sp",
                                background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        exit.bind(on_press=self.changer)
        timetable.bind(on_press=self.timetable)
        schedule.bind(on_press=self.schedule)
        homework.bind(on_press=self.homework)
        btn_1.add_widget(schedule)
        btn_1.add_widget(timetable)
        btn_1.add_widget(homework)
        btn_1.add_widget(exit)
        set_btn.add_widget(btn_1)
        self.add_widget(set_btn)

    def timetable(self, *args):
        self.manager.current = 'timetable'

    def schedule(self, *args):
        self.manager.current = 'schedule'

    def homework(self, *args):
        self.manager.current = 'homework'

    def changer(self, *args):
        self.manager.current = exit()




class Monday(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        self.i = 1
        super(Monday, self).__init__(**kwargs)
        exit_button = Button(background_normal="", text='<--', size_hint=(.2, .06), pos_hint={"x": .02, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25)
        exit_button.bind(on_press=self.changer)
        self.add_widget(exit_button)
        self.add_widget(Label(text='Понедельник', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(.15, .06),
                              pos_hint={"x": .43, "y": .92}, disabled_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25))
        add_button_monday = Button(background_normal="", text='Добавить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_button_monday.bind(on_press=self.add_label)
        #delete_but = Button(text='Удалить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .78}, background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        #delete_but.bind(on_press=self.delete_wid)
        #self.add_widget(delete_but)
        self.text_input = TextInput(size_hint=(.2, .06), pos_hint={"x": .78, "y": .85}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), multiline=False)
        self.add_widget(self.text_input)
        self.add_widget(add_button_monday)
        #mon_but = AnchorLayout(anchor_x='right', anchor_y='top', pos_hint={'center_x':.25, 'center_y':.4})
        boxl = BoxLayout(size_hint=(.6, .9), pos_hint={"x": .1, "y": .005})
     
        self.labels = StackLayout(orientation='tb-lr')
        boxl.add_widget(self.labels)
        self.add_widget(boxl)



    def add_label(self, instance):
        if len(self.text_input.text) < 31 and len(self.text_input.text) != 0 and self.i < 17:
            text = self.text_input.text
            self.text_input.text = ''
            a = Label(text=str(self.i) + ". " + text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint = (1.0, .06), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.i += 1
            self.labels.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'timetable'




class Tuesday(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        self.i = 1
        super(Tuesday, self).__init__(**kwargs)
        exit_button = Button(background_normal="", text='<--', size_hint=(.2, .06), pos_hint={"x": .02, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25)
        exit_button.bind(on_press=self.changer)
        self.add_widget(exit_button)
        self.add_widget(Label(text='Вторник', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(.15, .06),
                              pos_hint={"x": .43, "y": .92}, disabled_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25))
        add_button_tuesday = Button(background_normal="", text='Добавить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .92},
                                   background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_button_tuesday.bind(on_press=self.add_label)
        self.text_input = TextInput(size_hint=(.2, .06), pos_hint={"x": .78, "y": .85},
                                    background_color=(134 / 255, 117 / 255, 117 / 255, 1), multiline=False)
        print(self.text_input.text)
        self.add_widget(self.text_input)
        self.add_widget(add_button_tuesday)

        boxl = BoxLayout(size_hint=(.6, .9), pos_hint={"x": .1, "y": .005})

        self.labels = StackLayout(orientation='tb-lr')
        boxl.add_widget(self.labels)
        self.add_widget(boxl)

    def add_label(self, instance):
        if len(self.text_input.text) < 31 and len(self.text_input.text) != 0 and self.i < 17:
            text = self.text_input.text
            self.text_input.text = ''
            a = Label(text=str(self.i) + ". " + text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint = (1.0, .06), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.i += 1
            self.labels.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'timetable'




class Wednesday(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        self.i = 1
        super(Wednesday, self).__init__(**kwargs)
        exit_button = Button(background_normal="", text='<--', size_hint=(.2, .06), pos_hint={"x": .02, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25)
        exit_button.bind(on_press=self.changer)
        self.add_widget(exit_button)
        self.add_widget(Label(text='Среда', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(.15, .06),
                              pos_hint={"x": .43, "y": .92}, disabled_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25))
        add_button_wednesday = Button(background_normal="", text='Добавить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .92},
                                   background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_button_wednesday.bind(on_press=self.add_label)
        self.text_input = TextInput(size_hint=(.2, .06), pos_hint={"x": .78, "y": .85},
                                    background_color=(134 / 255, 117 / 255, 117 / 255, 1), multiline=False)
        print(self.text_input.text)
        self.add_widget(self.text_input)
        self.add_widget(add_button_wednesday)
        boxl = BoxLayout(size_hint=(.6, .9), pos_hint={"x": .1, "y": .005})

        self.labels = StackLayout(orientation='tb-lr')
        boxl.add_widget(self.labels)
        self.add_widget(boxl)

    def add_label(self, instance):
        if len(self.text_input.text) < 31 and len(self.text_input.text) != 0 and self.i < 17:
            text = self.text_input.text
            self.text_input.text = ''
            a = Label(text=str(self.i) + ". " + text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint = (1.0, .06), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.i += 1
            self.labels.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'timetable'




class Thursday(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        self.i = 1
        super(Thursday, self).__init__(**kwargs)
        exit_button = Button(background_normal="", text='<--', size_hint=(.2, .06), pos_hint={"x": .02, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25)
        exit_button.bind(on_press=self.changer)
        self.add_widget(exit_button)
        self.add_widget(Label(text='Четверг', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(.15, .06),
                              pos_hint={"x": .43, "y": .92}, disabled_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25))
        add_button_thursday = Button(background_normal="", text='Добавить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .92},
                                   background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_button_thursday.bind(on_press=self.add_label)
        self.text_input = TextInput(size_hint=(.2, .06), pos_hint={"x": .78, "y": .85},
                                    background_color=(134 / 255, 117 / 255, 117 / 255, 1), multiline=False)
        print(self.text_input.text)
        self.add_widget(self.text_input)
        self.add_widget(add_button_thursday)
        boxl = BoxLayout(size_hint=(.6, .9), pos_hint={"x": .1, "y": .005})

        self.labels = StackLayout(orientation='tb-lr')
        boxl.add_widget(self.labels)
        self.add_widget(boxl)

    def add_label(self, instance):
        if len(self.text_input.text) < 31 and len(self.text_input.text) != 0 and self.i < 17:
            text = self.text_input.text
            self.text_input.text = ''
            a = Label(text=str(self.i) + ". " + text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint = (1.0, .06), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.i += 1
            self.labels.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'timetable'




class Friday(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        self.i = 1
        super(Friday, self).__init__(**kwargs)
        exit_button = Button(background_normal="", text='<--', size_hint=(.2, .06), pos_hint={"x": .02, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25)
        exit_button.bind(on_press=self.changer)
        self.add_widget(exit_button)
        self.add_widget(Label(text='Пятница', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(.15, .06),
                              pos_hint={"x": .43, "y": .92}, disabled_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25))
        add_button_friday = Button(background_normal="", text='Добавить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .92},
                                   background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_button_friday.bind(on_press=self.add_label)
        self.text_input = TextInput(size_hint=(.2, .06), pos_hint={"x": .78, "y": .85},
                                    background_color=(134 / 255, 117 / 255, 117 / 255, 1), multiline=False)
        print(self.text_input.text)
        self.add_widget(self.text_input)
        self.add_widget(add_button_friday)
        boxl = BoxLayout(size_hint=(.6, .9), pos_hint={"x": .1, "y": .005})

        self.labels = StackLayout(orientation='tb-lr')
        boxl.add_widget(self.labels)
        self.add_widget(boxl)

    def add_label(self, instance):
        if len(self.text_input.text) < 31 and len(self.text_input.text) != 0 and self.i < 17:
            text = self.text_input.text
            self.text_input.text = ''
            a = Label(text=str(self.i) + ". " + text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint = (1.0, .06), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.i += 1
            self.labels.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'timetable'




class Saturday(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        self.i = 1
        super(Saturday, self).__init__(**kwargs)
        exit_button = Button(background_normal="", text='<--', size_hint=(.2, .06), pos_hint={"x": .02, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25)
        exit_button.bind(on_press=self.changer)
        self.add_widget(exit_button)
        self.add_widget(Label(text='Суббота', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(.15, .06),
                              pos_hint={"x": .43, "y": .92}, disabled_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25))
        add_button_saturday = Button(background_normal="", text='Добавить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .92},
                                   background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_button_saturday.bind(on_press=self.add_label)
        self.text_input = TextInput(size_hint=(.2, .06), pos_hint={"x": .78, "y": .85},
                                    background_color=(134 / 255, 117 / 255, 117 / 255, 1), multiline=False)
        print(self.text_input.text)
        self.add_widget(self.text_input)
        self.add_widget(add_button_saturday)
        boxl = BoxLayout(size_hint=(.6, .9), pos_hint={"x": .1, "y": .005})

        self.labels = StackLayout(orientation='tb-lr')
        boxl.add_widget(self.labels)
        self.add_widget(boxl)

    def add_label(self, instance):
        if len(self.text_input.text) < 31 and len(self.text_input.text) != 0 and self.i < 17:
            text = self.text_input.text
            self.text_input.text = ''
            a = Label(text=str(self.i) + ". " + text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint = (1.0, .06), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.i += 1
            self.labels.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'timetable'




class Sunday(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        self.i = 1
        super(Sunday, self).__init__(**kwargs)
        exit_button = Button(background_normal="", text='<--', size_hint=(.2, .06), pos_hint={"x": .02, "y": .92}, background_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25)
        exit_button.bind(on_press=self.changer)
        self.add_widget(exit_button)
        self.add_widget(Label(text='Воскресенье', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(.15, .06),
                              pos_hint={"x": .43, "y": .92}, disabled_color=(134 / 255, 117 / 255, 117 / 255, 1), font_size=25))
        add_button_sunday = Button(background_normal="", text='Добавить', size_hint=(.2, .06), pos_hint={"x": .78, "y": .92},
                                   background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_button_sunday.bind(on_press=self.add_label)
        self.text_input = TextInput(size_hint=(.2, .06), pos_hint={"x": .78, "y": .85},
                                    background_color=(134 / 255, 117 / 255, 117 / 255, 1), multiline=False)
        print(self.text_input.text)
        self.add_widget(self.text_input)
        self.add_widget(add_button_sunday)
        boxl = BoxLayout(size_hint=(.6, .9), pos_hint={"x": .1, "y": .005})

        self.labels = StackLayout(orientation='tb-lr')
        boxl.add_widget(self.labels)
        self.add_widget(boxl)

    def add_label(self, instance):
        if len(self.text_input.text) < 31 and len(self.text_input.text) != 0 and self.i < 17:
            text = self.text_input.text
            self.text_input.text = ''
            a = Label(text=str(self.i)+ ". " +text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint = (1.0, .06), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.i += 1
            self.labels.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'timetable'




class Timatable(Screen):
    def __init__(self, **kwargs):
        self.text_lab = ''
        super(Timatable, self).__init__(**kwargs)
        box_button_days = GridLayout(cols=1, padding=[.1, .1], spacing=2)
        exit_day = Button(background_normal="", text='<--', font_size=25, background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        monday = Button(background_normal="", text='Понедельник', background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        tuesday = Button(background_normal="", text='Вторник', background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        wednesday = Button(background_normal="", text='Среда', background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        thursday = Button(background_normal="", text='Четверг', background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        friday = Button(background_normal="", text='Пятница', background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        saturday = Button(background_normal="", text='Суббота', background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        sunday = Button(background_normal="", text='Воскресенье', background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        exit_day.bind(on_press=self.changer)
        monday.bind(on_press=self.mon)
        tuesday.bind(on_press=self.tue)
        wednesday.bind(on_press=self.wed)
        thursday.bind(on_press=self.thu)
        friday.bind(on_press=self.fri)
        saturday.bind(on_press=self.sat)
        sunday.bind(on_press=self.sun)
        box_button_days.add_widget(exit_day)
        box_button_days.add_widget(monday)
        box_button_days.add_widget(tuesday)
        box_button_days.add_widget(wednesday)
        box_button_days.add_widget(thursday)
        box_button_days.add_widget(friday)
        box_button_days.add_widget(saturday)
        box_button_days.add_widget(sunday)
        self.add_widget(box_button_days)

    def changer(self, *args):
        self.manager.current = 'home'

    def mon(self, *args):
        self.manager.current = 'mon'
    def tue(self, *args):
        self.manager.current = 'tue'
    def wed(self, *args):
        self.manager.current = 'wed'
    def thu(self, *args):
        self.manager.current = 'thu'
    def fri(self, *args):
        self.manager.current = 'fri'
    def sat(self, *args):
        self.manager.current = 'sat'
    def sun(self, *args):
        self.manager.current = 'sun'




class Homework(Screen):
    def __init__(self, **kwargs):
        super(Homework, self).__init__(**kwargs)
        exit_button_hw = Button(background_normal="", text='<--', font_size=25, size_hint=(.15, .06), pos_hint={"x": .015, "y": .92},
                                  background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        exit_button_hw.bind(on_press=self.changer)
        self.add_widget(exit_button_hw)
        self.add_widget(Button(background_normal="", size_hint=(.04, .25),
                            background_color=(184 / 255, 15 / 255, 10 / 255, 1), pos_hint={"x": .02, "y": .63}))
        self.add_widget(Button(background_normal="", size_hint=(.04, .25),
                            background_color=(239 / 255, 130 / 255, 13 / 255, 1), pos_hint={"x": .02, "y": .35}))
        self.add_widget(Button(background_normal="", size_hint=(.04, .25),
                            background_color=(76 / 255, 187 / 255, 23 / 255, 1), pos_hint={"x": .02, "y": .07}))



        red_but = Button(background_normal="", size_hint=(.1, .06), pos_hint={"x": .43, "y": .92},
                         background_color=(184 / 255, 15 / 255, 10 / 255, 1))
        red_but.bind(on_press=self.add_homework)
        self.add_widget(red_but)

        bx_red = BoxLayout(size_hint=(.9, .25), pos_hint={'center_x': .53, 'center_y': .755})
        self.sl = StackLayout(orientation="tb-lr", height=500, size_hint=(1, 2.5))
        sv = ScrollView(size_hint=(.8, 1))
        sv.add_widget(self.sl)
        bx_red.add_widget(sv)
        self.add_widget(bx_red)



        oran_but = Button(background_normal="", size_hint=(.1, .06), pos_hint={"x": .53, "y": .92},
                          background_color=(239 / 255, 130 / 255, 13 / 255, 1))
        oran_but.bind(on_press=self.add_homework_oran)
        self.add_widget(oran_but)

        bx_oran = BoxLayout(size_hint=(.9, .25), pos_hint={'center_x': .53, 'center_y': .475})
        self.sl_2 = StackLayout(orientation="tb-lr", height=500, size_hint=(1, 2.5))
        sv_2 = ScrollView(size_hint=(.8, 1))
        sv_2.add_widget(self.sl_2)
        bx_oran.add_widget(sv_2)
        self.add_widget(bx_oran)


        green_but = Button(background_normal="", size_hint=(.1, .06), pos_hint={"x": .63, "y": .92},
                           background_color=(76 / 255, 187 / 255, 23 / 255, 1))
        green_but.bind(on_press=self.add_homework_green)
        self.add_widget(green_but)

        bx_green = BoxLayout(size_hint=(.9, .25), pos_hint={'center_x': .53, 'center_y': .19})
        self.sl_3 = StackLayout(orientation="tb-lr", height=500, size_hint=(1, 2.5))
        sv_3 = ScrollView(size_hint=(.8, 1))
        sv_3.add_widget(self.sl_3)
        bx_green.add_widget(sv_3)
        self.add_widget(bx_green)



        self.add_work = TextInput(size_hint=(.2, .06), pos_hint={"x": .76, "y": .92}, multiline=False)
        self.add_widget(self.add_work)



    def add_homework(self, instance):
        if len(self.add_work.text) < 45 and len(self.add_work.text) != 0:
            text = self.add_work.text
            self.add_work.text = ''
            a = Label(text=text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint=(1.0, .1), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.sl.add_widget(a)
        else:
            pass

    def add_homework_oran(self, instance):
        if len(self.add_work.text) < 45 and len(self.add_work.text) != 0:
            text = self.add_work.text
            self.add_work.text = ''
            a = Label(text=text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint=(1.0, .1), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.sl_2.add_widget(a)
        else:
            pass

    def add_homework_green(self, instance):
        if len(self.add_work.text) < 45 and len(self.add_work.text) != 0:
            text = self.add_work.text
            self.add_work.text = ''
            a = Label(text=text, color=(46 / 255, 40 / 255, 40 / 255, 1), font_size=22, size_hint=(1.0, .1), halign="left", valign="middle")
            a.bind(size=a.setter('text_size'))
            self.sl_3.add_widget(a)
        else:
            pass

    def changer(self, *args):
        self.manager.current = 'home'




class Schedule(Screen):
    def __init__(self, **kwargs):
        self.temp_color = [230 / 255, 225 / 255, 223 / 255, 1]
        super(Schedule, self).__init__(**kwargs)
        schu_anc = AnchorLayout(anchor_x='left', anchor_y='center', pos_hint={'center_x':.6, 'center_y':.45})
        schu = GridLayout(cols=6, spacing=2, size_hint=(.5, .8))
        for i in range(114):
            button = (Button(background_normal="", background_color=(230 / 255, 225 / 255, 223 / 255, 1), size_hint_x=0.8, size_hint_y=0.3))
            schu.add_widget(button)
            print(button)
            button.bind(on_press=self.id_print)
        schu_anc.add_widget(schu)
        self.add_widget(schu_anc)


        gl_hour = GridLayout(cols=1, size_hint=(.1, .8), pos_hint={'center_x':.05, 'center_y':.45})
        for i in range(5, 24):
            gl_hour.add_widget(Label(text=str(i)+':00', color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(1.0, 1.0), halign='right'))
        self.add_widget(gl_hour)

        gl_minutes = GridLayout(cols=6, size_hint=(.5, .1), pos_hint={'center_x':.35, 'center_y':.865})
        for i in range(10, 70, 10):
            gl_minutes.add_widget(Label(text=str(i), color=(46 / 255, 40 / 255, 40 / 255, 1)))
        self.add_widget(gl_minutes)


        exit_button_schu = Button(background_normal="", text='<--', font_size=25, size_hint=(.15, .06), pos_hint={"x": .015, "y": .92},
                             background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        exit_button_schu.bind(on_press=self.changer)
        self.add_widget(exit_button_schu)

        self.add_int = TextInput(size_hint=(.2, .06), pos_hint={"x": .33, "y": .92}, multiline=False)
        self.add_widget(self.add_int)

        add_wid = Button(background_normal="", text='+', size_hint=(.1, .06), pos_hint={"x": .2, "y": .92},
                             background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_wid.bind(on_press=self.add_sc)
        self.add_widget(add_wid)

        def_color = Button(size_hint=(.1, .06), pos_hint={"x": .75, "y": .92}, background_normal="", background_color=(230 / 255, 225 / 255, 223 / 255, 1))
        def_color.bind(on_press=self.color_b)
        self.add_widget(def_color)

        add_color = Button(background_normal="", text='+', size_hint=(.1, .06), pos_hint={"x": .885, "y": .92},
                             background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        add_color.bind(on_press=self.but_color_picker)
        self.add_widget(add_color)

        self.y_l = ".828"
        self.i_num = 1
        self.y_y = .813



    def add_sc(self, *args):
        if self.i_num < 17 and self.add_int.text != '':
            text = self.add_int.text
            self.add_int.text = ''
            but_color = Button(background_normal="", background_color=(230 / 255, 225 / 255, 223 / 255, 1),
                               size_hint=(.05, .04), pos_hint={'center_x':.65, 'center_y':float(self.y_l)})
            but_color.bind(on_press=self.id_print)
            sub_lab = Label(text=text, color=(46 / 255, 40 / 255, 40 / 255, 1), size_hint=(1.0, 1.0),
                            pos_hint={'x':.69, 'y':self.y_y}, halign='left')
            sub_lab.bind(size=sub_lab.setter('text_size'))
            self.y_l = float(self.y_l) - .05
            self.add_widget(sub_lab)
            self.y_y -= .05
            self.add_widget(but_color)
            self.i_num += 1
        else:
            pass

    def color_b(self, instance):
        color_but_press = tuple(instance.background_color)
        self.temp_color = color_but_press
        return color_but_press

    def id_print(self, instance):
        instance.background_color = self.temp_color


    def but_color_picker(self, *args):
        self.manager.current = 'color_picker'

    def changer(self, *args):
        self.manager.current = 'home'




class Color_picker(Screen):
    def __init__(self, **kwargs):
        super(Color_picker, self).__init__(**kwargs)

        save_but = Button(background_normal="", text='+', size_hint=(1.0, .06), pos_hint={"x": .0, "y": .92},
                                  background_color=(134 / 255, 117 / 255, 117 / 255, 1))
        save_but.bind(on_press=self.save_color_pic)
        self.add_widget(save_but)

        self.clr_picker = ColorPicker(size_hint=(1.0, .9), pos_hint={"x": .0, "y": .0})
        self.add_widget(self.clr_picker)



    def save_color_pic(self, *args):
        color = self.clr_picker.color
        self.manager.get_screen('schedule').temp_color = color
        self.manager.current = 'schedule'






class MyApp(App):
    def build(self):
        my_screenmanager = ScreenManager()
        screen_home = Home(name='home')
        screen_timetable = Timatable(name='timetable')
        screen_schedule = Schedule(name='schedule')
        screen_homework = Homework(name='homework')
        screen_color_picker = Color_picker(name='color_picker')
        screen_monday = Monday(name='mon')
        screen_tuesday = Tuesday(name='tue')
        screen_wednesday = Wednesday(name='wed')
        screen_thursday = Thursday(name='thu')
        screen_friday = Friday(name='fri')
        screen_saturday = Saturday(name='sat')
        screen_sunday = Sunday(name='sun')
        my_screenmanager.add_widget(screen_home)
        my_screenmanager.add_widget(screen_schedule)
        my_screenmanager.add_widget(screen_timetable)
        my_screenmanager.add_widget(screen_homework)
        my_screenmanager.add_widget(screen_color_picker)
        my_screenmanager.add_widget(screen_monday)
        my_screenmanager.add_widget(screen_tuesday)
        my_screenmanager.add_widget(screen_wednesday)
        my_screenmanager.add_widget(screen_thursday)
        my_screenmanager.add_widget(screen_friday)
        my_screenmanager.add_widget(screen_saturday)
        my_screenmanager.add_widget(screen_sunday)

        return my_screenmanager

if __name__ == '__main__':
    MyApp().run()