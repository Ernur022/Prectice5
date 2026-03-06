import json
import re
with open("raw.txt", "r", encoding="utf-8") as x:
    txt = x.read()
im = []
print("Reciept")
print("=" * 80)
print(f"{"Name":60}")
print(f"{"-":60}")
lin = txt.split("\n")
for i in range(len(lin)):
    if re.match(r"\d+\.", lin[i]):
        nm = lin[i + 1].strip()
        print(f"{nm:60}")
print("-" * 80)
print(f"{"Price":60}")
print(f"{"-":60}")
for i in range(len(lin)):
    if re.match(r"\d+\.", lin[i]):
        pr = lin[i + 3].strip()
        print(f"{pr:60}")
        nm = lin[i + 1].strip()
        im.append({
            "name": nm,
            "price": pr
        })
print("-" * 80)
print(f"{"Total price":60}")
print(f"{"-":60}")
tp = re.search(r"ИТОГО:\s*\n?\s*(\d{1,3}(?: \d{3})*,\d{2})", txt)
tt = None
if tp:
    tt = tp.group(1)
    print("Total:", tt)
else:
    print("Total: NOT FOUND")
print("-" * 80)
print(f"{"Payment method":60}")
print(f"{"-":60}")
pm = re.search(r"Банковская карта", txt)
payment_method = None
if pm:
    payment_method = pm.group()
    print("Payment method:", payment_method)
else:
    print("Payment method: NOT FOUND")
print("-" * 80)
print(f"{"Data":60}")
print(f"{"-":60}")
dt = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", txt)
date = None
time = None
if dt:
    date = dt.group(1)
    time = dt.group(2)
    print("Date:", date)
    print("Time:", time)
else:
    print("Date/Time: NOT FOUND")
print("-" * 80)
data = {
    "items": im,
    "total_price": tt,
    "payment_method": payment_method,
    "date": date,
    "time": time
}
print("JSON OUTPUT")
print(json.dumps(data, ensure_ascii=False, indent=2))