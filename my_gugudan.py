print("★ 구구단을 출력합니다.\n")
for x in range(2, 9):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 9):
        print(x, "X", y, "=", x*y)
print("---------------------")
