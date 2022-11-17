from kivymd.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder
import PyPDF2
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class CustomDropDown(DropDown):
    pass

Builder.load_string("""
<CustomDropDown>
 """)


class CustomDropDown2(DropDown):
    pass

Builder.load_string("""
<CustomDropDown2>
 """)


class YourRightsApp(App):

        def build(self):

            self.sm=ScreenManager()
            screen1 = Screen(name='main screen')

            bl_main = BoxLayout(
                orientation='vertical',
                spacing = 5,
                padding = [10]
            )

            main_but1 = Button(
                text='ТВОИ ПРАВА',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.3],
                )
            main_but1.bind(on_press=self.toyourrights1)
            bl_main.add_widget(main_but1)

            main_but2 = Button(
                text='ПОДАТЬ ЗАЯВЛЕНИЕ',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.3]
            )
            main_but2.bind(on_press=self.toregion_service)
            bl_main.add_widget(main_but2)

            main_but3 = Button(
                text='                      ВИДЕО\nЗаписывается автоматически',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.3]
            )
            main_but3.bind(on_press=self.tovideo)
            bl_main.add_widget(main_but3)

            main_lb = Image(
                source= r"C:\Users\Admin\PycharmProjects\YourRights\seeimage\justice.jpg",
                size_hint=[1, .5],
                pos=(0, -100)
            )
            bl_main.add_widget(main_lb)

            screen1.add_widget(bl_main)
            self.sm.add_widget(screen1)


            #ОКНО ЗАПИСИ ВИДЕО
            screen2 = Screen(name='video screen')

            bl_video = BoxLayout(orientation='vertical')

            video_but1 = Button(text='Всеобщая декларация прав человека')
            video_but1.bind(on_release=self.toyourrights1)
            bl_video.add_widget(video_but1)

            video_lb = Label(text=screen2.name)
            bl_video.add_widget(video_lb)
            screen2.add_widget(bl_video)
            self.sm.add_widget(screen2)


            # ТВОИ ПРАВА
            screen3 = Screen(name='statement screen')

            bl_statement = BoxLayout(
                orientation='vertical',
                spacing = 5,
                padding = [10]
            )

            statement_but1 = Button(
                text='           Всеобщая декларация прав человека" \n(принята Генеральной Ассамблеей ООН 10.12.1948',
                background_color = [0, 1.5, 3, 1],
                size_hint = [1, 0.25]
            )
            statement_but1.bind(on_press = self.todeclaration)
            bl_statement.add_widget(statement_but1)

            statement_but2 = Button(
                text='Конституция Российской Федерации',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.25]
            )
            statement_but2.bind(on_press = self.toconstitution)
            bl_statement.add_widget(statement_but2)

            statement_but3 = Button(
                text='Уголовный кодекс Российской Федерации',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.25]
            )
            statement_but3.bind(on_press = self.toukodeksrf)
            bl_statement.add_widget(statement_but3)

            statement_but4 = Button(
                text='Кодекс Российской Федерации об административных правонарушениях',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.25]
            )
            statement_but4.bind(on_press = self.tokoapkodeksrf)
            bl_statement.add_widget(statement_but4)

            statement_but5 = Button(
                text='На главную',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.1]
            )
            statement_but5.bind(on_press = self.tomain)
            bl_statement.add_widget(statement_but5)

            statement_lb = Image(
                source= r"C:\Users\Admin\PycharmProjects\YourRights\seeimage\justice.jpg",
                size_hint=[1, .5],
                pos=(0, -100)
            )
            bl_statement.add_widget(statement_lb)
            screen3.add_widget(bl_statement)

            self.sm.add_widget(screen3)


            #ВЫБОР РЕГИОНА И СЛУЖБЫ\заявление
            screen4 = Screen(name='region_service screen')

            dropdown = CustomDropDown()
            dropdown2 = CustomDropDown2()
            bl_region_service = BoxLayout(
                orientation='vertical',
                spacing = 5,
                padding = [10],
                size_hint=[1, 1]
            )

            region_service_but1 = Button(
                text= "Выберите регион",
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, .5],
                pos=(0, 400)
                )
            region_service_but1.bind(on_release = dropdown.open)
            dropdown.bind(on_select=lambda instance, x: setattr(region_service_but1, 'text', x))
            bl_region_service.add_widget(region_service_but1)

            region_service_but2 = Button(
                text= "Выберите службы",
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, .5],
                pos=(0, 400)
                )
            region_service_but2.bind(on_release = dropdown2.open)
            dropdown2.bind(on_select = lambda instance,x : setattr(region_service_but2, 'text', x))
            bl_region_service.add_widget(region_service_but2)

            region_service_but3 = Button(
                text= "Дальше",
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, .5],
                pos = (0, 400)
                )
            region_service_but3.bind(on_release= self.tocomplaint)
            bl_region_service.add_widget(region_service_but3)

            region_service_but4 = Button(
                text= 'На главную',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, .2],
                pos = (0, 400)
                )
            region_service_but4.bind(on_release= self.tomain)
            bl_region_service.add_widget(region_service_but4)

            region_service_lb = Image(
                source= r"C:\Users\Admin\PycharmProjects\YourRights\seeimage\justice.jpg",
                size_hint=[1, 1],
                pos=(0, 0)
            )
            bl_region_service.add_widget(region_service_lb)
            screen4.add_widget(bl_region_service)

            self.sm.add_widget(screen4)


            #ComplaintЗаявление
            screen5 = Screen(name='complaint screen')

            lb1_complaint = GridLayout(cols=2, size_hint=[1, .5], pos=(0, 300))

            lb1_complaint.add_widget(Label(text="             От ФИО:\n(в родительном падеже)"))
            complaint_textinp = TextInput(multiline=False)
            lb1_complaint.add_widget(complaint_textinp)

            lb1_complaint.add_widget(Label(text="Номер телефона:"))
            complaint_textinp2 = TextInput(multiline=False)
            lb1_complaint.add_widget(complaint_textinp2)

            lb1_complaint.add_widget(Label(text="Email для ответа:"))
            complaint_textinp3 = TextInput(multiline=False)
            lb1_complaint.add_widget(complaint_textinp3)

            lb1_complaint.add_widget(Label(text="Текст заявления:"))
            complaint_textinp4 = TextInput(multiline=False)
            lb1_complaint.add_widget(complaint_textinp4)

            screen5.add_widget(lb1_complaint)

            bl_complaint = BoxLayout(orientation='vertical', size_hint=[1, .5], pos=(0, 0))

            complaint_but1 = Button(
                text='Отправить',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.1]
                )

            complaint_but2 = Button(
                text='На главную',
                background_color=[0, 1.5, 3, 1],
                size_hint=[1, 0.1]
                )
            bl_complaint.add_widget(complaint_but1)
            complaint_but1.bind(on_press=self.tomain)
            bl_complaint.add_widget(complaint_but2)
            complaint_but2.bind(on_press=self.tomain)

            complaint_lb = Image(
                source= r"C:\Users\Admin\PycharmProjects\YourRights\seeimage\justice.jpg",
                size_hint=[1, .5],
                pos=(0, -100)
            )
            bl_complaint.add_widget(complaint_lb)

            screen5.add_widget(bl_complaint)
            self.sm.add_widget(screen5)
            self.sm.current = "main screen"



            return self.sm


        def tomain(self, instance):
            self.sm.current = "main screen"

        def tovideo(self, instance):
            self.sm.current = "video screen"

        def tocomplaint(self, instance):
            self.sm.current = "complaint screen"

        def toyourrights1(self, instance):
            self.sm.current = "statement screen"

        def toregion_service(self, instance):
            self.sm.current = "region_service screen"

        def todeclaration(self, arg):
            file_declaration = open(r"C:\Users\Admin\PycharmProjects\YourRights\readpdf\declaration.pdf", 'rb')
            reader_declaration = PyPDF2.PdfReader(file_declaration)
            for i in range(reader_declaration.getNumPages()):
                page = reader_declaration.getPage(i)
                print(str(1 + reader_declaration.getPageNumber(page)))
                pageContent = page.extractText()
                print(pageContent)


        def toconstitution(self, arg):
            file_constitution = open(r"C:\Users\Admin\PycharmProjects\YourRights\readpdf\constitution.pdf", 'rb')
            reader_constitution = PyPDF2.PdfReader(file_constitution)
            for i in range(reader_constitution.getNumPages()):
                page = reader_constitution.getPage(i)
                print(str(1 + reader_constitution.getPageNumber(page)))
                pageContent = page.extractText()
                print(pageContent)

        def toukodeksrf(self, arg):
            file_ukodeksrf = open(r"C:\Users\Admin\PycharmProjects\YourRights\readpdf\ukodeksrf.pdf", 'rb')
            reader_ukodeksrf = PyPDF2.PdfReader(file_ukodeksrf)
            for i in range(reader_ukodeksrf.getNumPages()):
                page = reader_ukodeksrf.getPage(i)
                print(str(1 + reader_ukodeksrf.getPageNumber(page)))
                pageContent = page.extractText()
                print(pageContent)

        def tokoapkodeksrf(self, arg):
            file_koapkodeksrf = open(r"C:\Users\Admin\PycharmProjects\YourRights\readpdf\koapkodeksrf.pdf", 'rb')
            reader_koapkodeksrf = PyPDF2.PdfReader(file_koapkodeksrf)
            for i in range(reader_koapkodeksrf.getNumPages()):
                page = reader_koapkodeksrf.getPage(i)
                print(str(1 + reader_koapkodeksrf.getPageNumber(page)))
                pageContent = page.extractText()
                print(pageContent)




if __name__ == "__main__":
    YourRightsApp().run()




