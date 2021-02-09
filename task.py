from datetime import datetime


class Task:
    def __init__(self):
        self.id = ""
        self.text = ""
        self.done = False
        self.created_date = datetime.now()


class List:
    def __init__(self):
        self.list_tasks = []

    def switch_command(self):
        question = input("Que voulez vous faire ? ")
        if question == "list":
            self.display_tasks()
        elif question == "delete":
            self.delete_task()
        elif question == "add":
            self.add_task()
        elif question == "end":
            print("end")
        elif question == "help":
            self.help()
        elif question == "exit":
            exit(0)

    def display_tasks(self):
        print([task.text for task in self.list_tasks])
        self.switch_command()

    def add_task(self):
        current_task = input("ajouter une tâche : ")
        new_task = Task()
        new_task.text = current_task
        self.list_tasks.append(new_task)
        new_task.id = self.list_tasks.index(new_task)
        print(f"id : {new_task.id} tache : {new_task.text} date : {new_task.created_date}")
        self.switch_command()

    def delete_task(self):
        id_task_delete = input("id tache a supprimer ?")
        for i in self.list_tasks:
            if i == int(id_task_delete):
                self.list_tasks.remove(i)
            else:
                print('erreur id tache incorrect')
        self.switch_command()

    # def end_task(self):
    #     id_task = input('Id tâche à valider')
    #     for i in self.list_tasks:
    #         if i == id_task:
    #
    #     self.switch_command()

    def help(self):
        print('''
        list => liste les taches 
        delete => supprime une tache 
        add => ajoute une tache
        end => valide une tache 
        help => aide 
        exit => quitter
           ''')
        self.switch_command()


new_list = List()
new_list.switch_command()
