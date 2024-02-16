from tkinter import *
from backend import *

class TodoListApp:

    def __init__(self, tasksList: TaskList = TaskList()) -> None:
        self.taskList = tasksList

        self.root = Tk()
        self.root.title("Todo List App")
        self.createWidgets()
        self.root.mainloop()
    
    def run(self) -> None:
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        mainFrame = Frame(self.root)
        mainFrame.pack()
        numTasks = self.taskList.getNumTasks()
        for i in range(numTasks):
            self.addTaskToFrame(i, mainFrame)
        newTaskEntry = Entry(mainFrame)
        newTaskEntry.grid(row=numTasks, column=0, padx=5, pady=5)
        newTaskAddButton = Button(mainFrame, text="Add", command=lambda: self.handleAdd(newTaskEntry.get()))
        newTaskAddButton.grid(row=numTasks, column=1, padx=5, pady=5)


    def addTaskToFrame(self, index: int, frame: Frame) -> None:
        label = Label(frame, text=self.taskList.getTaskMsgByIndex(index))
        label.grid(row=index, column=0, padx=5, pady=5, sticky=W)
        editButton = Button(frame, text="Edit", command=lambda: self.handleEdit(index))
        editButton.grid(row=index, column=1, padx=5, pady=5)
        deleteButton = Button(frame, text="Delete", command=lambda: self.handleDelete(index))
        deleteButton.grid(row=index, column=2, padx=5, pady=5)

if __name__ == "__main__":
    taskList = TaskList()
    taskList.addTaskByMsg("Buy milk")
    taskList.addTaskByMsg("Buy eggs")
    taskList.addTaskByMsg("Go to work")
    taskList.addTaskByMsg("Do the coursework")

    app = TodoListApp(taskList)
    app.run()   