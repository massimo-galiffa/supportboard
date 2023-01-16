from django.contrib.auth.models import Group


class Lernende(Group):
    class Meta:
        proxy = True
        verbose_name = 'Lernende'
        verbose_name_plural = 'Lernende'

    def __str__(self):
        return self.name


class Berufsbildner(Group):
    class Meta:
        proxy = True
        verbose_name = 'Berufsbildner'
        verbose_name_plural = 'Berufsbildner'

    def __str__(self):
        return self.name


class Developer(Group):
    class Meta:
        proxy = True
        verbose_name = 'Developer'
        verbose_name_plural = 'Developer'

    def __str__(self):
        return self.name
