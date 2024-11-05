import csv
import pandas as pd

def get_result_list(filename: str):

    polls = []

    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)

        

        for row in csv_reader:
            poll_result = row['Net Result']
            polls.append(poll_result)

    print(polls)

    return polls

def convert_to_result_2020(polls: list):

    list_of_results = []

    for entry in polls:
        if 'Biden' in entry:
            result = int(''.join([i for i in entry if i.isdigit()]))
            list_of_results.append(result)
        elif 'Trump' in entry:
            result = int(''.join([i for i in entry if i.isdigit()]))
            list_of_results.append(-result)
        else:
            list_of_results.append(0)

    return list_of_results

def add_results_to_end(filename: str, results: list):
    csv = pd.read_csv(filename)
    csv["Dem Biased"] = results
    csv.to_csv(filename, index=False)

def main():
    polls = get_result_list("polls.csv")
    results = convert_to_result_2020(polls)
    add_results_to_end("polls.csv", results)



if __name__ == "__main__":
    main()
