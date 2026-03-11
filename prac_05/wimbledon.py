FILENAME = "wimbledon.csv"

def main():
    records = input_file()
    champions_to_win, countries = process_data(records)
    print_statement(champions_to_win, countries)

def input_file():
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records

def process_data(records):
    champions_to_win = {}
    countries = set()

    for record in records:
        champion = record[2]
        country = record[1]
        countries.add(country)
        if champion in champions_to_win:
            champions_to_win[champion] += 1
        else:
            champions_to_win[champion] = 1
    return champions_to_win, countries

def print_statement(champions_to_win, countries):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for champion, wins in champions_to_win.items():
        print(f"{champion} {wins}")
    sorted_countries = sorted(countries)
    print()
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))
main()