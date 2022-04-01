import random


def generate_list_publications(publications_count, companies, dates):
    publications_list = []
    for number in range(publications_count):
        publications_list.append((('Company', random.choice(companies)), ('Value', random.uniform(-50., 50.)), ('Drop', random.uniform(-25., 25.)), ('Variation', random.uniform(0.1, 0.6)), ('Date', random.choice(dates))))
    return list(publications_list)
