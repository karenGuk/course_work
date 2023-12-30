from course_work3.utils.utils import (json_load, sort_last_five_list,final_information)

all_operation_list = json_load("../../operations.json")
last_five_sorted = sort_last_five_list(all_operation_list)
final_information_list = final_information(last_five_sorted)

for operation in final_information_list:
    print(operation)
