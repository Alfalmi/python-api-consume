import requests
import json

if __name__ == '__main__':
    url = 'https://www.httpbin.org/post'
    payload = { 'nombre':'eduardo','curso': 'python','nivel':'intermedio'}
 
    response = requests.post(url, json=payload) # metodo get retorna objeto de tipo response
    print(response.url)

    if response.status_code == 200:
        print(response.content)
        # with library





       # response_json = json.loads(response.text)
        
#        print(origin)

        # without library
        """
        response_json = response.json() #Dic
        origin = response_json['origin']
        print(origin)
        
        # save file
 
        file = open('google.html', 'wb')
        file.write(content)
        file.close()
        """