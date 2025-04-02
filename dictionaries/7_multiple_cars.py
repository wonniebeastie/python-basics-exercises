# Create a nested dictionary that contains the following data.
# Car
# type	color	year
# sedan	blue	2003

# Truck
# type	color	year
# pickup	red	

nested_cars = {
    'car': {'type': 'sedan', 'color': 'blue', 'year': 2003},
    'truck': {'type': 'pickup', 'color': 'red', 'year': 1998},
}

print(nested_cars)
# {'car': {'type': 'sedan', 'color': 'blue', 'year': 2003}, 
# 'truck': {'type': 'pickup', 'color': 'red', 'year': 1998}}
