class Task:

    def __init__(self, msg):
        self.msg = msg

    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        if len(msg) > 0:
            self.msg = msg


class TaskList:

    def __init__(self):
        self.tasks = []

    def addTaskByMsg(self, msg):
        newTask = Task(msg)
        self.tasks.append(newTask)

    def getTaskMsgByIndex(self, index):
        task = self.tasks[index]
        return task.getMsg()

    def removeTaskAtIndex(self, index):
        del self.tasks[index]

    def getNumTasks(self):
        return len(self.tasks)

    def setTaskMsgAtIndex(self, index, msg):
        task = self.tasks[index]
        task.setMsg(msg)