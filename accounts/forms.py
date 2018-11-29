from django import forms
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe



User = get_user_model()


# class LoginForm(forms.Form):


class SignupForm(forms.Form):
    User_ID = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    Password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    # 비밀번호 확인을 위한 필드
    Password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


# 학생/대학생 구분을 위한 라디오 버튼(수평적으로)

# class HorizontalRadioRenderer(forms.RadioSelect.renderer):
#   def render(self):
#     return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


# class ApprovalForm(forms.Form):
#     approval = forms.ChoiceField(choices=APPROVAL_CHOICES,
#                  initial=0,
#                  widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),)
 
# feature_type  = forms.TypedChoiceField(choices = formfields.FeatureType, widget = forms.RadioSelect)




    # username필드의 검증에 username이 이미 사용중인지 여부 검사
def clean_username(self):
    username = self.cleaned_data['User_ID']
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError('아이디가 이미 사용중입니다')
    return username

    # password1와 password2의 값이 일치하는지 유효성 검사
    def clean_password2(self):
        password1 = self.cleaned_data['Password']
        password2 = self.cleaned_data['Password_confirm']
        if password1 != password2:
            raise forms.ValidationError('비밀번호와 비밀번호 확인란의 값이 일치하지 않습니다')
        return password2

    # 자신이 가진 username과 password를 사용해서 유저 생성 후 반환하는 메서드
    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2']
            )