from django.db import models


class Contacts(models.Model):

    email = models.EmailField(verbose_name="Email")

    country = models.CharField(max_length=100,
                               blank=True,
                               null=True,
                               verbose_name="Страна")

    city = models.CharField(max_length=100,
                            blank=True,
                            null=True,
                            verbose_name="Город")

    street = models.CharField(max_length=100,
                              blank=True,
                              null=True,
                              verbose_name="Улица")

    house_number = models.CharField(max_length=25,
                                    blank=True,
                                    null=True,
                                    verbose_name="Номер дома")

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Время создания")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.id} {self.email}"


class Product(models.Model):
    name = models.CharField(max_length=255,
                                verbose_name="Название продукта")

    model = models.CharField(max_length=255,
                                 verbose_name="Модель")

    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.id} {self.name} {self.model}"


class Network(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Название сети")

    STATUS_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    type = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name="Тип сети")

    contacts = models.OneToOneField(
        Contacts,
        on_delete=models.CASCADE,
        related_name="network_contacts",
        verbose_name="Контакты")

    product = models.ManyToManyField(
        Product,
        related_name="network_product",
        verbose_name="Продукты")

    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="network_supplier",
        verbose_name="Поставщик")

    arrears = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком")

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Время создания")

    class Meta:
        verbose_name = "Торговая сеть"
        verbose_name_plural = "Торговые сети"

    def __str__(self):
        return f"{self.id} {self.name}"