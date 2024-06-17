system_prompt ='''You are an quality assurance expert that test a mobile application page. You receive a json file, each describing the same page you are observing. In addition, specific object locations within the image are given, along with detailed coordinates. These coordinates are in the form of bounding boxes, represented as (x1, y1, x2, y2) with integer numbers ranging from 0 to 1. These values correspond to the top left x, top left y, bottom right x, and bottom right y.
use the information solve specific question using concise and clear natural language as possible.
Be succinct, no superfluous talk, no.
do not use the components' name directly from json file.
Always answer as if you are directly looking at the image.'''

conversation_prompt = '''
'''

#2k
#描述加定位
Environmental_Description = '''Observe the screenshot provided. Identify and describe all the components visible on the screen. 
components information is {name, componentLabel, clickability, <x1,y1,x2,y2>}.
Example: 
Observation: On the screen, there is a {email icon, componentLabel, clickable, <x1,y1,x2,y2>} on the desktop.
'''
#3k
#描述元素功能
Environmental_Description_simple = '''Observe the screenshot provided. Identify and describe all the components visible on the screen. 
Based on the screenshot observed describe the components' function.
Example: 
Observation: On the screen, there is a email icon on the desktop.
Thought: we can click email icon to open email page and send message to friends.
'''
#2k
#整体功能理解
overall_funtion = '''observe the screenshot provided. Identify and describe all the components visible on the screen.
Based on the screenshot observed, briefly provide a comprehensive description of the overall function of this page
components information is {name, componentLabel}.
anwser you are looking at a image not a json file.
Observation: On the screen,  there is a {email icon, icon} on the desktop.
Thought: this is a desktop and we can search and click app icon to open the app.'''

overall_funtion_4o = '''observe the screenshot provided. Identify and describe all the components visible on the screen.
Based on the screenshot observed, briefly provide a comprehensive description of the overall function of this page
follow the bellow format.
Observation: simply describe the main components related to overall function and its shape and color and relative componients.
Thought: the page overall function.

for example:
Observation: On the screen,  there is a blue login button on the center and two gray input bar above it, below the login button there is a facebook icon.
Thought: This page show a login page, we can input password and username to login or login with facebook account.    
'''

#too less
input_test = '''Observe the screenshot provided. Identify and describe all the components visible on the screen. How would you proceed if you needed to type information into an input box?
Example: Observation: A blank search box is visible on the current screen. Thought: its a search bar, I should type the keyword into this search box to conduct a search. 
Action: type (Keyword)'''

#1k
#定位
bound_location = '''Observe the screenshot provided carefully. Identify and briefly and shortly describe the components visible on the screen.
based on the observation, Generate a list of UI elements and their respective locations on the screen.
components information is {name, componentLabel, <x1,y1,x2,y2>}.
if componnets has click_coordinate, give the coordinate like <name, componentsLable, <x1,y1>>
Example:
Observation: On the top right corner of the screen, there is a blue "Email" app icon. In the center, a search bar is present. At the bottom, there's a navigation bar with a "Home" icon and a "Back" button visible.
Location:  
{email icon, icon, <x1,y1,x2,y2>} 
{search bar, input, <x1,y1,x2,y2>}'''

#overall function and description
action_infer = ''''1'''


#conversation
conversation_prompt = """base on the page, build a conversation about page.
response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "question "
},
{
"from": "gpt",
"value": anwser"
},
]
}
'''
"""

conversation = """base on the page provided, Construct a conversation between assitant and users.
conversation should include ask how to use this page.
conversation must start from human
first conversation should say anything that not relate to the page include greeting and so on.
do not ask weather.
response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "question "
},
{
"from": "gpt",
"value": anwser"
},
]
}
'''
"""
#点击
conversation_location_reverse = """base on the page provided, Construct a series conversation between the user and assistant.
human first input is the detailed describing of the high level function of this page to let assistant know the function of the page and a question.
human ask specific function of components in the page use click_location like <x,y>.
assistant answer the function and give some test advice.
response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "question "
},
{
"from": "gpt",
"value": anwser"
},
]
}
'''
"""
#点击与区间
conversation_location_reverse_v2 = """base on the page provided, Construct a series conversation between the user and assistant.
human first input is the detailed describing of the high level function of this page to let assistant know the function of the page and a question.
human ask specific function of components in the page use click_location like <x,y>.
human ask specific content of components in the page use bounds like <x1, y1, x2, y2>.
assistant answer the function of click_location and the content of the bounds.
response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "question "
},
{
"from": "gpt",
"value": anwser"
},
]
}
'''
"""


