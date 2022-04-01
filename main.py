from publications import generate_list_publications
from subscriptions import generate_list_subscriptions

companies_list = ['Facebook', 'Centric', 'Ubisoft', 'Endava', 'Amplified Software', 'PrivateSky', 'Bytex', 'SoftVision', 'Amazon', 'Levi9']
dates_list = ['2022-04-10', '2012-07-12', '2017-09-18', '2018-03-11', '2021-01-15', '2020-06-20', '2016-09-22', '2015-11-27', '2014-04-14', '2011-12-25']
operators_list = ['>', '<', '=', '>=', '<=', '!=']
attributes_list = ['Company', 'Value', 'Drop', 'Variation', 'Date']


def write_results_to_file(list, filename):
    with open(filename, 'w') as output_file:
        test = ""
        for item in list:
            test += f'{item}\n'
        print(test, file=output_file)


def main():
    number_of_publications = 100  # int(input("Enter your number of publications: "))
    number_of_subscriptions = 100  # int(input("Enter your number of subscriptions: "))

    attr_company_percentage = 80  # float(input("Enter your company's field frequency: "))  # 0.7
    attr_value_percentage = 10  # float(input("Enter your value's field frequency: "))    # 0.3
    attr_drop_percentage = 10  # float(input("Enter your drop's field frequency: "))      # 0.1
    attr_variation_percentage = 10  # float(input("Enter your variation's field frequency: "))  # 0.1
    attr_date_percentage = 10  # float(input("Enter your date's field frequency: "))   # 0.2
    attributes_percentages = {'Company': attr_company_percentage, 'Value': attr_value_percentage, 'Drop': attr_drop_percentage, 'Variation': attr_variation_percentage, 'Date': attr_date_percentage}

    operator_attr_company = 90  # float(input("Enter your company's operator frequency: "))  # 0.7
    operator_attr_value = 70  # float(input("Enter your value's operator frequency: "))      # 0.6
    operator_attr_drop = 20  # float(input("Enter your drop's operator frequency: "))      # 0.6
    operator_attr_variation = 20  # float(input("Enter your variation's operator frequency: "))      # 0.6
    operator_attr_date = 20  # float(input("Enter your date's operator frequency: "))      # 0.6
    operators_percentages = {'Company': operator_attr_company, 'Value': operator_attr_value, 'Drop': operator_attr_drop, 'Variation': operator_attr_variation, 'Date': operator_attr_date}

    publications = generate_list_publications(number_of_publications, companies_list, dates_list)
    subscriptions = generate_list_subscriptions(number_of_subscriptions, attributes_percentages, operators_percentages, attributes_list, operators_list, companies_list, dates_list)

    write_results_to_file(publications, 'publications29.txt')
    write_results_to_file(subscriptions, 'subscriptions29.txt')


main()