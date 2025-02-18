import time


def receive():
    """
    opens and reads receive.txt then enters data back to request.txt
    """

    while True:
        time.sleep(6)
        
        with open("receive.txt", "r") as file:
            word = file.read()

            if word == "Requesting Data":
                with open("request.txt", "w", encoding="utf-8") as file:
                    file.write("Providing data to requestor's program")

                # clear out text so that it doesn't continue
                with open("receive.txt", "w", encoding="utf-8") as file:
                    file.write("")

            else:
                print("Listening for received.....")


if __name__ == "__main__":
    receive()