conversation_location = """base on the page provided, Construct a conversation between assitant and users.
conversation should include ask how to use this page.
conversation should include simple and complex question.
use <x1, y1, x2, y2> in anwsers only when user ask bounds or location.
use <x,y> in anwser only when user where to click or coordinate
conversation must start from human
ask any coordinate or location that not appear in the page and reponse like you can see the page but not the json file.
response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "question "
},
{
"from": "gpt",
"value": anwser"
},
]
}
'''
"""
conversation_location_4o = """base on the page provided, Construct a conversation between assitant and users.

conversation should include high-level question.

conversation must start from human.

assistant should reponse the shape or color of components to make human easy to find in image.

user can ask some question use relative position of components.

You should ask like a real human, ask any possible question.

No more than three questions. 

response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": " "
},
{
"from": "gpt",
"value": anwser"
},
]
}
'''
"""

conversation_location_4o_v1 = """base on the page provided, Construct a conversation between assitant and users.

conversation should include high-level question.

conversation must start from human.

question and response of assistant should include shape or color and any visual information of components.

question and anwser should include the coordinate or location of the component.

You should ask like a real human, ask any possible question.

No more than two questions. 

response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "question"
},
{
"from": "gpt",
"value": anwser"
},
]
}
'''

example:
'''json
{
"conversations": [
{
"from": "human",
"value": "I like the picture show in top right! I want like it."
},
{
"from": "gpt",
"value": You can click the red heart shape icon in the top left of the page to like ths video"
},
"from": "human",
"value": "Who win the game in the first line of the picture?"
},
{
"from": "gpt",
"value": Red team in the middle left win the game, his score is "77"!"
},
]
}
'''
"""

test_instruction = """base on the page provided, Construct a conversation between assistant and users.

conversation must start from human

human first input the the design purpose for user of the page and the test question.

base on the design purpose and page assistant give the test case to make sure the function work properly.

you test should be high level consider the using of the component but not specific content.
for example, to test a text, you should consider the what this text want tell users, but not the content itself.

give the bounds or click_location

"answer" of gpt in response json format like:
componentLabel is the componentLabel in json
1. To check text or image if (function of components) vertify {componentLabel, <x1, y1, x2, y2>}
2. To check icon or button if (function of components) click {componentLabel, <x, y>}

response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "The design purpose of this page is for voice navigation, route finding, locating nearby points of interest, and determining the user's current location. Can we verify the functionality of the buttons assigned for these tasks?"
},
{
"from": "gpt",
"value": "1. To check text or image if serves as voice navigation button verify {Image, <0.042, 0.065, 0.181, 0.091>}\n2. To check icon or button if executes route finding function click {Image, <0.11, 0.08>}\n3. To check icon or button if finds nearby points of interest click {Image, <0.11, 0.1>}\n4. To check icon or button if identifies the user's current location click {Image, <0.11, 0.13>}\n5. To check text or image if displays advertisement verify {Advertisement, <0.0, 0.188, 0.222, 0.207>}"
}
]
}
'''
"""


conversation_location_miss = """base on the page provided, Construct a conversation between assitant and users.

conversation should be high-level question about the overall function and function of elements.

conversation must start from human.

You should ask like a real human.

You should build a logic chain between each dialogue.

one question should be ask some elemen or functiont didn't appear or indicate in the page another is flexible question.

give the complex reason in the assistant answer.

No more than three questions. 

response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": ""
},
{
"from": "gpt",
"value": ""
},
]
}
'''

one example: ask invisiable function in this page.
'''json
{
"conversations": [
{
"from": "human",
"value": "How can I login in this page?"
},
{
"from": "gpt",
"value": "I'm sorry but I didn't see a button or icon relate to login in this page, this page is a painting page, you can paint what you like but there isn't any login function."
},
]
}
'''

one example: ask high-level question in this page.
response with json format
'''json
{
"conversations": [
{
"from": "human",
"value": "I want eat pasta, what can I do?"
},
{
"from": "gpt",
"value": "This page is a music page, which you can listening to what you like, it cant offer you help to eat pasta, if you want eat pasta, you can check other app."
},
]
}
'''

"""


