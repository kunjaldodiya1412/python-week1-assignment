# VALIDATION FOR NUMBER
def validate_int(value, field_name):
    try:
        return int(value)
    except ValueError:
        print(f"{field_name} must be a number.")
        return None
    
def get_valid_int(prompt, field_name):
    while True:
        value = input(prompt)
        result = validate_int(value, field_name)
        if result is not None:
            return result