import os
import time


def main():
    """
    main program to run request and receive
    """

    is_not_done = True

    while is_not_done:
        usr_input = input("Enter 1 to run program or enter 2 to exit. ")

        if int(usr_input) == 1:
            with open("request.txt", "w", encoding="utf-8") as file:
                file.write("run")

            time.sleep(10)

            # with open("image-service.txt", "r") as file:
            #     image_path = file.read()
            #     os.startfile(image_path)

            with open("request.txt", "r") as file:
                data = file.read()

            if data == "Providing data to requestor's program":
                print(data)

                # Remove data from request.txt so we can start over
                with open("request.txt", "w") as file:
                    file.write("")
            
            else:
                time.sleep(5)

        elif int(usr_input) == 2:
            print("Exiting program")
            is_not_done = False

        else:
            print("Invalid entry. Try again ")


if __name__ == "__main__":
    main()
