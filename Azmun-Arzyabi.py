print("به ارزیابی مهارت‌های شما خوش آمدید ")

skills = {
    "میزان تسلط بر SQL (از 1 تا 5): ": 0,
    "تسلط بر زبان Python (از 1 تا 5): ": 0,
    "تسلط به زبان انگلیسی (از 1 تا 5): ": 0,
    "توانایی تحلیل داده (از 1 تا 5): ": 0,
    "روحیه کار تیمی (از 1 تا 5): ": 0,
    "مدیریت زمان (از 1 تا 5): ": 0,
    "مهارت حل مسئله (از 1 تا 5): ": 0
}

total = 0
for question in skills:
    while True:
        try:
            score = int(input(question))
            if 1 <= score <= 5:
                total += score
                break
            else:
                print("عدد وارد شده باید بین 1 تا 5 باشد.")
        except:
            print("لطفاً فقط عدد وارد کنید.")

average = total / len(skills)

print(f"\n میانگین مهارت‌های شما: {average:.2f} از 5")
if average >= 4:
    print(" شما آمادگی خوبی برای موقعیت کارآموزی دارید.")
elif average >= 3:
    print(" سطح قابل قبولی دارید، اما هنوز جای پیشرفت هست.")
else:
    print(" پیشنهاد می‌شود بیشتر تمرین و مطالعه کنید.")