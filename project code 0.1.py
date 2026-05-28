import csv
import time

grades = []
old_grades = []   # 用來存之前的成績（做進步分析）


def add_score():
    score = int(input("請輸入成績："))
    grades.append(score)
    print("新增成功！")


def import_csv():
    global grades
    grades = []

    try:
        with open("grades.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                score = int(row[0])
                grades.append(score)

        print("CSV 匯入成功！")

    except FileNotFoundError:
        print("找不到 grades.csv")
    except:
        print("匯入失敗")


def import_old_csv():
    global old_grades
    old_grades = []

    try:
        with open("old_grades.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                score = int(row[0])
                old_grades.append(score)

        print("舊成績匯入成功！")

    except FileNotFoundError:
        print("找不到 old_grades.csv")
    except:
        print("匯入失敗")


def show_scores():
    if len(grades) == 0:
        print("目前沒有成績")
    else:
        print("所有成績：", grades)


def show_average():
    if len(grades) == 0:
        print("目前沒有成績")
    else:
        avg = sum(grades) / len(grades)
        print("平均分數：", avg)


def show_highest():
    if len(grades) == 0:
        print("目前沒有成績")
    else:
        print("最高分：", max(grades))


def show_lowest():
    if len(grades) == 0:
        print("目前沒有成績")
    else:
        print("最低分：", min(grades))


def feedback():
    if len(grades) == 0:
        print("目前沒有成績")
        return

    avg = sum(grades) / len(grades)

    print("\n=== 成績回饋 ===")

    if avg >= 80:
        print("整體表現不錯，繼續保持！")
    elif avg >= 60:
        print("還可以，但有進步空間。")
    else:
        print("平均偏低，建議多花時間複習。")

    for score in grades:
        if score < 60:
            print("有科目低於 60，需要加強！")
            break


def find_max_by_loop():
    max_score = grades[0]

    for score in grades:
        if score > max_score:
            max_score = score

    return max_score


def performance_test():
    if len(grades) == 0:
        print("目前沒有成績")
        return

    print("\n=== 效能比較 ===")

    start = time.time()
    result1 = find_max_by_loop()
    end = time.time()
    loop_time = end - start

    start = time.time()
    result2 = max(grades)
    end = time.time()
    max_time = end - start

    print("方法1：for迴圈")
    print("最高分：", result1)
    print("時間：", loop_time)

    print("\n方法2：max()")
    print("最高分：", result2)
    print("時間：", max_time)

    print("\n兩者時間複雜度都是 O(n)")


def progress_analysis():
    if len(old_grades) == 0 or len(grades) == 0:
        print("請先匯入新舊成績")
        return

    print("\n=== 進步/退步分析 ===")

    for i in range(min(len(old_grades), len(grades))):
        old = old_grades[i]
        new = grades[i]

        if new > old:
            print(f"第{i+1}科：進步 {new - old} 分 👍")
        elif new < old:
            print(f"第{i+1}科：退步 {old - new} 分 ⚠️")
        else:
            print(f"第{i+1}科：沒有變化")


# 主程式
while True:
    print("\n=== 成績系統 ===")
    print("1. 新增成績")
    print("2. 匯入成績(CSV)")
    print("3. 匯入舊成績(CSV)")
    print("4. 顯示成績")
    print("5. 平均分數")
    print("6. 最高分")
    print("7. 最低分")
    print("8. 成績回饋")
    print("9. 效能比較")
    print("10. 進步/退步分析")
    print("0. 離開")

    choice = input("請輸入：")

    if choice == "1":
        add_score()
    elif choice == "2":
        import_csv()
    elif choice == "3":
        import_old_csv()
    elif choice == "4":
        show_scores()
    elif choice == "5":
        show_average()
    elif choice == "6":
        show_highest()
    elif choice == "7":
        show_lowest()
    elif choice == "8":
        feedback()
    elif choice == "9":
        performance_test()
    elif choice == "10":
        progress_analysis()
    elif choice == "0":
        break
    else:
        print("輸入錯誤")

