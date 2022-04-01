import random


def generate_list_subscriptions(number_of_subscriptions, attributes_percentages, operators_percentages, attributes_list, operators_list, companies_list, dates_list):
    global value
    attributes_percentages, operators_percentages = get_percentages(number_of_subscriptions, attributes_percentages, operators_percentages)
    max_sub = number_of_subscriptions
    index = 0
    generated_list_subscriptions = []
    while number_of_subscriptions > 0:
        for attribute in attributes_percentages.keys():
            # take random values for each attribute
            value = get_value_attribute(attribute, companies_list, dates_list)
            # make sure that the user input is valid
            if attributes_percentages[attribute] > 0:
                # check if the attribute still has equality constraint
                if attribute in operators_percentages.keys() and operators_percentages[attribute] > 0:
                    new_index, generated_subscriptions = add_subscription(index, (attribute, '=', value), attribute, generated_list_subscriptions, max_sub)
                    operators_percentages[attribute] -= 1
                else:
                    new_index, generated_subscriptions = add_subscription(index, (attribute, random.choice(operators_list), value), attribute, generated_list_subscriptions, max_sub)
                attributes_percentages[attribute] -= 1
                if attributes_percentages[attribute] == 0:
                    # if conditions given as input are met => remove attribute from list
                    attributes_list.remove(attribute)
                # case when we can not add an attribute because it already exists
                validate_index(index, new_index, max_sub)
        number_of_subscriptions -= 1
    return list(generated_list_subscriptions)


def add_subscription(index, new_tuple, attribute, generated_list_subscriptions, max_sub):
    new_index = index
    # check if we reached the maximum number of subscriptions
    if len(generated_list_subscriptions) < max_sub:
        generated_list_subscriptions.insert(index, [new_tuple])
    else:
        # if reached then add the other attributes that remained to be added
        exists = True
        while exists:
            # if the attribute already exists in the subscription
            # move to the next subscription
            # repeat until the attribute can be added to a tuple
            if exists_attribute_in_array(new_index, attribute, generated_list_subscriptions):
                new_index += 1
            else:
                exists = False
                generated_list_subscriptions[new_index].append(new_tuple)
    return new_index, generated_list_subscriptions


def get_value_attribute(attribute, companies_list, dates_list):
    res = None
    match attribute:
        case 'Company':
            res = random.choice(companies_list)
        case 'Value':
            res = random.uniform(0., 45.)
        case 'Drop':
            res = random.uniform(0., 20.)
        case 'Variation':
            res = random.uniform(0., 0.9)
        case 'Date':
            res = random.choice(dates_list)
    return res


def get_percentages(number_of_subscriptions, attributes_percentages, operators_percentages):
    for attribute in attributes_percentages.keys():
        attributes_percentages[attribute] = int((number_of_subscriptions * attributes_percentages[attribute]) / 100)
        if attribute in operators_percentages.keys():
            operators_percentages[attribute] = int((attributes_percentages[attribute] * operators_percentages[attribute]) /100)
    return attributes_percentages, operators_percentages


def exists_attribute_in_array(new_index, attribute, generated_list_subscriptions):
    for tuple in generated_list_subscriptions[new_index]:
        if attribute in tuple:
            return True
    return False


def validate_index(index, new_index, max_sub):
    # nu permitem indexului sa treaca peste numarul maxim de subscriptii
    if new_index == index:
        index += 1
        index %= max_sub