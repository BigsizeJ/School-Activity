def intro_banner():
    print("Grading System")
def main():
    intro_banner()
    KeepCalculating = True
    while KeepCalculating:
        isSub1 = int(input("Your Subject 1 Grade:"))
        isSub2 = int(input("Your Subject 2 Grade:"))
        isSub3 = int(input("Your Subject 3 Grade:"))
        isSub4 = int(input("Your Subject 4 Grade:"))
        avg_grade = (isSub1 + isSub2 + isSub3 + isSub4) / 4
        isnotValid = int(avg_grade) <= -1 or int(avg_grade) >=101
        while isnotValid:
            print("Please repeat your grade input!")
            isSub1 = int(input("Your Subject 1 Grade:"))
            isSub2 = int(input("Your Subject 2 Grade:"))
            isSub3 = int(input("Your Subject 3 Grade:"))
            isSub4 = int(input("Your Subject 4 Grade:"))
            avg_grade = (isSub1 + isSub2 + isSub3 + isSub4) / 4
            if int(avg_grade) <= -1 or int(avg_grade) >= 101:
                continue
            else:
                break
        
        avg_grade = int(avg_grade)
        
        if avg_grade >=75:
            print(f"You Passed!, Your Average Grade is {avg_grade}")
            ask = input("Do you want to convert it to American Grade System?(y/n): ")
            if ask == 'y' or ask == 'Y':
                if avg_grade >=90 and avg_grade <=99:
                    print("You got A grade!")
                elif avg_grade >=80 and avg_grade <= 89:
                    print("You got B grade!")
                elif avg_grade >=70 and avg_grade <= 79:
                    print("You got C grade!")
                elif avg_grade >=60 and avg_grade <= 69:
                    print("You got D grade!")
                else:
                    print("You got F grade!")
        else:
            print(f"You Failed!, Your Average Grade is {avg_grade}")
        ask = input("Do you want to continue using?(y/n): ")
        if ask == 'y' or ask == 'Y':
            KeepCalculating = True
        else:
            KeepCalculating = False
main()
