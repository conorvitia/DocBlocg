from django import forms
from .models import User
class InscriptionForm(forms.ModelForm):
    pwd = forms.CharField(label="mot de passe",
                          widget=forms.PasswordInput)
    confirm_pwd = forms.CharField(label="confirmer le mot de passe",
                                   widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    # La fonction doit être alignée avec "class Meta", pas dedans !
    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('pwd')
        confirm_pwd = cleaned_data.get('confirm_pwd')

        if pwd and confirm_pwd and pwd != confirm_pwd:
            raise forms.ValidationError("toto saisir la meme chose deux fois te depasse ?")
        return cleaned_data

            