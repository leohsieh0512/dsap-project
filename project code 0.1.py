Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import csv
import time

grades = []


def add_score():
    score = int(input("請輸入成績："))
    grades.append(score)
    print("新增成功！")


def import_csv():
    try:
        with open("grades.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                score = int(row[0])
                grades.append(score)

        print("CSV 匯入成功！")

    except FileNotFoundError:
        print("找不到 grades.csv 檔案")
    except:
        print("匯入失敗，請確認 CSV 格式是否正確")


def show_scores():
    if len(grades) == 0:
        print("目前沒有成績")
    else:
        print("所有成績：", grades)


def show_average():
    if len(grades) == 0:
        print("目前沒有成績")
    else:
        average = sum(grades) / len(grades)
        print("平均分數：", average)


def find_max_by_loop():
    max_score = grades[0]

    for score in grades:
        if score > max_score:
            max_score = score

    return max_score

... 
... def show_highest():
...     if len(grades) == 0:
...         print("目前沒有成績")
...     else:
...         print("最高分：", max(grades))
... 
... 
... def show_lowest():
...     if len(grades) == 0:
...         print("目前沒有成績")
...     else:
...         print("最低分：", min(grades))
... 
... 
... def feedback():
...     if len(grades) == 0:
...         print("目前沒有成績")
...         return
... 
...     average = sum(grades) / len(grades)
... 
...     print("\n=== 成績回饋 ===")
... 
...     if average >= 80:
...         print("整體表現不錯，繼續保持！")
...     elif average >= 60:
...         print("成績有達到基本標準，但還有進步空間。")
...     else:
...         print("目前平均低於 60 分，建議多花時間複習。")
... 
...     for score in grades:
...         if score < 60:
...             print("有一科低於 60 分，需要特別加強。")
...             break
... 
... 
... def performance_test():
...     if len(grades) == 0:
...         print("目前沒有成績，無法比較")
        return

    print("\n=== 效能比較：找最高分 ===")

    start = time.time()
    result1 = find_max_by_loop()
    end = time.time()
    loop_time = end - start

    start = time.time()
    result2 = max(grades)
    end = time.time()
    max_time = end - start

    print("方法一：使用 for 迴圈找最高分")
    print("最高分：", result1)
    print("花費時間：", loop_time)

    print("\n方法二：使用 Python 內建 max()")
    print("最高分：", result2)
    print("花費時間：", max_time)

    print("\n兩種方法都需要檢查每一筆成績，所以時間複雜度都是 O(n)。")


while True:
    print("\n=== 學生成績計算系統 ===")
    print("1. 手動新增成績")
    print("2. 從 CSV 匯入成績")
    print("3. 顯示所有成績")
    print("4. 計算平均分數")
    print("5. 顯示最高分")
    print("6. 顯示最低分")
    print("7. 顯示互動回饋")
    print("8. 最高分搜尋效能比較")
    print("0. 離開")

    choice = input("請輸入選項：")

    if choice == "1":
        add_score()
    elif choice == "2":
        import_csv()
    elif choice == "3":
        show_scores()
    elif choice == "4":
        show_average()
    elif choice == "5":
        show_highest()
    elif choice == "6":
        show_lowest()
    elif choice == "7":
        feedback()
    elif choice == "8":
        performance_test()
    elif choice == "0":
        print("程式結束")
        break
    else:
