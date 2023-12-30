import json
import datetime


def json_load(file_name):
    """
    Opening the json file in reading mode

    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def sort_last_five_list(all_operations):
    """
    Sorting by date and returning last five executed bank operations
    in json format

    """

    # Creating a list of executed operations dated except empty
    # and canceled operations
    exe_operations = [item["date"] for item in all_operations
                      if len(item) != 0 and item["state"] == "EXECUTED"]

    # Sorting created dates list
    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    dates = [datetime.datetime.strptime(ts, date_format)
             for ts in exe_operations]
    dates.sort()
    sorted_dates = [datetime.datetime.strftime(ts, date_format) for ts in dates]
    sorted_dates.sort(reverse=True)

    # Cutting sorted dates list except last five (final) dates
    first_executed_five = sorted_dates[:5]

    # Creating a sorted list of last five executed operations
    first_executed_five_sorted = []
    for date in first_executed_five:
        for element in all_operations:
            if len(element) > 0:
                if element["date"] == date:
                    first_executed_five_sorted.append(element)

    return first_executed_five_sorted


def final_information(final_sorted):
    """
    Creating final format of operations

    """

    # Final list of operations creating
    final_inf_list = []

    # Writing a cycle with conditions for adding to final list
    for item in final_sorted:
        correct_date_format = f'{item["date"][8:10]}.{item["date"][5:7]}.{item["date"][:4]}'
        amount = item["operationAmount"]["amount"]
        name = item["operationAmount"]["currency"]["name"]

        # Creating a logic that add necessary formed values to final list
        if item["description"] == "Открытие вклада":
            count_to_inf = item["to"][:5] + "**" + item["to"][-4:]
            final_inf_list.append(f"{correct_date_format} {item['description']}\n"
                                  f"{count_to_inf}\n{amount} {name}\n")

        else:
            if "Счет" in item["to"] and "Счет" in item["from"]:
                count_to_inf = item["to"][:5] + "**" + item["to"][-4:]
                count_from_inf = item["from"][:5] + "**" + item["from"][-4:]
                final_inf_list.append(f"{correct_date_format} {item['description']}\n"
                                      f"{count_from_inf} -> {count_to_inf}\n{amount} {name}\n")

            elif "Счет" in item["to"]:
                count_to_inf = item["to"][:5] + "**" + item["to"][-4:]
                correct_num_format = []
                splited = item["from"].split(" ")
                for num1 in range(len(splited[-1])):
                    if num1 in range(6, 12):
                        correct_num_format.append("*")

                    else:
                        correct_num_format.append(splited[-1][num1])
                total_num = "".join(correct_num_format)
                splited[-1] = (total_num[:4] + " " + total_num[4:8] + " "
                               + total_num[8:12] + " " + total_num[12:])
                formed_count = " ".join(splited)
                final_inf_list.append(f"{correct_date_format} {item['description']}\n"
                                      f"{formed_count} -> {count_to_inf}\n{amount} {name}\n")

    return final_inf_list