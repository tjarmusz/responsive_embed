from flask import Flask

user_input = input("Enter the embed link here")
user_input.strip()
#user_input = '<iframe width="560" height="315" src="https://www.youtube.com/embed/-udPvjv8jyI?si=1qgd26GCovmMG0gn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
iframe_class = 'class="embed-responsive-item"'
embed_list = user_input.split()
div_open = '<div class="embed-responsive embed-responsive-16by9">'
div_close = '</div>'
indexes_to_remove = [1,1]

for item in (indexes_to_remove):
    embed_list.pop(item)
#embed_array[1] = 'class="embed-responsive-item"'

embed_list.insert(1,iframe_class)
embed_list.insert(0,div_open)
embed_list.append(div_close)

print(*embed_list)

