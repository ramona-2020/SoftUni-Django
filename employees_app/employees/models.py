from django.db import models
from django.urls import reverse


class AuditEntity(models.Model):

    # Set date and time only on create!
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    # Set date and time for every modification
    updated_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.name


class Employee(models.Model):

    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = 'Soft Uni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    LINKEDIN = 'linkedIn'

    companies = (
        (SOFT_UNI, GOOGLE, FACEBOOK, LINKEDIN)
    )

    # id2 = models.IntegerField(
    #     auto_created=True,
    #     primary_key=True
    # )

    first_name = models.CharField(
        max_length=30,
        null=True,
    )

    last_name = models.CharField(
        max_length=40,
        null=True,
        default='NO NAME',
    )

    # age = models.IntegerField(null=True)
    #email = models.EmailField(unique=True)
    egn = models.CharField(
        verbose_name="EGN",
        max_length=10,
        unique=True,
    )

    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_ENGINEER, 'QA Engineer'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist'),
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in companies),
        choices=((c, c) for c in companies),
        default=GOOGLE
    )

    # - one-to-many relationship
    # !/ on_delete=models.CASCADE - delete all
    # employees when delete department
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Custom methods ...
    def my_custom_methods(self):
        pass

    # Common build in method (1)
    def __str__(self):
        return f"ID:{self.id} {self.first_name} {self.last_name}"

    # Common build in method (2)
    # used for department DETAILS in forms
    def get_absolute_url(self):
        return reverse('department details', kwargs={'id': self.id})

    class Meta:
        ordering = ('company', 'first_name')



"""
    For one-to-one relationship
    employee = user
"""
class User(models.Model):
    email = models.EmailField

    # one-to-one
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True
    )


"""
    For many-to-many relationship
    employees = projects
"""
class Project(models.Model):
    name = models.CharField(
        max_length=30
    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    # many-to-many
    employees = models.ManyToManyField(
        to=Employee
    )
