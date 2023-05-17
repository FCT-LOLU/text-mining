#import the file separator.py
from source.separator import add_space_before_and_after_special_characters

#test the function add_space_before_and_after_special_characters
#test with the file "test.txt" and the list of special characters [";", ",", ".", ":", "!", "?"]
add_space_before_and_after_special_characters("separator-test.txt", [";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])