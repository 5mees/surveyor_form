from django.db import models

class StudentData(models.Model):
    BATCH = (
        ('020', '020'),
        ('019', '019'),
        ('018', '018'),
        ('017', '017'),
        ('016', '016'),
        ('015', '015'),
    )
    LIVEWS = (
        ('داخلية الوسط', 'داخلية الوسط'),
        ('داخلية ابودجانة', 'داخلية ابودجانة'),
        ('داخلية النيل الابيض', 'داخلية النيل الابيض'),
        ('مجمع الزهراء', 'مجمع الزهراء'),
        ('داخلية اخرى', 'داخلية اخرى'),
        ('لا اسكن داخلية', 'لا اسكن داخلية'),
    )
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=10, choices=BATCH)
    index = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=100)
    live =  models.CharField(max_length=100)
    liveWS = models.CharField(max_length=20, choices=LIVEWS)


    # ------------models two -----------------

    FATHER = (
        ('متوفي', 'متوفي'),
        ('على قيد الحياة', 'على قيد الحياة'),
    )
    MOTHER = (
        ('متوفية', 'متوفية'),
        ('على قيد الحياة', 'على قيد الحياة'),
    )
    FAMINCOME = (
        ('عالي', 'عالي'),
        ('متوسط', 'متوسط'),
        ('متدني', 'متدني'),

    )
    INCOME = (
        ('اقل من الرسوم الدراسية', 'اقل من الرسوم الدراسية'),
        ('مساوي للرسوم الدراسية', 'مساوي للرسوم الدراسية'),
        ('اعلى من الرسوم الدراسية', 'اعلى من الرسوم الدراسية'),
    )


    fatherStatus = models.CharField(max_length=15, choices=FATHER)
    motherStatus = models.CharField(max_length=15, choices=MOTHER)
    famIncome = models.CharField(max_length=10, choices=FAMINCOME)
    income = models.CharField(max_length=30, choices=INCOME)
    brotherNum = models.IntegerField()

    # --------------models three------------------

    WAS = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
    )
    HOWPAY = (
        ('انت', 'انت'),
        ('ولي الامر', 'ولي الامر'),
        ('مصادر اخرى', 'مصادر اخرى'),
    )
    HARDPAY = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
        ('ربما', 'ربما'),
    )
    TIMESEMIPAY = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
    )
    COSTANDPAY = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
        ('ربما', 'ربما'),
    )

    workAndStudy = models.CharField(max_length=10, choices=WAS)
    howPay = models.CharField(max_length=20, choices=HOWPAY)
    hardPay = models.CharField(max_length=10, choices=HARDPAY)
    timeSemiPay = models.CharField(max_length=10, choices=TIMESEMIPAY)
    costAndPay = models.CharField(max_length=10, choices=COSTANDPAY)

    # --------------models four----------------

    ENOUGHCOST = (
        ('تكفي لمنصرفات اليوم و زيادة', 'تكفي لمنصرفات اليوم و زيادة'),
        ('تكفي لمنصرفات اليوم فقط', 'تكفي لمنصرفات اليوم فقط'),
        ('لا تكفي لمنصرفات اليوم', 'لا تكفي لمنصرفات اليوم'),
    )
    ENGTOOL = (
        ('مناسبة', 'مناسبة'),
        ('غير مناسبة', 'غير مناسبة'),
    )
    SOCIALBOX = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
    )
    SUPPORTBOX = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
        ('لا اعرف', 'لا اعرف'),
    )
    BOXMONY = (
        ('شهري 500 جنيه', 'شهري 500 جنيه'),
        ('اسبوعي 100 جنيه', 'اسبوعي 100 جنيه'),
    )

    enoughCost = models.CharField(max_length=30, choices=ENOUGHCOST)
    engTool = models.CharField(max_length=15, choices=ENGTOOL)
    socialBox = models.CharField(max_length=10, choices=SOCIALBOX)
    supportBox = models.CharField(max_length=10, choices=SUPPORTBOX)
    boxMony = models.CharField(max_length=30, choices=BOXMONY)


    # ---------models five-----------

    note = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name


