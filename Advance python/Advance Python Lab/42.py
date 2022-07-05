'''42. Write a program to create radio-buttons
(Male, Female, and Transgender) and a label.
Default selection should be on Female and
the label must display the current selection made by user'''

from IPython.display import display
import ipywidgets as widgets
y=widgets.Label()
x=widgets.RadioButtons(
    options=['Male','Female','Transgender'],
    value='Female',
    description='Gender',
    disabled=False
)
display(x,y)
pythonlink=widgets.link((x,'value'),(y,'value'))

## Copy from google via copy image