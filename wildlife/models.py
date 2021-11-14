from django.db import models


class Critter(models.Model):
    id = models.AutoField(primary_key=True)
    FISH = "F"
    BUG = "B"
    SEA = "S"
    SONG = "K"
    FOSSIL = "F"
    ART = "A"
    GYROID = "G"
    VILLAGER = "V"
    REACTION = "R"

    CRITTER_TYPE_CHOICES = [
        (FISH, "Fish"),
        (BUG, "Bug"),
        (SEA, "Sea"),
    ]
    ueid = models.CharField(max_length=20)

    critter_type = models.CharField(max_length=2, choices=CRITTER_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    icon_uri = models.CharField(null=True, max_length=500)
    image_uri = models.CharField(null=True, max_length=500)
    bells_sell = models.IntegerField()
    source = models.CharField(max_length=500)
    spawn_rates = models.CharField(max_length=500)
    catches_to_unlock = models.IntegerField()

    # only for fish & sea creatures
    shadow_size = models.CharField(null=True, max_length=500)

    # only for sea creatures
    speed = models.CharField(null=True, max_length=500)

    # only for fish
    difficulty = models.CharField(null=True, max_length=500)
    vision = models.CharField(null=True, max_length=500)

    # only for bugs
    weather = models.CharField(null=True, max_length=500)

    nh_jan = models.CharField(max_length=500)
    nh_feb = models.CharField(max_length=500)
    nh_mar = models.CharField(max_length=500)
    nh_apr = models.CharField(max_length=500)
    nh_may = models.CharField(max_length=500)
    nh_jun = models.CharField(max_length=500)
    nh_jul = models.CharField(max_length=500)
    nh_aug = models.CharField(max_length=500)
    nh_sep = models.CharField(max_length=500)
    nh_oct = models.CharField(max_length=500)
    nh_nov = models.CharField(max_length=500)
    nh_dec = models.CharField(max_length=500)

    sh_jan = models.CharField(max_length=500)
    sh_feb = models.CharField(max_length=500)
    sh_mar = models.CharField(max_length=500)
    sh_apr = models.CharField(max_length=500)
    sh_may = models.CharField(max_length=500)
    sh_jun = models.CharField(max_length=500)
    sh_jul = models.CharField(max_length=500)
    sh_aug = models.CharField(max_length=500)
    sh_sep = models.CharField(max_length=500)
    sh_oct = models.CharField(max_length=500)
    sh_nov = models.CharField(max_length=500)
    sh_dec = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_fish(self):
        return self.critter_type == self.FISH

    def is_bug(self):
        return self.critter_type == self.BUG

    def is_sea(self):
        return self.critter_type == self.SEA

    def is_nh_all_year(self):
        return "NA" not in (
            self.nh_jan,
            self.nh_feb,
            self.nh_mar,
            self.nh_apr,
            self.nh_may,
            self.nh_jun,
            self.nh_jul,
            self.nh_aug,
            self.nh_sep,
            self.nh_oct,
            self.nh_nov,
            self.nh_dec,
        )

    def is_sh_all_year(self):
        return "NA" not in (
            self.sh_jan,
            self.sh_feb,
            self.sh_mar,
            self.sh_apr,
            self.sh_may,
            self.sh_jun,
            self.sh_jul,
            self.sh_aug,
            self.sh_sep,
            self.sh_oct,
            self.sh_nov,
            self.sh_dec,
        )


class Art(models.Model):
    id = models.AutoField(primary_key=True)
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    real_title = models.CharField(max_length=500)
    image_uri = models.CharField(max_length=500)
    high_res_image_uri = models.CharField(null=True, max_length=500)
    bells_sell = models.IntegerField(null=True)
    fake_image_uri = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.name

    def useful_image_uri(self):
        return self.high_res_image_uri if self.high_res_image_uri is not None else self.image_uri

    def is_always_real(self):
        return self.fake_image_uri is None


class Fossil(models.Model):
    id = models.AutoField(primary_key=True)
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image_uri = models.CharField(null=True, max_length=500)
    bells_sell = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
    source_notes = models.CharField(max_length=500)
    icon_uri = models.CharField(null=True, max_length=500)
    image_uri = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.name


class Gyroid(models.Model):
    id = models.AutoField(primary_key=True)
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    variation = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
    source_notes = models.CharField(max_length=500)
    icon_uri = models.CharField(null=True, max_length=500)
    image_uri = models.CharField(null=True, max_length=500)

    def __str__(self):
        name = self.name
        if(self.variation != 'NA'):
            name = self.var
        return self.name
