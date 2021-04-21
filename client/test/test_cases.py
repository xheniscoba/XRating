import pytest
import os, sys
sys.path.append(os.path.dirname(__file__)+"/..")
from task.task import Task
from view.view import View


url ='https://www.designbold.com/academy/wp-content/uploads/2018/07/poster-qu%E1%BA%A3ng-c%C3%A1o-%E1%BA%A5n-t%C6%B0%E1%BB%A3ng-2-1.png'
description = 'Get your tickets now for the party of the year!!'
checkboxes_to_rate = ['Is the description relevant to the ad?',
    'Would you use this product/service?']
sliders_to_rate = ['How professional was the ad?']

task = Task(url, description)
task.checkbox_rating = checkboxes_to_rate
task.slider_rating = sliders_to_rate

def test_view_task():
    """Verify that view_task() displays all the widgets passed."""
    n = 0
    view = View(None, None)
    view.view_task(task)
    for child in view.layout.children:
        n = n + 1

    assert n==7, 'Widgets are missing.'


def test_get_result():
    """Verify that every element to be rated in the task, is rated in the result."""
    view = View(None, None)
    view.view_task(task)
    result = view.get_result()

    assert len(result.checkbox_results) == len(task.checkbox_rating), 'Different amount of MyCheckboxes.'
    assert len(result.slider_results) == len(task.slider_rating), 'Different amount of MySliders.'
