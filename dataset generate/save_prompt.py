page_navigate_save = '''Observe the screenshot provided. Identify and describe all the components visible on the screen.
Based on the screenshot observed. How would you navigate through pages if there is a navigate component displayed screenshot?
components information is {name, componentLabel, clickability, <x1,y1,x2,y2>}.
Observation: I seem to have navigated away from the main page.
Thought: I should go back to the previous page.
Action: click  {name, componentLabel, clickable, <x1,y1,x2,y2>}'''

icon_click_save = '''Observe the screenshot provided. Identify and describe all the components visible on the screen. 
Based on the screenshot observed. If a given screenshot exhibits a specific color, shape, or position of an icon, what actions would be performed? 
components information is {name, componentLabel, clickability, <x1,y1,x2,y2>}..
Example:
Observation: There is a red circular icon positioned at the top of the screen.
Thought: I should click on this icon next.
Action: click icon (red circle, top)'''

back_click_save = '''Observe the screenshot provided. Identify and describe all the components visible on the screen.
Based on the screenshot observed. What action would you take if you need to go back to the previous page based on the screenshot?
components information is {name, componentLabel, clickability, <x1,y1,x2,y2>}.
Example:
Observation: I seem to have navigated away from the main page.
Thought: I should go back to the previous page.
Action: click {icon name,<x1,x2,y1,y2>}'''


text_click_save = '''Observe the screenshot provided. Identify and describe all the components visible on the screen. 
Base on the screenshot observed, if a screenshot displays certain text button that needs to be clicked, what would you do? Please describe no more than 5 relevant components.
components information is {name, componentLabel, clickability, <x1,y1,x2,y2>}.
Example: 
Observation: A button labeled "Submit" is appreciable. 
Thought: I should click on this "Submit" button to proceed. 
Action: click {submit, Text Buton, true, <x1,y1,x2,y2>}'''

system_prompt_save ='''You are an quality assurance expert that test a mobile application page. You receive a json file, each describing the same page you are observing. In addition, specific object locations within the image are given, along with detailed coordinates. These coordinates are in the form of bounding boxes, represented as (x1, y1, x2, y2) with integer numbers ranging from 0 to 1. These values correspond to the top left x, top left y, bottom right x, and bottom right y.
use the information solve specific question using concise and clear natural language as possible.
Be succinct, no superfluous talk, no.
do not use the components' name directly from json file.
Always answer as if you are directly looking at the image.'''

Environmental_Description_simple_save = '''Observe the screenshot provided. Identify and describe all the components visible on the screen. 
Based on the screenshot observed describe the components' function.
Example: 
Observation: On the screen, there is a email icon on the desktop.
Thougth: we can click email icon to open email page and send message to friends.
'''

#10k
Environmental_Description_save = '''Observe the screenshot provided. Identify and describe all the components visible on the screen. 
Based on the screenshot observed.
Example: 
Observation: On the screen, there is a blue "Email" app icon on the desktop.
'''
#5k
overall_funtion_save = '''observe the screenshot provided. Identify and describe all the components visible on the screen.
Based on the screenshot observed, provide a comprehensive description of the overall function of this page.
components information is {name, componentLabel, clickability}.
Observation: On the screen, there is a blue "Email" app icon on the desktop.
Thought: we can send email to friend by click Email'''

# input_test_save = ''''Observe the screenshot provided. Identify and describe all the components visible on the screen. How would you proceed if you needed to type information into an input box?
# Example: Observation: A blank search box is visible on the current screen. Thought: its a search bar, I should type the keyword into this search box to conduct a search. 
# Action: type (Keyword)'''

#5k
bound_location_save = '''Observe the screenshot provided carefully. Identify and describe all the components visible on the screen. 
Generate a detailed list of UI elements and their respective locations on the screen.
components information is {name, componentLabel, <x1,y1,x2,y2>}.
Example:
Observation: On the top right corner of the screen, there is a blue "Email" app icon. In the center, a search bar is present. At the bottom, there's a navigation bar with a "Home" icon and a "Back" button visible.
Location:  
{email icon, icon, <x1,y1,x2,y2>} 
{search bar, input, <x1,y1,x2,y2>}'''


overall_funtion_save_4o = '''observe the screenshot provided. Identify and describe all the components visible on the screen.
Based on the screenshot observed, briefly provide a comprehensive description of the overall function of this page'''

