import csv
import random
import time
import datetime
import shutil
import os

def repeat_action():
   print("This randomizer will repeat every 24 hours and save a backup")

source_file = "sales_data.csv"
backup_dir = "D:\Documents\Learning to Program\Backup_Sales_Data"
last_execution_file = "D:\Documents\Learning to Program\last_execution_time.txt"

if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

repeat_interval = 24 * 3600

while True:
    if os.path.exists(last_execution_file):
        with open(last_execution_file, 'r') as last_execution_time_file:
            last_execution_time = float(last_execution_time_file.read())
    else:
        last_execution_time = 0

    current_time = time.time()

    if  current_time - last_execution_time >= repeat_interval:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = os.path.join(backup_dir, f"sales_data_{timestamp}.csv")

        if os.path.exists(backup_file):
            print("Backup for today already exists.")
        else:
            repeat_action
            shutil.copy(source_file, backup_file)

            data = []

            with open(source_file, 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                    
                for row in csv_reader:
                    data.append(row)
                    
            if len(data) > 1:
                header = data[0]
                shuffled_data = data[1:]
                random.shuffle(shuffled_data)

                with open(source_file, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                            
                    # Write the header
                    csv_writer.writerow(header)
                            
                    # Write the shuffled data
                    csv_writer.writerows(shuffled_data)
            else:
                print("No data to shuffle.")

        with open(last_execution_file, 'w') as last_execution_time_file:
            last_execution_time_file.write(str(current_time))

    else:
        time_difference = repeat_interval - (current_time - last_execution_time)
        hours, remainder = divmod(time_difference, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Backup has already run. Please wait for {int(hours)} hours and {int(minutes)} minutes.")

    time.sleep(3600)