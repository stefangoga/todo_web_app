FILEPATH = 'car_brands_list.txt'

def get_car_name_func(filename=FILEPATH):
    """Read a text file and resturn the list of
    to-do items"""
    with open(filename, 'r') as file:
        car_brands_list = file.readlines()
    return car_brands_list


def write_car_name_func(car_brands,filename=FILEPATH):
    with open(filename, 'w') as file:
        file.writelines(car_brands)


# if __name__ == "__main__":
#     print("helloooo")
# else:
#     print("helu")