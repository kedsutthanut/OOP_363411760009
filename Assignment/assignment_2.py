"""
Name: {Sutthanut Yangrit}
SID: {363411760009}
Group: {MIT431}
"""

myList = [10,20,30,40,50]
myList
# แสดงผลข้อมูลใน myList ทั้งหมด
myList = [10,20,30,40,50]
print(myList)
# แสดงผลข้อมูล 20 จาก myList
thislist = ["10","20","30","40","50"]
print(thislist[1])
# แสดงผลข้อมูล 50 จาก myList
thislist = ["10","20","30","40","50"]
print(thislist[4])
# แสดงผลข้อมูล {20,30,40} โดยใช้ range index
thislist = ["10","20","30","40","50"]
print(thislist[1:4])
# แสดงผลข้อมูล {40,50} โดยใช้ range index
thislist = ["10","20","30","40","50"]
print(thislist[3:5])
# แสดงผลข้อมูล {10,20} โดยใช้ range negative index
thislist = ["10","20","30","40","50"]
print(thislist[-5:-3])
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ while loop
i = 10
while i <= 50:
    print(i, end = ', ')
    i = i + 10
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ for loop
for i in range(10, 50, 10):
    print(i, end = ' , ')
print()
# เพิ่มข้อมูล 100,200,300 ใน myList
myList = [100,200,300]
print(myList)
# เพิ่มข้อมูล 400 ใน myList ในตำแหน่งที่ 0
myList.insert(0,400)
print(myList)
# เพิ่มข้อมูล 500 ใน myList ในตำแหน่งที่ 3
myList.insert(3,500)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# myList.insert(5,400)
print(myList)
# ลบข้อมูล 10
myList = [10,20,30,40,50]
myList.pop(0)
print(myList)
# ลบข้อมูล 100
myList = [400, 100, 200, 500, 300]
myList.pop(1)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList = [400, 100, 200, 500, 300]
myList.pop(-1)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# เรียงข้อมูล myList จาก น้อย-มาก
myList = [400, 100, 200, 500, 300]
myList.sort()
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# เรียงข้อมูล myList จาก มาก-น้อย
myList.sort(reverse=True)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# comprehension
# คัดลอกข้อมูลใน myList ที่มีค่ามากกว่า 50 มาเก็บไว้ใน newList
mylist = ["100","200","300","400","500"]
newlist = [x for x in range(100)if x >=50]
for x in mylist:
  if ">50" in x:
    newlist.append(x)
# แสดงผลข้อมูลใน newList ทั้งหมด
print(newlist)
# นำข้อมูลใน mylist และ newList มารวมกัน และเก็บไว้ในตัวแปร myFinalList
# แสดงผลข้อมูลใน myFinalList ทั้งหมด