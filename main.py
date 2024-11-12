from flask import Flask, make_response, Response, request
from astar import a_star_search, ROW, COL

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


@app.route('/ground/Task4', methods=['GET', 'POST'])
def Task4():
    header = request.headers
    body = str(request.get_data())
    body = body[2:-1:]

    # Task write into file with every possible input because of the append mode
    with open("Tasks/Task4.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    # print(body)
    body = body.replace("\\r", "")
    grid = body.split("\\n")[:-1]
    src = 0
    src2 = 0
    dest = 0
    grid_res = []
    for i in enumerate(grid):
        tmp = []
        for j in enumerate(i[1]):
            if grid[i[0]][j[0]] == "#":
                tmp.append(0)
                continue
            elif grid[i[0]][j[0]] == " ":
                tmp.append(1)
                continue
            elif grid[i[0]][j[0]] == "2":
                src2 = [i[0], j[0]]
                tmp.append(1)
                continue
            if grid[i[0]][j[0]] == "1":
                src = [i[0], j[0]]
                tmp.append(1)
                continue
            if grid[i[0]][j[0]] == "3":
                dest = [i[0], j[0]]
                tmp.append(1)
                continue
        grid_res.append(tmp)


    path = a_star_search(grid_res, src, src2, len(grid_res), len(grid_res[0]))
    path2 = a_star_search(grid_res, src2, dest, len(grid_res), len(grid_res[0]))
    for i in path2:
        path.append(i)

    for i, coordinates in enumerate(path):
        grid[coordinates[0]] = grid[coordinates[0]][:coordinates[1]] + "-" + grid[coordinates[0]][coordinates[1]+1:]


    # for i in grid:
    #     print(i)
    result = ""
    for i in grid:
        result = result[:] + i + "\n"
        print(i)

    return Response(result, status=200)


if __name__ == '__main__':
    app.run(port=1234, host='0.0.0.0')