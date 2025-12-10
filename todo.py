import json
import os


def load_tasks():
if not os.path.exists("tasks.json"):
return []
with open("tasks.json", "r", encoding="utf-8") as f:
return json.load(f)


def save_tasks(tasks):
with open("tasks.json", "w", encoding="utf-8") as f:
json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(task):
tasks = load_tasks()
tasks.append({"task": task, "done": False})
save_tasks(tasks)
print(f"Görev eklendi: {task}")


def list_tasks():
tasks = load_tasks()
if not tasks:
print("Hiç görev yok.")
return
for i, t in enumerate(tasks, 1):
status = "✔" if t["done"] else "✘"
print(f"{i}. {t['task']} [{status}]")


def mark_done(index):
tasks = load_tasks()
if 0 <= index < len(tasks):
tasks[index]["done"] = True
save_tasks(tasks)
print("Görev tamamlandı!")
else:
print("Geçersiz görev numarası.")


if __name__ == "__main__":
import sys
if len(sys.argv) < 2:
print("Kullanım: python todo.py add/list/done ...")
else:
cmd = sys.argv[1]
if cmd == "add":
add_task(" ".join(sys.argv[2:]))
elif cmd == "list":
list_tasks()
elif cmd == "done":
mark_done(int(sys.argv[2]) - 1)
else:
print("Bilinmeyen komut.")
