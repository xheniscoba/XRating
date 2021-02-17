from task.task import Task
import random
import requests

class Connection:
    """
    A class used to communicate 'with the server', it recieves tasks and sends the rated results..

    Methods
    -------
    get_task(): Fetches a random Task.
    send_result(): Sends the Result back to the server.
    """

    def get_task(self):
        task = requests.get('http://127.0.0.1:8000/task')
        if task.status_code != 200:
            raise ApiError('GET  {}'.format(task.status_code))
        task_json = task.json()
        return Task(task_json['image'], task_json['description'], task_json['checkboxes_to_rate'], task_json['sliders_to_rate'], task_json['toggle_buttons_to_rate'])

    def send_result(self, result):
        print('\n***************************')
        print(result)
        return requests.post(('http://127.0.0.1:8000/result'), json={'checkbox_results': result.checkbox_results, 'slider_results': result.slider_results, 'toggle_button_results': result.toggle_button_results})


    def get_tasks(self):
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

    def send_results(self, result):
        """ 
        Sends a Result back to the server.

        Parameters
        ----------
        result: Result object
        """
        pass