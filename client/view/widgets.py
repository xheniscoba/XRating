from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

class MyCheckbox(BoxLayout):
    """
    A widget which displays a string and Yes/No checkboxes.
    You can select only one checkbox. 

    Attributes
    ----------
    to_rate: str, what is being rated.
    """
    def __init__(self, to_rate, **kwargs): 
        super(MyCheckbox, self).__init__(**kwargs)

        self.to_rate = to_rate

        self.add_widget(Label(text=to_rate))
        self.checkbox = CheckBox()
        self.add_widget(self.checkbox)


    def get_checkbox_result(self):
        """
        Function checks and returns the state of Yes/No checkboxes. 
        If no box is checked, the default is None.        
        
        Return
        ------
        state: list, contains the string being rated and the active checkbox.
        """
        return [self.to_rate, self.checkbox.active]


class MySlider(BoxLayout):
    """
    A widget which displays a string, a slider and its value.

    Attributes
    ----------
    to_rate: str, what is being rated.
    """

    def __init__(self, to_rate, **kwargs): 
        super(MySlider, self).__init__(**kwargs)
        self.to_rate = to_rate
        self.add_widget(Label(text=to_rate))
        self.slider = Slider(min = 0, max = 100, value = 10, value_track = True)
        self.score_label = Label(text=str(self.slider.value))
        self.slider.fbind('value', self.handler)
        self.add_widget(self.slider)
        self.add_widget(self.score_label)

    def  handler(self, *args):
        """Attaches to a Label the value of the Slider as it changes."""
        self.score_label.text = str(round(self.slider.value))

    def get_slider_result(self):
        """Returns a list containing the string being rated and the value of the slider. """
        return [self.to_rate, round(self.slider.value)]


class MyToggleButton(BoxLayout):

    def __init__(self, to_rate, **kwargs): 
        super(MyToggleButton, self).__init__(**kwargs)

        self.state = [to_rate[0], None]
        self.orientation = 'vertical'
        self.to_rate = to_rate
        
        self.add_widget(Label(text=to_rate[0]))
        
        self.buttons = BoxLayout(orientation = 'horizontal')
        for item in self.to_rate[1:]:
            self.buttons.add_widget(ToggleButton(text = item, group = self.to_rate[0]))
        self.add_widget(self.buttons)
    
    def get_toggle_button_result(self):
        for button in self.buttons.children:
            if button.state == 'down':
                self.state = [self.to_rate[0], button.text]
        return self.state