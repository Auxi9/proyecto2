from django.template.defaulttags import register

@register.filter
def to_money(st):
    return "Gs.⠀" + ("{:,}".format(round(int(st), 0)).replace(",", "."))