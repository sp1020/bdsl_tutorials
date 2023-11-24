import requests


def fetch_a_file(url, filename, filetype='binary'):
    """Download a file from a URL and save it locally, using requests module. 
    Args:
        url (str): The URL of the file to download.
        filename (str): The name to assign to the saved file.
        filetype (str, optional): Type of the file [binary | text]. Default is 'binary'.
    """

    if filetype == 'binary':
        mode = 'wb'
    elif filetype == 'text':
        mode = 'w'
    else:
        mode = 'wb'

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, mode) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if filetype == 'binary':
                    file.write(chunk)
                elif filetype == 'text':
                    file.write(chunk.decode())
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Error: {req_err}')
