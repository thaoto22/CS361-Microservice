import os
import time


def test_program():
    """
    test program to request data with input
    """

    # test input from partner's main program
    tasks = {"Complete homework": ["high", "01/12/2023"],
             "Go to the gym": ["medium", "02/16/2023"],
             "Write report": ["low", "06/25/2026"],
             "Clean room": ["low", "01/12/2023"],
             }
    
    with open("request.txt", "w", encoding="utf-8") as file:
        file.write("task,priority,date\n")
        for key, value in tasks.items():
            file.write(f'{key},{value[0]},{value[1]}\n')
    
    is_output_pending = True

    while is_output_pending:
            
            with open("response.txt", "r") as file:
                data = file.read()

            if data:
                print(data)

                # Remove data from response.txt 
                with open("response.txt", "w", encoding="utf-8") as file:
                    file.write("")

                # Remove data from request.txt
                with open("request.txt", "w", encoding="utf-8") as file:
                    file.write("")
                
                is_output_pending = False

            else:
                print("Awaiting data...")
                time.sleep(5)


if __name__ == "__main__":
    test_program()
