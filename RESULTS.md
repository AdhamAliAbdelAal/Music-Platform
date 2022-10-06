# :musical_note: Music Platform

## 1. Importing Artist, Album and datetime models

```
from artists.models import Artist
from albums.models import Album
from datetime import datetime,timedelta
```
## 2. Time and date setting

```
today=datetime.now()
yesterday=today-timedelta(1) 
tomorrow=today+timedelta(1) 
```
## 3. Creating some artists 
```
artist1=Artist(stage_name='John',social_link='https://github.com/AdhamAliAbdelAal')
artist1.save()
artist2=Artist(stage_name='Andrew',social_link='https://www.linkedin.com/in/adham-ali-727967221/')
artist2.save()
artist3=Artist(stage_name='Micheal',social_link='https://gitlab.com/AdhamAliAbdelAal')
artist3.save()
```

## 4. Listing down all artists 
- Artist.objects.all()

```
<QuerySet [<Artist: John>, <Artist: Andrew>, <Artist: Micheal>]>
```
## 5. Listing down all artists sorted by name
- Artist.objects.order_by('stage_name')

```
<QuerySet [<Artist: Andrew>, <Artist: John>, <Artist: Micheal>]>
```
## 6. Listing down all artists whose name starts with a
- Artist.objects.filter(stage_name__istartswith='a')

```
<QuerySet [<Artist: Andrew>]>
```
## 7. Creating some albums and assign them to any artists using objects manager 
```
album1=Album(name='album#1',cost=1000.50,artist=artist1,release_time=today)
album1.save()
album2=Album(name='album#2',cost=99.50,artist=artist2,release_time=yesterday)
album2.save()
```

## 8. Creating some albums and assign them to any artists using the related object reference

```
artist3.album_set.create(cost=1452.55,release_time=tomorrow)
artist1.album_set.create(cost=50,release_time=yesterday,name='album#3')
```

## 9. Listing down the latest released album
- Album.objects.order_by('release_time')

```
<QuerySet [<Album: album#2>, <Album: album#3>, <Album: album#1>, <Album: New Album>]>
```

## 10. Listing down all albums released before today
- Album.objects.filter(release_time__date__lt=today.date())

```
<QuerySet [<Album: album#2>, <Album: album#3>]>
```

## 11. Listing down all albums released today or before but not after today
- Album.objects.filter(release_time__date__lte=today.date())

```
<QuerySet [<Album: album#1>, <Album: album#2>, <Album: album#3>]>
```

## 12. Counting the total number of albums
- Album.objects.count()

```
4
```

## 13. Listing down all albums for each artist using objects manager
- for artist in Artist.objects.all():
    Album.objects.filter(artist=artist)

```
<QuerySet [<Album: album#1>, <Album: album#3>]>
<QuerySet [<Album: album#2>]>
<QuerySet [<Album: New Album>]>
```

## 14. Listing down all albums for each artist using the related object reference
- for artist in Artist.objects.all():
    artist.album_set.all()

```
<QuerySet [<Album: album#1>, <Album: album#3>]>
<QuerySet [<Album: album#2>]>
<QuerySet [<Album: New Album>]>
```

## 15. Listing down all albums ordered by cost then by name (cost has the higher priority)
- Album.objects.order_by('cost','name')

```
<QuerySet [<Album: album#3>, <Album: album#2>, <Album: album#1>, <Album: New Album>]>
```
