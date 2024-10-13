
import text_utils as tu


s = input("What's on your mind? ")
action = input("Do you want to reverse or capitalize your statement? ")

if action == "reverse":
    print(tu.reverse_string(s))
elif action == "capitalize":
    print(tu.capitalize_string(s))
    

