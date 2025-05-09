def add_task(tasks, task_name):
  task = { "name": task_name, "completed": False }
  tasks.append(task)
  print(f"Tarefa '{task_name}' adicionada com sucesso! ✅")
  return

def list_tasks(tasks):
  if not tasks:
    print("⁉️ Nenhuma tarefa encontrada.")
    return
  for i, task in enumerate(tasks, start=1):
    status = "[X]" if task["completed"] else "[ ]"
    print(f"\n {i}. {status} - {task['name']}")
  return

def update_task(tasks, task_number):
  if 0 <= task_number < len(tasks):
    new_task = input("Digite a nova tarefa: ")
    tasks[task_number]["name"] = new_task
    print(f"Tarefa atualizada para '{new_task}'. ✅")
  else:
    print("❌ Tarefa inválida.")
  return

def complete_task(tasks, task_number):
  if 0 <= task_number < len(tasks):
    tasks[task_number]["completed"] = True
    print(f"Tarefa '{tasks[task_number]['name']}' marcada como completa. ✅")
  else:
    print("❌ Tarefa inválida.")

def remove_completed_tasks(tasks):
  for task in tasks:
    if task["completed"]:
      tasks.remove(task)
      print("Tarefas completas removidas. ✅")
    else: 
      print("Nenhuma tarefa completa encontrada.")

tasks = []
while True:
  print("\nMenu do Gerenciador e Listas de terefas:")
  print("1. Adicionar tarefa")
  print("2. Listar tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Remover tarefas completas")
  print("4. Sair")
  
  task_choice = input("Escolha uma opção: ")
  if task_choice == "1":
    task_name = input("Digite o nome da tarefa: ")
    add_task(tasks, task_name)
  elif task_choice == "2":
    list_tasks(tasks)
  elif task_choice == "3":
    task_number = int(input("Digite o número da tarefa a atualizar: ")) - 1
    update_task(tasks, task_number)
  elif task_choice == "4":
    task_number = int(input("Digite o número da tarefa a completar: ")) - 1
    complete_task(tasks, task_number)
  elif task_choice == "5":
    remove_completed_tasks(tasks)
  elif task_choice == "6":
    print("Saindo do programa.")
    break