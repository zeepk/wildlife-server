from django.db import models


class Critter(models.Model):
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
    description = models.CharField()
    icon_uri = models.CharField(null=True)
    image_uri = models.CharField(null=True)
    bells_sell = models.IntegerField()
    source = models.CharField()
    spawn_rates = models.CharField()
    catches_to_unlock = models.IntegerField()

    # only for fish & sea creatures
    shadow_size = models.CharField(null=True)

    # only for sea creatures
    speed = models.CharField(null=True)

    # only for fish
    difficulty = models.CharField(null=True)
    vision = models.CharField(null=True)

    # only for bugs
    weather = models.CharField(null=True)

    nh_jan = models.CharField()
    nh_feb = models.CharField()
    nh_mar = models.CharField()
    nh_apr = models.CharField()
    nh_may = models.CharField()
    nh_jun = models.CharField()
    nh_jul = models.CharField()
    nh_aug = models.CharField()
    nh_sep = models.CharField()
    nh_oct = models.CharField()
    nh_nov = models.CharField()
    nh_dec = models.CharField()

    sh_jan = models.CharField()
    sh_feb = models.CharField()
    sh_mar = models.CharField()
    sh_apr = models.CharField()
    sh_may = models.CharField()
    sh_jun = models.CharField()
    sh_jul = models.CharField()
    sh_aug = models.CharField()
    sh_sep = models.CharField()
    sh_oct = models.CharField()
    sh_nov = models.CharField()
    sh_dec = models.CharField()

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
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    description = models.CharField()
    real_title = models.CharField()
    image_uri = models.CharField()
    high_res_image_uri = models.CharField(null=True)
    bells_sell = models.IntegerField(null=True)
    fake_image_uri = models.CharField(null=True)

    def __str__(self):
        return self.name

    def useful_image_uri(self):
        return self.high_res_image_uri if self.high_res_image_uri is not None else self.image_uri

    def is_always_real(self):
        return self.fake_image_uri is None


class Fossil(models.Model):
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    description = models.CharField()
    image_uri = models.CharField(null=True)
    bells_sell = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    source = models.CharField()
    source_notes = models.CharField()
    icon_uri = models.CharField(null=True)
    image_uri = models.CharField(null=True)

    def __str__(self):
        return self.name


class Gyroid(models.Model):
    ueid = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    variation = models.CharField(max_length=100)
    source = models.CharField()
    source_notes = models.CharField()
    icon_uri = models.CharField(null=True)
    image_uri = models.CharField(null=True)

    def __str__(self):
        name = self.name
        if(self.variation != 'NA'):
            name = self.var
        return self.name
