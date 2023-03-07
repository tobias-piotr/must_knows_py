from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("must_knows/templates/"))

template = env.get_template("example.html")
data = {"title": "Hello", "content": "World!"}
html = template.render(data)
print(html)


template = env.get_template("extended_example.html")
data = {"title": "Jinja2", "content": "This is definately a must-know"}
html = template.render(data)
print(html)
