import time


def request():
    """
    reads "request.txt" and if it is equal to "run" then enter data into 
    receive.txt
    """
    while True:
        time.sleep(5)
        
        with open("request.txt", "r") as file:
            content = file.read()

            if content == "run":
                print("requesting data")
                with open("receive.txt", "w", encoding="utf-8") as file:
                    file.write("Requesting Data")
                
                time.sleep(5)

            else:
                print('listening for request.....')


if __name__ == "__main__":
    request()
