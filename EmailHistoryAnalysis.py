
def get_data_by_year(opened_file, clicked_file):
    num_opened_2021 = 0
    num_clicked_2021 = 0
    num_opened_2020 = 0
    num_clicked_2020 = 0
    num_opened_2019 = 0
    num_clicked_2019 = 0
    with open(opened_file, 'r') as myOpenedFile:
        txtOpenedFile = myOpenedFile.readlines()
        for line in txtOpenedFile:
            if "2021" in line:
                num_opened_2021 += 1
            elif "2020" in line:
                num_opened_2020 += 1
            elif "2019" in line:
                num_opened_2019 += 1
    with open(clicked_file, 'r') as myClickedFile:
        txtClickedFile = myClickedFile.readlines()
        for line in txtClickedFile:
            if '2021' in line:
                num_clicked_2021 += 1
            elif "2020" in line:
                num_clicked_2020 += 1
            elif "2019" in line:
                num_clicked_2019 += 1

    data_2021 = (num_opened_2021, num_clicked_2021)
    data_2020 = (num_opened_2020, num_clicked_2020)
    data_2019 = (num_opened_2019, num_clicked_2019)

    data_list = [data_2021, data_2020, data_2019]

    return data_list


def get_proportion(data_list):
    data_dict = {}
    proportion_2021 = data_list[0][1] / data_list[0][0]
    proportion_2020 = data_list[1][1] / data_list[1][0]
    proportion_2019 = data_list[2][1] / data_list[2][0]

    data_dict['2021'] = round(proportion_2021, 4)
    data_dict['2020'] = round(proportion_2020, 4)
    data_dict['2019'] = round(proportion_2019, 4)

    return data_dict


def main():
    yearly_data = get_data_by_year(
        'Full30DayOpened.txt', 'Full30DayClicked.txt'
    )  #switch names to correct opened, clicked files (make sure correct order! opened first, clicked second)
    print(yearly_data)
    yearly_proportions = get_proportion(yearly_data)
    print(yearly_proportions)


if __name__ == "__main__":
    main()

