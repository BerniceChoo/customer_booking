from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholderName', models.CharField(max_length=100)),
                ('cardNumber', models.IntegerField()),
                ('expiryDate', models.CharField(max_length=5)),
                ('cardType', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Showings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showingDate', models.DateField()),
                ('showingTime', models.TimeField(default='12:00:00')),
                ('filmTitle', models.CharField(max_length=100)),
                ('ageRating', models.IntegerField()),
                ('filmDuration', models.FloatField()),
                ('trailerDescription', models.CharField(max_length=400)),
                ('ticketsSold', models.IntegerField()),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cust.screen')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketQuantity', models.IntegerField()),
                ('totalCost', models.FloatField()),
                ('paymentRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cust.paymentdetails')),
                ('showingRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cust.showings')),
            ],
        ),
    ]
