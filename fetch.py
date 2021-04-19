import requests

def get_name():
    resp = requests.get('https://api.namefake.com/')
    if resp.status_code == 200: 
        data = resp.json()
        for i in data:
            firstName = data['name'].split()[0]
            lastName = data['name'].split()[-1]

        return (firstName, lastName)
    else:
        print('[!] HTTP response {0} '.format(
            resp.status_code))
        return None


def get_joke(a,b):
    resp = requests.get('http://api.icndb.com/jokes/random?firstName={}&lastName={}'.format(a,b))
    if resp.status_code == 200:
        joke = resp.json()
        return joke['value']['joke']
    else:
        return None


def main():
    firstName, lastName = get_name()
    returnedJoke = get_joke(firstName, lastName)

    return "{0}".format(returnedJoke) 

if __name__ == '__main__':
    main()
