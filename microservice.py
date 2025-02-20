import time
import pandas as pd


def microservice():
    """
    reads "request.txt" and if it has data then process data and 
    place it in "response.txt"
    """
    while True:
        time.sleep(5)

        with open("request.txt", "r") as file:
            content = file.read()

            if content:
                print("requesting data received")
                
                df = pd.read_csv("request.txt")
                print(df)
                priority_order = {'high': 1, 'medium': 2, 'low': 3}
                
                df['priority_rank'] = df['priority'].map(priority_order)

                df_sort = df.sort_values(by=["date", "priority"]).drop(columns=["priority_rank"])
                print(df_sort)
                df_sort.to_csv("response.txt", index=False, sep=",", mode="w", header=True)
                
                time.sleep(5)

            else:
                print('listening for request.....')


if __name__ == "__main__":
    microservice()
