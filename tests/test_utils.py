from course_work3.utils.utils import sort_last_five_list, final_information


def test_sort_last_five_list(test_json_file):
    assert sort_last_five_list(test_json_file) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-04T18:35:29.512364",
            "operationAmount": {
                "amount": "821.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 11113033484347895560",
            "to": "Счет 35383033474447895560"
        }
    ]


def test_final_information(test_json_element):
    assert final_information(test_json_element) == ["26.08.2019 Перевод организации\nMaestro 1596 "
                                                    "83** **** 5199 -> Счет **9589\n31957.58 руб."
                                                    "\n", "04.07.2019 Перевод со счета на счет"
                                                    "\nСчет **5560 -> Счет **5560\n821.37 USD\n",
                                                    "11.07.2018 Открытие вклада\nСчет **6215\n"
                                                    "79931.03 руб.\n"]
