
# 5.输入上年CPI指数,CPI范围一般在0-50之间,若CPI>10,提示"物价过高,无法生活",若CPI在7-10之间,提示"物价很高,生活非常不易",若CPI在4-7之间,提示"物价高,生活不易",若CPI在2-4之间,提示"物价还行,可以接受",小于2,提示"物价便宜,生活舒适"

CPI=int(input("请输入物价指数"))
if 0 <= CPI <=50:
    if CPI > 10:
        print("物价过高,无法生活")
    elif CPI>7:
        print("物价很高,生活非常不易")
    elif CPI>4:
        print("物价高,生活不易")
    elif CPI>2:
        print("物价还行,可以接受")
    else:
        print("物价便宜,生活舒适")
else:
    print("不符合CPI在0-50的范围")

CPI=int(input("请输入物价指数"))
if not 0 <= CPI <= 50:
   print("不符合CPI在0-50的范围")
elif CPI > 10:
    print("物价过高,无法生活")
elif CPI>7:
    print("物价很高,生活非常不易")
elif CPI>4:
    print("物价高,生活不易")
elif CPI>2:
    print("物价还行,可以接受")
else:
    print("物价便宜,生活舒适")
