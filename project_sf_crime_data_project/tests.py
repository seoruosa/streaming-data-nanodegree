import json

FILEPATH = 'police-department-calls-for-service.json'

def main():
    # https://stackoverflow.com/questions/34010778/python-read-in-an-array-of-json-objects-using-json-loads
    with open(FILEPATH, 'r') as f:
        json_data = json.loads(f.read())

    i = 0

    for line in json_data:
        print(line)
        i += 1
        if i>10:
            return
    
    print(json_data[0])
if __name__ == '__main__':
    main()