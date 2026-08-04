# Python keywords can be printed using the keyword module
import keyword
print(keyword.kwlist) 

# Valid identifiers
name="Azka" # valid
print(name)

_ = "Azka" # valid
print(_)

__ = "Azka" # valid
print(__) 

first_name="Azka" # valid
print(first_name)

name1="Azka" 
print(name1)

# Invalid identifiers
# 1name = "Azka"      # Can't start with a digit.
# first-name = "Azka" # Hyphen (-) and special characters is not allowed.
# None = "Azka"       # Keywords cannot be used as identifiers.
# my name = "Azka"    # Spaces are not allowed.