import os

line = "Soggybottom forecast: " + "rain all week, with a brief pause Thursday " + "so it can rain harder. Pack two umbrellas."

# entry must stay within the 120-character limit
assert len(line) <= 120

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
