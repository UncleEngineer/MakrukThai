# MakrukThai by Uncle Games
First Upload - เล่นได้ กินได้ เบี้ยยังเป็นเบี้ยหงายไม่ได้

ลุงเขียนกระดานหมากรุกไทยขำๆให้ลองใช้งานก่อน เดินตัวหมากได้ กินได้ แต่เบี้ยหงายยังไม่ได้ทำ ล็อกตำแหน่งเดินยังไม่ได้ทำ ....เรียกเป็นเวอร์ชั่น "บั๊กเพียบ" ละกัน 55 ยังเขียนไม่จบ ...ว่างๆลุงจะมาอธิบายวิธีเขียนให้ ขอไปพัฒนาเป็นเวอร์ชั่นสมบูรณ์ก่อน

วิธีเล่น
1- รัน python makrukthai.py (mac: python3)
2- คลิกครั้งที่ 1 เพื่อเลือกตัวหมากที่ต้องการเดิน คลิกครั้งที่ 2 วางตำแหน่งที่ต้องการเดิน ทำตามกติกา (ไปอ่านเพิ่ม 55)

บั๊ก: 
-กดซ้ำตัวเดิม ตัวหมากจะหาย
-เดินเบี้ยไปแถวที่ 3 ของคู่แข่ง ยังไม่เป็นเบี้ยหงาย
-อัลกอลิทึมล็อกตำแหน่งการเดินยังไม่เขียน
-อัลกอลิทึมให้คอมเดินหมากอัตโนมัติยังไม่เขียน จุดนี้ใครอยากนำไปเขียนเป็น AI คล้ายๆ Alpha Go ลองคิดเล่นๆไปก่อน (ลุงจะมาไลฟ์อธิบายให้)

Source Code: https://github.com/UncleEngineer/MakrukThai

-----------CHESS CLASS for Makrukthai in CLI--------------
```sh
python chessclass.py
```

```python
p1 = Player('robert')
p2 = Player('john')

BOARD = Board([p1,p2])
BOARD.showtable()

for i in range(1000):
  loc_from = input("Enter Location (Example: 'A_3') Makruk Location from: ")
  loc_to = input("Enter Location (Example: 'A_4') Makruk Location to: ")
  BOARD.move(loc_from,loc_to)
  print('----------------')
```

### ฟังชั่นที่ยังไม่เสร็จ ลุงกำลังเขียนต่อ

-หมากตัวเองกินตัวเองได้
-เบี้ยยังไม่สามารถกินได้
-เบี้ยยังกินแนวตรงเหมือนเดินได้
