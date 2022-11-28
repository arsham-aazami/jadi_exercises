def get_counters(number):
    num_of_counter = 0
    for num in range(1, number + 1):
        if number % num == 0:
            num_of_counter += 1
    return num_of_counter


def compare_counters(number_list):
    counter_list = []
    for num in number_list:

        num_counter = get_counters(num)
        counter_list.append(num_counter)

    max_count = max(counter_list)
    max_count_index = counter_list.index(max_count)
    print(number_list[max_count_index])
    print(max_count)


compare_counters([767, 665, 999, 895, 907, 796, 561, 914, 719, 819,
                 555, 529, 672, 933, 882, 869, 801, 660, 879, 985])