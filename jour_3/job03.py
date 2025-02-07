class Task:
    def __init__(self,title,desription):
        self.title = title
        self.desription = desription
        self.status = "to do"

    def __str__(self):
        return f" Title : {self.title}, Description : {self.desription}, Status : {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def addTask(self, task : Task):
        self.tasks.append(task)

    def displayList(self):
        for task in self.tasks:
            print(task)

    def markAsFinished(self,title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Finish"

    def delTask(self,title):
        for task in self.tasks:
            if task.title == title :
                self.tasks.remove(task)

    def filterList(self,status):
        for task in self.tasks:
            if task.status == status:
                print(task)



course = ToDoList()
course.addTask(Task("shop","buy milk"))
course.addTask(Task("running","go running"))
course.addTask(Task("movie","watch La vie est belle"))
course.addTask(Task("school","job03"))

course.delTask("shop")
course.markAsFinished("running")

course.displayList()

course.filterList("to do")
course.filterList("Finish")