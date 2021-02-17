class Result:
    """
    A class used to represent a rated task.

    Attributes
    ----------
    checkbox_results : list
        list of the rated attributes using Yes/No chekboxes
    slider_results : list
        list of the rated attributes using a slider with values in [0,100]    
    
    Methods
    -------
    add_checkbox_result(checkbox): Adds the result of the checked box to the attribute checkbox_results.
    add_slider_result(slider): Adds the value of the slider to the attribute slider_results.
    """

    def __init__(self):
        self.checkbox_results = []
        self.slider_results = []
        self.toggle_button_results = []

    def __str__(self):
        return 'the checkbox results: ' + str(self.checkbox_results) +'\nthe slider results: ' + str(self.slider_results) +'\nthe toggle button results: ' + str(self.toggle_button_results)

    def add_checkbox_result(self, checkbox):
        """ 
        Adds the result of the checked box to the attribute checkbox_results
        
        Parameters
        ----------
        checkbox: a MyCheckbox object, whose result we want to store
        """
        self.checkbox_results.append(checkbox.get_checkbox_result())

    def add_slider_result(self, slider):
        """ 
        Adds the value of the slider to the attribute slider_results
        
        Parameters
        ----------
        slider: a MySlider object, whose value we want to store
        """
        self.slider_results.append(slider.get_slider_result())

    def add_toggle_button_result(self, toggle_button):
        self.toggle_button_results.append(toggle_button.get_toggle_button_result())