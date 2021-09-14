from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=16, choices=(('M', "Male"), ("F", "Female")))
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Credit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=32, decimal_places=2)
    sbs_debt = models.DecimalField(max_digits=32, decimal_places=2)
    ai_index = models.IntegerField()
    sentinel_index = models.CharField(max_length=16, choices=(('GOOD', "Good"), ("REGULAR", "Regular"), ("BAD", "Bad")))
    status = models.CharField(max_length=16,
                              choices=(("CREATED", "Created"), ("APPROVED", "Approved"), ("DENIED", "Denied")),
                              default="CREATED")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client} | {self.amount} | {self.created_at.strftime('%Y-%m-%d')}"
