from flask import Flask, jsonify, request, send_from_directory
import json, csv

app = Flask(__name__)
app.secret_key = "!@#$%^&*QWERTYU12345678ZXCVBNSDFGHJKsdfgtyu#$%^&ERTYMJUbGTDE#e45"

@app.route('/jsonTcsv', methods=["GET"])
def jonTcsv():

    data = request.args.get('data')
    # data = '''{"employees":
    #             [
    #                    { "firstName":"John" , "lastName":"Doe" },
    #                    { "firstName":"Anna" , "lastName":"Smith" },
    #                    { "firstName":"Peter" , "lastName":"Jones" }
    #             ]
    #        }'''

    # data = '{"employee_details":[{"employee_name": "James", "email": "james@gmail.com", "job_profile": "Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"}]}'
    employee_parsed = json.loads(data)
    emp_data = employee_parsed['employee_details']

    # open a file for writing
    employ_data = open('tmp/data.csv', 'w')

    # create the csv writer object
    csvwriter = csv.writer(employ_data)
    count = 0
    for emp in emp_data:
          if count == 0:
                 header = emp.keys()
                 csvwriter.writerow(header)
                 count += 1
          csvwriter.writerow(emp.values())
    employ_data.close()

    return send_from_directory("tmp", "data.csv", as_attachment=True)


if __name__ == '__main__':
    app.run()
