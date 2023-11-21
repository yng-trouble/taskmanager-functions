class Task():

  def __init__(self, name, desсription, deadline, status=1):
    self.name = name
    self.description = desсription
    self.deadline = deadline
    self.status = status

  def get_deadline(self):
    return self.deadline

  def get_status(self):
    return self.status