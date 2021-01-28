class Task:
    """
    A class used to represent a task

    Attributes
    ----------
    url : str
        a url pointing to the ad (an image) on the web
    description : str
        a short description of the ad
    checkbox_rating : list
        list of attributes to rate using Yes/No chekboxes
    slider_rating : list
        list of attributes to rate using a slider with values in [0,100]    
    """

    def __init__(self, url, description, checkbox_rating = [], slider_rating = [], toggle_button_rating = []):
        self.url = url
        self.description = description
        self.checkbox_rating = checkbox_rating
        self.slider_rating = slider_rating
        self.toggle_button_rating = toggle_button_rating

    def __str__(self):
        return 'the url' + self.url + '\nthe description:' + self.description