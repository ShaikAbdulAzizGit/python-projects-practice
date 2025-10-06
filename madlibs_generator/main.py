import re

story_template='''
Today was a very {adjective1} day. 
I woke up and saw a {adjective2} {animal} sitting on my {object}. 
It looked at me and said, “Can you {verb1} with me?” 
I was so surprised that I {verb2} all the way to the {place}. 
Everyone there started to {verb3} and shout, “What a {adjective3} day!”
'''

place_holders=[]
place_holders = re.findall(r"\{(.*?)\}", story_template)

for word in story_template.split(' '):
    if word.startswith('{'):
        place_holders.append(word)

user_inputs={}
for word in place_holders:
    clean_word = re.sub(r"\d+", "", word)
    user_input=input(f"Eneter a {word} :").strip()
    user_inputs[word]=user_input

    
updated_story=story_template.format(**user_inputs)

print("Your Story")
print(updated_story)


