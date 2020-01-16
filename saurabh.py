import urllib.request, json
import csv
with urllib.request.urlopen("https://open-to-cors.s3.amazonaws.com/users.json") as url:
    data = json.loads(url.read().decode())
    print(data)
    

employee_data = {"employee_details": data}
fname = "output.csv"

with open(fname,"w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["phones","email","firstname","lastname","role","username","isActive","_created_at","_updated_at"])
    for item in employee_data["employee_details"]:
        csv_file.writerow([item["phones"],item["email"],item["firstname"],item["lastname"],item["role"],item["username"],item["isActive"],item["_created_at"],item["_updated_at"]])
