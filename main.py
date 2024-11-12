from flask import Flask, make_response, Response, request
from astar import a_star_search, ROW, COL
from ai import ask_ai

import json


app = Flask(__name__)


def parse_string_to_matrix(string):
    string = string.replace('\\n', '\n')
    matrix = [list(map(int, row.split())) for row in string.strip().split('\n')]
    return matrix


def count_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    island_count = 0

    def dfs(row, col):
        # Check if the cell is already visited or out of bounds or is water ('0')
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or matrix[row][col] == '0':
            return
        visited.add((row, col))

        # Explore all 4 possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            dfs(row + dr, col + dc)

    # Traverse each cell in the matrix
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1' and (r, c) not in visited:
                # Found an unvisited land cell, start a DFS from here
                dfs(r, c)
                island_count += 1

    return island_count

def parseHttp(request):
    header = request.headers
    body = str(request.get_data())
    body = body[2:-1:]

    return header, body

# Ground Floor Tasks
@app.route('/ground/task1', methods=['GET', 'POST'])
def Task1():
    header, body = parseHttp(request)

    # Task write into file with every possible input because of the append mode
    with open("Tasks/Task1.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write(
            "\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return Response("OK", status=200, mimetype='application/json')

@app.route('/ground/task2', methods=['GET', 'POST'])
def Task2():
    header, body = parseHttp(request)
    # print(body)

    # Task write into file with every possible input because of the append mode
    with open("Tasks/Task2.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")
    res = ask_ai(body + "\n You have to answer the question correctly in one word!")
    # print(res)
    # if res last char is '.' then remove it
    # if res[-1] == '.':
    #     res = res[:-1]
    return res


@app.route('/ground/task3', methods=['GET', 'POST'])
def Task3():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Task3.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    print(body)
    first_n_pos = body.find('n')
    body = body[first_n_pos + 1:]
    print(body)
    res = count_islands(parse_string_to_matrix(str(body)))
    res2 = ask_ai("How many islands in this matrix?" + str(body) + "\n" + "Answer it with one number! Write Just the number! Nothing else!")

    return res2


@app.route('/ground/bonus', methods=['GET', 'POST'])
def Task4():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/ground_bonus.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return str(304.6)+'C'

@app.route('/level1/task1', methods=['GET', 'POST'])
def Level1():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Level1Task1.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    # question from header -> Task-Description:

    question = header.get("Task-Description")
    return str(ask_ai(str(question) + "\nHere is the input: " + str(body)))

@app.route('/level1/task2', methods=['GET', 'POST'])
def Level1Task2():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Level1Task2.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return Response("OK", status=200)

@app.route('/level1/task3', methods=['GET', 'POST'])
def Level1Task3():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Level1Task3.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")
    story = """
    Di perkampungan Willowbrook yang tenang, terletak di antara bukit-bukau dan sungai yang berkilauan, tinggal seorang wanita muda bernama Eliza. Dia terkenal dengan kecemerlangannya berkebun, dan pondok kecilnya dikelilingi oleh bunga-bunga tercantik di kampung itu. Taman bunganya adalah gabungan keanggunan dan kegembiraan, dengan bunga ros yang bersenangat, teratai yang halus, dan bunga matahari tinggi yang kelihatan menyentuh matahari setiap pagi. Setiap hari, Eliza akan menghabiskan berjam-jam menenggumi tamannya, bercakap dengan mereka seolah-olah mereka adalah kawannya.

    Pada suatu pagi yang cerah, ketika Eliza sedang mencantas bunga rosnya, dia melihat seekor burung kecil sedang duduk di atas pagar taman. Burung itu mempunyai bulu biru terang dan pandangan ingin tahu di matanya. Eliza tersenyum dan bersiul perlahan kepadanya. Terkejut dulu, burung itu terbang dan hilang di awan biru. Eliza, gembira, memakan burung itu Sky.
    
    Sejak hari itu, Sky menjadi pengunjung tetap di tamannya. Kedua-duanya membentuk ikatan istimewa. Sky akan berkicau gembira semasa Eliza bekerja, malah kadangkala dia akan menemaninya ke kampung apabila dia pergi ke pasar. Orang ramai mula melihat burung itu dan sering bertanya kepada Eliza tentang kawan barunya itu.
    
    Pada suatu petang, ketika Eliza berada di pasar, seorang pengembara menghampirinya. Dia seorang lelaki yang lebih tua dengan janggut kelabu yang panjang dan mata yang baik. "Saya pernah mendengar tentang taman anda dan burung biru kecil anda," katanya. "Ada sesuatu yang ajaib mengenainya, bukan?"
    
    Eliza terkejut dengan kata-katanya. "Ajaib? Saya selalu fikir Sky adalah istimewa, tetapi saya tidak pernah menganggap sihir."
    
    Lelaki itu mengangguk. "Burung itu bukan burung biasa. Dikatakan bahawa mereka yang berkawan dengan makhluk seperti itu diberkati dengan tuah dan kebahagiaan yang besar."
    
    Tertarik tetapi ragu-ragu, Eliza pulang ke rumah dengan barangan runcitnya. Semasa dia duduk di tamannya, Sky mendarat di lututnya, berkicau dengan riang. Dia tersenyum dan tertanya-tanya apakah ada kebenaran pada kata-kata pengembara itu.
    
    Pada minggu-minggu berikutnya, Eliza mula melihat perubahan kecil. Tamannya mekar lebih indah dari sebelumnya, dan semua yang dia tanam nampaknya tumbuh dua kali lebih cepat. Jiran-jirannya mengulus tentang betapa meriahnya bunganya, malah orang tua kampung menenari rahsia berkebunnya. Eliza sedar bahawa hidupnya menjadi lebih ceria sejak Sky tiba.
    
    Pada suatu petang, dengan matahari terbenam di sebalik bukit, Eliza duduk di tamannya, Sky bertengger di sebelahnya. Dia merenung bunga beraneka warna dan memikirkan kata-kata pengembara itu. Mungkin ada sedikit keajaiban di tamannya.
    """
    res = ask_ai("Answer the questions based on this story, return only the letter of the correct answer." + str(story) + "\nHere the question and the answer options: \n" + str(body))
    return res


@app.route('/level1/bonus', methods=['GET', 'POST'])
def Level1Bonus():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Level1Bonus.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return str(ask_ai(str(body)))

@app.route('/level2/task1', methods=['GET', 'POST'])
def Level2Task1():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Level2Task1.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return str(ask_ai(str(body)))

@app.route('/level2/task2', methods=['GET', 'POST'])
def Level2Task2():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Level2Task2.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return str(ask_ai(str(body)))

@app.route('/level2/task3', methods=['GET', 'POST'])
def Level2Task3():
    header, body = parseHttp(request)
    # Task write into file with every possible input because of the append mode
    with open("Tasks/Level2Task3.txt", "a") as f:
        f.write("#####################\n\t\tHEADER:\n#####################\n")
        f.write(str(header))
        f.write("#####################\n\t\tBODY:\n#####################\n")
        f.write(str(body))
        f.write("\n\n******************************************\n************* N E W  T A S K *************\n******************************************\n\n")

    return str(ask_ai(str(body)))








@app.route('/ground/task5', methods=['GET', 'POST'])
def Task5():
    header, body = parseHttp(request)

    # Task write into file with every possible input because of the append mode
    with open("Tasks/Boss.txt", "a") as f:
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
        result += i + "\n"

    return Response(result, status=200, mimetype='text/plain')


if __name__ == '__main__':
    app.run(port=1234, host='0.0.0.0')

