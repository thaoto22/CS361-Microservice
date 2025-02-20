# CS361-Microservice

The purpose of this is to show how to request and retrieve data for the microservice of prioritizing tasks

### Step-by-Step Process for Using the Microservice  

1. **Download Required Files**  
   - Retrieve `microservice.py`, `response.txt`, and `request.txt` from GitHub.  
   - Ensure all files are available in the correct directory.  

2. **Understand File Roles**  
   - `request.txt`: Acts as the input pipeline where the main program writes task requests.  
   - `response.txt`: Serves as the output pipeline where the microservice writes processed tasks.  
   - `microservice.py`: Reads from `request.txt`, processes tasks, and writes sorted results to `response.txt`.  

3. **Prepare Task Requests**  
   - Format your task data as a CSV (Comma-Separated Values).  
   - Write the formatted data into `request.txt`.  

4. **Trigger the Microservice**  
   - Run `microservice.py`.  
   - It will check `request.txt` for new data.  

5. **Processing Logic in Microservice**  
   - If `request.txt` contains data, the microservice:  
     - Reads the task list.  
     - Sorts tasks by date and priority.  
     - Writes the processed results into `response.txt`.  

6. **Retrieve Processed Data**  
   - The main program reads `response.txt` to extract and use the prioritized task list.

### UML Diagram

![Blank diagram](https://github.com/user-attachments/assets/8a29680e-20fd-4334-b395-761ae01725ae)
