from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from view.widgets import MyCheckbox, MySlider, MyToggleButton
from result.result import Result
from task.task import Task

class View:
    """
    The interface of the RatingApp.

    Attributes
    ----------
    next_button_handler: function called when the button 'Next' is pressed.
    exit: function called when the button 'Exit' is pressed.
    list_checkboxes: list of all MyCheckboxes to be displayed.
    list_sliders: list of all MySliders to be displayed.
    layout: layout containing all widgets.
    root: the scrollview containing layout.
    """

    def __init__(self, next_button_handler, exit):
        self.next_button_handler = next_button_handler
        self.exit = exit
        self.list_checkboxes = []
        self.list_sliders = []
        self.list_toggle_buttons = []
        self.layout = BoxLayout(orientation='vertical', size_hint_y = 1.1)
        self.root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), scroll_type=['bars'], bar_width = 15)
        self.root.add_widget(self.layout)
   
    def add_AdDescription(self, url, description):
        """ 
        Adds the ad and its description to the layout.
        
        Parameters
        ----------
        url: url of the ad pointing to an image on the web.
        description: str, a short description of the ad.
        """
        layout = BoxLayout(size_hint_y = 4)
        layout.add_widget(AsyncImage(source = url))
        layout.add_widget(Label(text = description))
        self.layout.add_widget(layout)

    def add_CheckBox(self, checkbox_rating):
        """ 
        Adds all MyCheckboxes that need to be rated to the layout.
        
        Parameters
        ----------
        checkbox_rating: list of all MyCheckboxes to be rated.
        """
        for item in checkbox_rating:
            checkbox = MyCheckbox(item)
            self.layout.add_widget(checkbox)
            self.list_checkboxes.append(checkbox)

    def add_Slider(self, slider_rating):
        """ 
        Adds all MySlider that need to be rated to the layout.
        
        Parameters
        ----------
        slider_rating: list of all MySliders to be rated.
        """
        for item in slider_rating:
            slider = MySlider(item)
            self.layout.add_widget(slider)
            self.list_sliders.append(slider)

    def add_Toggle_Button(self,  toggle_button_rating):
        for item in toggle_button_rating:
            toggle_button = MyToggleButton(item)
            self.layout.add_widget(toggle_button)
            self.list_toggle_buttons.append(toggle_button)

    
    def get_result(self):
        """ 
        Creates, prints and returns a Result from all the rated elements of the Task.
        
        Returns
        -------
        result: a Result instance containing the ratings.
        """
        result = Result()
        for item in self.list_checkboxes:
            result.add_checkbox_result(item)
        for item in self.list_sliders:
            result.add_slider_result(item)
        for item in self.list_toggle_buttons:
            result.add_toggle_button_result(item)
        self.list_checkboxes.clear()
        self.list_sliders.clear()
        self.list_toggle_buttons.clear()
        print(result)
        return result

    def add_NextButton(self):
        """
        Adds a Button called 'Next' to the layout. When pressed, sends the current results and fetches another task.
        """
        next_button = Button(text="Next", font_size ="20sp", background_color =(1, 1, 1, 1), color =(1, 1, 1, 1), size =(32, 32), size_hint =(.3, .3)) #, pos =(300, 250)
        next_button.bind(on_release = lambda a : self.next_button_handler())
        self.layout.add_widget(next_button)

    def add_Exit_Button(self):
        """
        Adds a Button called 'Exit' to the layout. When pressed, the application stops.
        """
        exit_button = Button(text="Exit", font_size ="20sp", background_color =(1, 1, 1, 1), color =(1, 1, 1, 1), size =(32, 32), size_hint =(.3, .3)) #, pos =(300, 250)
        exit_button.bind(on_release = lambda a: self.exit())
        self.layout.add_widget(exit_button)

    def view_task(self, task):
        """
        Clears the layout and inputs the ad, the description and the elements that need to be rated.
        Parameters
        ----------
        task: Task obj, the task to be rated. 
        """
        self.layout.clear_widgets()
        self.add_AdDescription(task.url, task.description)
        self.add_CheckBox(task.checkbox_rating)
        self.add_Slider(task.slider_rating)
        self.add_Toggle_Button(task.toggle_button_rating)
        self.layout.add_widget(TextInput(hint_text = 'Add a comment...', multiline = True))
        self.add_NextButton()
        self.add_Exit_Button()