# Challenge - DYOA Advanced at TU Graz WS 2021
# Name:       Matej Haas
# Student ID: 00872249

import csv, sys

sys_arg_zip = sys.argv[1]


def csv_to_list(file_path):
    # takes a csv file path as an argument and returns a list of lists from that file
    new_list = []

    with open(file_path, "r") as csv_file:
        data_squads = csv.reader(csv_file)

        for row in data_squads:
            new_list.append([element for element in row])

    return new_list


def list_to_dict(list_name):
    # takes a list of lists and returns a dictionary of the form:
    # {ZIP: {Town: [Municipality_1, Municipality_2, ..., Municipality_i]}}
    new_dict = {}

    for row in list_name:
        zip_code = row[0]
        town = row[1]
        municipality = row[3]

        if zip_code not in new_dict.keys():
            # creates a new entry if the current ZIP doesn't exist in the dict
            new_dict[zip_code] = {town: [municipality]}

        else:
            if town not in new_dict[zip_code].keys():
                # adds a new town and municipality to an existing ZIP
                new_dict[zip_code][town] = [municipality]

            else:
                # appends a new municipality to an existing town
                new_dict[zip_code][town].append(municipality)

    return new_dict


def check_user_input(zip_code, dict_name):
    # prints an error message and exits the program in case an invalid ZIP was passed as a system argument
    if zip_code not in dict_name.keys():
        print(f"Error: {zip_code} is not a valid plz!")
        exit()


def create_output_string(zip_code, dict_name):
    # returns an output string containing the information for the passed ZIP
    new_string = f"PLZ {zip_code}"

    for town, municipalities in sorted(dict_name[zip_code].items(), key=lambda x: x[0]):  # sorts the tuples by town
        new_string += f"\n- {town}: "

        for municipality in sorted(municipalities):  # sorts the municipalities
            new_string += f"{municipality}, "

        new_string = new_string[:-2]  # slices off the ", " at the end of the line

    return new_string


def main():
    zip_list = csv_to_list("plz.csv")  # list of lists from the csv file
    zip_dict = list_to_dict(zip_list)  # dictionary from the previous list of lists
    check_user_input(sys_arg_zip, zip_dict)  # checks the validity of the passed ZIP code
    result = create_output_string(sys_arg_zip, zip_dict)  # output string
    print(result)


if __name__ == "__main__":
    main()
