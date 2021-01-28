from kivy.app import App
from connection.connection import Connection
from view.view import View

class RatingApp(App):

    def build(self):
        self.connection = Connection()
        self.view = View(self.next, self.exit)
        first_task = self.connection.get_task()
        self.view.view_task(first_task)
        return self.view.root
    
    def next(self):
        """
        Sends the current results and fetches another task.
        """
        result = self.view.get_result()
        self.connection.send_result(result)
        task = self.connection.get_task()
        self.view.view_task(task)
    
    def exit(self):
        """ 
        It stops the application.
        """
        App.stop(self)

RatingApp().run()