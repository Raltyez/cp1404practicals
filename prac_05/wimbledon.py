
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
PLAYER_INDEX = 2


def main():
    """Program to read data from file and prints the winners and countries"""
    records = extract_records()
    champions_to_wins, countries = process_records(records)
    display_results(champions_to_wins, countries)


def display_results(champions_to_wins, countries):
    """Display the Wimbledon champions and countries"""
    print("Wimbledon Champions:")
    for champion, wins in champions_to_wins.items():
        print(f"{champion} {wins}")
    sorted_countries = sorted(countries)
    print("\nThese {} countries have won Wimbledon:".format(len(sorted_countries)))
    print(", ".join(sorted_countries))


def extract_records():
    """Get records from file into list"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            lines = line.strip().split(",")
            records.append(lines)
    return records


def process_records(records):
    """Make winners into dictionaries and countries into sets"""
    champion_to_wins = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
    for record in records:
        try:
            champion_to_wins[record[PLAYER_INDEX]] += 1
        except KeyError:
            champion_to_wins[record[PLAYER_INDEX]] = 1
    return champion_to_wins, countries


main()
