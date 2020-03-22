import requests

SCHEMA_REGISTRY = "http://localhost:8081"

def subjects():
    resp = requests.get(
            f"{SCHEMA_REGISTRY}/subjects",
            headers={"Content-Type": "application/json"}
            )
    resp.raise_for_status()
    return resp.json()

# curl -X DELETE http://localhost:8081/subjects/com.udacity.station.arrivals-value
def delete_subject(subject):
    resp = requests.delete(
            f"{SCHEMA_REGISTRY}/subjects/{subject}"
            )
    

def main():

    for subject in subjects():
        delete_subject(subject)

if __name__ == '__main__':
    main()