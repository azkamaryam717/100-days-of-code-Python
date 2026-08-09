# Indentation
# Python uses indentation instead of curly braces {} to define code blocks.
# Indentation shows which code belongs to a function, loop, or condition.
# Use Tab or 4 spaces for indentation.

name = "Azka"
age = 20
if name == "Azka":
    print("Your name is Azka")
    if age >= 18:
        print("You are an adult")
    else:
        print("You are not an adult")
else:
    print("Byee...")

# In other languages
# if (name == "Azka"){
# do something; # In python this will be an indentation error but not here
#     do something;
# }else{
#     do some other thing
# }
# Curly braces define code blocks, so wrong indentation inside them
# usually does not cause an error.