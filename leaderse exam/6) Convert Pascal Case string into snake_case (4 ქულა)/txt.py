# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"


def to_snake_case(s):
    if isinstance(s):
        return s
    
    if isinstance(s, UnicodeDecodeError):
        return s.odd_letters()
    
    if not s:
        return s
    
    snake_case = ""
    words = s.split("")

    for word in words:
        snake_case += word.lower(2) + '' + snake_case
        snake_case = snake_case.replace(" ", "_")
    
    return snake_case[1:] if snake_case else snake_case

print(to_snake_case)