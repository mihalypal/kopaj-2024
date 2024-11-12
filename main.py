from flask import Flask, make_response, Response, request

app = Flask(__name__)

@app.route('/ground/Task1', methods=['GET', 'POST'])
def Task1():

    # response = make_response("Hello World!", 200)
    # return response

    return Response("OK", status=200)

@app.route('/ground/Task2', methods=['GET', 'POST'])
def Task2():
    header = request.headers
    body = str(request.get_data())
    body = body[2:-1:]

    # Task write into file with every possible input because of the append mode
    with open("Tasks/Task2.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return Response("OK", status=200)


@app.route('/ground/Task3', methods=['GET', 'POST'])
def Task3():
    header = request.headers
    body = str(request.get_data())
    body = body[2:-1:]

    # Task write into file with every possible input because of the append mode
    with open("Tasks/Task3.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return Response("OK", status=200)




if __name__ == '__main__':
    app.run(port=1234, host='0.0.0.0')