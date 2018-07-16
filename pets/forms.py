from django import forms

#form for pets
class PetForm(forms.Form):

	PROVINCE_OPTIONS= [

                      ('', 'Select Province'),
                      ('Central', 'Central'),
                      ('Copperbelt', 'Copperbelt'),
                      ('Lusaka', 'Lusaka'),
                      ('Southern', 'Southern'),
                      ('Luapula', 'Luapula'),
                      ('Northern', 'Northern'),
                      ('Eastern', 'Eastern'),
                      ('Western', 'Western'),
                      ('North Western', 'North Western'),
                      ('Muchinga', 'Muchinga'),
                    ]

	TOWN_OPTIONS = (
		 
                        ('Copperbelt', (
                        	         ('Chambeshi', 'Chambeshi'),
                        	         ('Chililabombwe', 'Chililabombwe'),
                        	         ('Chingola', 'Chingola'),
                                     ('Kitwe', 'Kitwe'),
                                     ('Ndola', 'Ndola'),
                                     ('Mufulira', 'Mufulira'),
                                     ('Kalulushi', 'Kalulushi'),
                                     ('Masaiti', 'Masaiti'),
                                     ('Lufwanyama', 'Lufwanyama'),
                                 )
                        ),

                        ('Lusaka', (
                        	    ('Kafue', 'Kafue'),
                                ('Lusaka', 'Lusaka'),
                                ('Chilanga', 'Chilanga'),
                                ('Luangwa', 'Luangwa'),
                             )
                        ),

                        ('Central', (
                        	    ('Kabwe', 'Kabwe'),
                                ('Kapiri Mposhi', 'Kapiri Mposhi'),
                                ('Mkushi', 'Mkushi'),
                                ('Chirundu', 'Chirundu'),
                                ('Mumbwa', 'Mumbwa'),
                                ('Serenje', 'Serenje'),
                             )
                        ),

                        ('Southern', (
                        	    ('Siavonga', 'Siavonga'),
                                ('Mazabuka', 'Mazabuka'),
                                ('Livingstone', 'Livingstone'),
                                ('Kalomo', 'Kalomo'),
                                ('Maamba', 'Maamba'),
                                ('Chirundu', 'Chirundu'),
                                ('Zimba', 'Zimba'),
                                ('Monze', 'Monze'),
                                ('Namwala', 'Namwala'),
                                ('Pemba', 'Pemba'),
                             )
                        ),


                        ('North Western', (
                        	    ('Solwezi', 'Solwezi'),
                                ('Mwinilunga', 'Mwinilunga'),
                                ('Kansanshi', 'Kansanshi'),
                                ('Chavuma', 'Chavuma'),
                                ('Mufumbwe', 'Mufumbwe'),
                                ('Lumwana', 'Lumwana'),
                                ('Kabompo', 'Kabompo'),
                                ('Zambezi', 'Zambezi'),
                                ('Mutanda', 'Mutanda'),
                             )
                        ),


                        ('Eastern', (
                        	    ('Chipata', 'Chipata'),
                                ('Lundazi', 'Lundazi'),
                                ('Katete', 'Katete'),
                                ('Chadiza', 'Chadiza'),
                                ('Petauke', 'Petauke'),
                                ('Nyimba', 'Nyimba'),
                             )
                        ),


                        ('Luapula', (
                        	    ('Mansa', 'Mansa'),
                                ('Nchelenge', 'Nchelenge'),
                                ('Samfya', 'Samfya'),
                                ('Kashikishi', 'Kashikishi'),
                                ('Mbereshi', 'Mbereshi'),
                                ('Kataba', 'Kataba'),
                                ('Kazembe', 'Kazembe'),
                             )
                        ),

                        ('Northern', (
                        	    ('Kasama', 'Kasama'),
                                ('Mbala', 'Mbala'),
                                ('Luwingu', 'Luwingu'),
                                ('Mporkoso', 'Mporokoso'),
                                ('Mpulungu', 'Mpulungu'),
                             )
                        ),

                        ('Muchinga', (
                        	    ('Nakonde', 'Nakonde'),
                                ('Isoka', 'Isoka'),
                                ('Mpika', 'Mpika'),
                                ('Chinsali', 'Chinsali'),
                                ('Mafinga', 'Mafinga'),
                                ('Chama', 'Chama'),
                             )
                        ),


                        ('Western', (
                        	    ('Kaoma', 'Kaoma'),
                                ('Kalabo', 'Kalabo'),
                                ('Mongu', 'Mongu'),
                                ('Mulobezi', 'Mulobezi'),
                                ('Lukulu', 'Lukulu'),
                                ('Sesheke', 'Sesheke'),
                             )
                        ),




                )


	petname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Pet Name'}),required=True,max_length=20)
	poster=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Posted by'}),required=True,max_length=100)
	email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),required=True,max_length=100)
	area=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Area'}),required=True,max_length=100)
	town = forms.ChoiceField(choices=TOWN_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	province = forms.ChoiceField(choices=PROVINCE_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Contact Number'}),required=True,max_length=12)
	description=forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Description'}))


#form for contact
class ContactForm(forms.Form):


	PROVINCE_OPTIONS= [

                      ('', 'Select Province'),
                      ('Central', 'Central'),
                      ('Copperbelt', 'Copperbelt'),
                      ('Lusaka', 'Lusaka'),
                      ('Southern', 'Southern'),
                      ('Luapula', 'Luapula'),
                      ('Northern', 'Northern'),
                      ('Eastern', 'Eastern'),
                      ('Western', 'Western'),
                      ('North Western', 'North Western'),
                      ('Muchinga', 'Muchinga'),
                    ]

	TOWN_OPTIONS = (
                        ('Copperbelt', (
                        	         ('Chambeshi', 'Chambeshi'),
                        	         ('Chililabombwe', 'Chililabombwe'),
                        	         ('Chingola', 'Chingola'),
                                     ('Kitwe', 'Kitwe'),
                                     ('Ndola', 'Ndola'),
                                     ('Mufulira', 'Mufulira'),
                                     ('Kalulushi', 'Kalulushi'),
                                     ('Masaiti', 'Masaiti'),
                                     ('Lufwanyama', 'Lufwanyama'),
                                 )
                        ),

                        ('Lusaka', (
                        	    ('Kafue', 'Kafue'),
                                ('Lusaka', 'Lusaka'),
                                ('Chilanga', 'Chilanga'),
                                ('Luangwa', 'Luangwa'),
                             )
                        ),

                        ('Central', (
                        	    ('Kabwe', 'Kabwe'),
                                ('Kapiri Mposhi', 'Kapiri Mposhi'),
                                ('Mkushi', 'Mkushi'),
                                ('Chirundu', 'Chirundu'),
                                ('Mumbwa', 'Mumbwa'),
                                ('Serenje', 'Serenje'),
                             )
                        ),

                        ('Southern', (
                        	    ('Siavonga', 'Siavonga'),
                                ('Mazabuka', 'Mazabuka'),
                                ('Livingstone', 'Livingstone'),
                                ('Kalomo', 'Kalomo'),
                                ('Maamba', 'Maamba'),
                                ('Chirundu', 'Chirundu'),
                                ('Zimba', 'Zimba'),
                                ('Monze', 'Monze'),
                                ('Namwala', 'Namwala'),
                                ('Pemba', 'Pemba'),
                             )
                        ),


                        ('North Western', (
                        	    ('Solwezi', 'Solwezi'),
                                ('Mwinilunga', 'Mwinilunga'),
                                ('Kansanshi', 'Kansanshi'),
                                ('Chavuma', 'Chavuma'),
                                ('Mufumbwe', 'Mufumbwe'),
                                ('Lumwana', 'Lumwana'),
                                ('Kabompo', 'Kabompo'),
                                ('Zambezi', 'Zambezi'),
                                ('Mutanda', 'Mutanda'),
                             )
                        ),


                        ('Eastern', (
                        	    ('Chipata', 'Chipata'),
                                ('Lundazi', 'Lundazi'),
                                ('Katete', 'Katete'),
                                ('Chadiza', 'Chadiza'),
                                ('Petauke', 'Petauke'),
                                ('Nyimba', 'Nyimba'),
                             )
                        ),


                        ('Luapula', (
                        	    ('Mansa', 'Mansa'),
                                ('Nchelenge', 'Nchelenge'),
                                ('Samfya', 'Samfya'),
                                ('Kashikishi', 'Kashikishi'),
                                ('Mbereshi', 'Mbereshi'),
                                ('Kataba', 'Kataba'),
                                ('Kazembe', 'Kazembe'),
                             )
                        ),

                        ('Northern', (
                        	    ('Kasama', 'Kasama'),
                                ('Mbala', 'Mbala'),
                                ('Luwingu', 'Luwingu'),
                                ('Mporkoso', 'Mporokoso'),
                                ('Mpulungu', 'Mpulungu'),
                             )
                        ),

                        ('Muchinga', (
                        	    ('Nakonde', 'Nakonde'),
                                ('Isoka', 'Isoka'),
                                ('Mpika', 'Mpika'),
                                ('Chinsali', 'Chinsali'),
                                ('Mafinga', 'Mafinga'),
                                ('Chama', 'Chama'),
                             )
                        ),


                        ('Western', (
                        	    ('Kaoma', 'Kaoma'),
                                ('Kalabo', 'Kalabo'),
                                ('Mongu', 'Mongu'),
                                ('Mulobezi', 'Mulobezi'),
                                ('Lukulu', 'Lukulu'),
                                ('Sesheke', 'Sesheke'),
                             )
                        ),




                )



	name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}),required=True,max_length=20)
	email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),required=True,max_length=100)
	area=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Area'}),required=True,max_length=100)
	town = forms.ChoiceField(choices=TOWN_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	province = forms.ChoiceField(choices=PROVINCE_OPTIONS, widget=forms.Select(attrs={'class':'form-control'}))
	contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'ContactNumber'}),required=True,max_length=12)
	message=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Message'}),required=True)




#form for contact
class LoginForm(forms.Form):


	username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),required=True,max_length=20)
	email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),required=True,max_length=100)
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),required=True,max_length=100)
	
	
