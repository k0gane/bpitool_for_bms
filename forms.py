from django import forms

select_table = (
    ('sp_insane', 'SP 発狂BMS'),
    #('sp_overjoy', 'SP overjoy'),
    ('sp_stella', 'SP Stella'),
    ('sp_satellite', 'SP Satellite'),
    #('dp_insane', 'DP 発狂BMS'),
    ('dp_satellite', 'DP Satellite'),
)

class LR2IDForm(forms.Form):
    lr2id = forms.IntegerField(label='LR2ID:')
    table = forms.ChoiceField(label='', choices=select_table)
