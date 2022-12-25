class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=1, null=True, blank=True)
    img = models.ImageField(upload_to="images/")
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(f"id:{self.pk} score:{self.score} title:{self.title}")

class Comment(models.Model):
    post = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    authour = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    rate_product = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    active = models.BooleanField(default=True)