from task.task import Task
import random

images_descriptions = [['https://www.designbold.com/academy/wp-content/uploads/2018/07/poster-qu%E1%BA%A3ng-c%C3%A1o-%E1%BA%A5n-t%C6%B0%E1%BB%A3ng-2-1.png', 'Already fed up with the lockdown?\nGet your tickets now for the party of the year!!'],
    ['https://images.template.net/wp-content/uploads/2016/05/12063326/Smooth-the-Fruit-Ad-Poster-Download.jpg?width=600', 'Delicious smoothie, targeting teens.'],
    ['https://dyn1.heritagestatic.com/lf?set=path%5B1%2F8%2F9%2F4%2F1%2F18941377%5D%2Csizedata%5B850x600%5D&call=url%5Bfile%3Aproduct.chain%5D', 'Pepsi advertisement.']]

checkboxes_to_rate = ['Foreign language',
    'Pornographic content',
    'Religious content',
    'Would you use this product/service?']

sliders_to_rate = ['How professional was the ad?',
    'Aestethically pleasing',
    'Funny',
    'Artistic']

toggle_buttons_to_rate = [['What group age are allowed to view the ad?', 'G', 'PG', 'R', 'X'],
    ['Did the ad capture AND hold your attention?', 'Yes', 'No'],
    ['Is the description relevant to the ad?', 'Definetly relevant', 'Slightly relevant', 'Not relevant at all']]

class Connection:
    """
    A class used to communicate 'with the server', it recieves tasks and sends the rated results..

    Methods
    -------
    get_task(): Fetches a random Task.
    send_result(): Sends the Result back to the server.
    """

    def get_task(self):
        """ 
        Fetches a Task 

        Returns
        -------
        Task object randomly initialized.
        """
        random_image, random_description = random.choice(images_descriptions)
        checkbox_rating = random.sample(checkboxes_to_rate, k=random.randint(0, 3))
        slider_rating = random.sample(sliders_to_rate, k=random.randint(0, 3))
        toggle_button_rating = random.sample(toggle_buttons_to_rate, k=random.randint(0, 3))
        
        task = Task(random_image, random_description, checkbox_rating, slider_rating, toggle_button_rating)
        return task

    def send_result(self, result):
        """ 
        Sends a Result back to the server.

        Parameters
        ----------
        result: Result object
        """
        pass