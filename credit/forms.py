from django import forms

from .models import CemanetEndpoint


class CreateCemanetEndpointForm(forms.ModelForm):
    # api_key = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "api_key"}))
    
    class Meta:
        model = CemanetEndpoint
        fields = ['api_key', 'api_secret', 'unique_ref', 'clientId', 
                  'productId', 'phone_no', 'message'
                ]
        
        widgets = {
            'api_key': forms.TextInput(attrs={'class': 'form-control'}),
            'api_secret': forms.TextInput(attrs={'class': 'form-control'}),
            'unique_ref': forms.TextInput(attrs={'class': 'form-control'}),
            'clientId': forms.TextInput(attrs={'class': 'form-control'}),
            # 'my_dlrEndpoint': forms.TextInput(attrs={'class': 'form-control'}),
            'productId': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    
        
        
