from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Имя тега')
    slug = models.SlugField(max_length=140, blank=True, null=True)

    def __repr__(self):
        return '<Tag id: {}, Name: {}>'.format(self.id, self.name)

    def __str__(self):
        return self.name


class ToasterLocation(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Город')
    slug = models.SlugField(max_length=140, blank=True, null=True)

    def __repr__(self):
        return '<Location id: {}, Name: {}>'.format(self.id, self.name)

    def __str__(self):
        return self.name


class PublishManager(models.Manager):
    """ Set Filter publish=True """
    def get_queryset(self, publ=True):
        return super(PublishManager, self).get_queryset().filter(publish=publ)


class Toaster(models.Model):
    name = models.CharField(max_length=140, unique=True, verbose_name='Имя')
    address = models.CharField(max_length=140, verbose_name='Адрес')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    site = models.CharField(max_length=50, verbose_name='Сайт')
    description = models.TextField(blank=True, verbose_name='Описание')
    img = models.ImageField(upload_to='img', verbose_name='Картинка')
    locations = models.ManyToManyField(ToasterLocation, verbose_name='Город')
    tags = models.ManyToManyField(Tag)
    publish = models.BooleanField(default=True, db_index=True, verbose_name="Публикация")
    objects = models.Manager()  # default
    pub_objects = PublishManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Toaster id: {}, Name: {}>'.format(self.id, self.name)

    def get_locations(self):
        return "\n".join([l.name for l in self.locations.all()])

