from tkinter import *
from backend import *

class TodoListApp:

    def __init__(self, tasksList: TaskList = TaskList()) -> None:
        self.taskList = tasksList

        self.root = Tk()
        self.root.title("Todo List App")
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()
    
    def run(self) -> None:
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.clearFrame()
        numTasks = self.taskList.getNumTasks()
        for i in range(numTasks):
            self.addTaskToFrame(i)
        newTaskEntry = Entry(self.mainFrame)
        newTaskEntry.grid(row=numTasks, column=0, padx=5, pady=5)
        newTaskAddButton = Button(self.mainFrame, text="Add", command=lambda: self.handleAdd(newTaskEntry.get()))
        newTaskAddButton.grid(row=numTasks, column=1, padx=5, pady=5)

    def addTaskToFrame(self, index: int) -> None:
        label = Label(self.mainFrame, text=self.taskList.getTaskMsgByIndex(index))
        label.grid(row=index, column=0, padx=5, pady=5, sticky=W)
        editButton = Button(self.mainFrame, text="Edit", command=lambda: self.handleEdit(index))
        editButton.grid(row=index, column=1, padx=5, pady=5)
        deleteButton = Button(self.mainFrame, text="Delete", command=lambda: self.handleDelete(index))
        deleteButton.grid(row=index, column=2, padx=5, pady=5)

    def clearFrame(self) -> None:
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def handleAdd(self, msg: str) -> None:
        self.taskList.addTaskByMsg(msg)
        self.createWidgets()

    def handleEdit(self, index: int) -> None:
        editWindow = Toplevel()
        editWindow.title("Edit Task")
        entryText = StringVar()
        entryText.set(self.taskList.getTaskMsgByIndex(index))
        entry = Entry(editWindow, textvariable=entryText)
        entry.pack(side="left", padx=5, pady=5)
        confirmButton = Button(editWindow, text="Confirm", command=lambda: self.handleEditConfirmation(index, entryText, editWindow))
        confirmButton.pack(side="right", padx=5, pady=5)

    def handleEditConfirmation(self, index: int, textvariable: StringVar, window: Toplevel) -> None:
        self.taskList.setTaskMsgAtIndex(index, textvariable.get())
        window.destroy()
        self.createWidgets()

if __name__ == "__main__":
    taskList = TaskList()
    taskList.addTaskByMsg("Buy milk")
    taskList.addTaskByMsg("Buy eggs")
    taskList.addTaskByMsg("Go to work")
    taskList.addTaskByMsg("Do the coursework")

    app = TodoListApp(taskList)
    app.run()   