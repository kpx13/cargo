# -*- coding: utf-8 -*-

import models

def get_rates():
    return models.Item.objects.filter(show=True).order_by('sort_parameter')

def get_page(id_):
    try:
        it = models.Item.objects.get(id=id_)
        return {'title': it.name,
                'header_photo': it.header_photo,
                'image': it.image,
                'rules': it.rules
                }
    except:
        return {}

def insert_test_data():
    models.Item.objects.all().delete()
    models.Item(name=u'Грузоперевозки по Москве',
                header_photo='uploads/headers/moscow.jpg',
                header_photo_min='uploads/mini_headers/moscow.jpg',
                image='uploads/photos/inf1.jpg',
                rules=u'Глиссандо, так или иначе, синхронно заканчивает мнимотакт, таким образом конструктивное состояние всей музыкальной ткани или какой-либо из составляющих ее субструктур (в том числе: временнoй, гармонической, динамической, тембровой, темповой) возникает как следствие их выстраивания на основе определенного ряда (модуса).'
                ).save()
    
    models.Item(name=u'Грузоперевозки по регионам',
                header_photo='uploads/headers/region.jpg',
                header_photo_min='uploads/mini_headers/region.jpg',
                image='uploads/photos/inf2.jpg',
                rules=u'Глиссандо, так или иначе, синхронно заканчивает мнимотакт, таким образом конструктивное состояние всей музыкальной ткани или какой-либо из составляющих ее субструктур (в том числе: временнoй, гармонической, динамической, тембровой, темповой) возникает как следствие их выстраивания на основе определенного ряда (модуса).'
                ).save()
                
    models.Item(name=u'Курьерская доставка внутренняя',
                header_photo='uploads/headers/kurier.jpg',
                header_photo_min='uploads/mini_headers/kurier.jpg',
                image='uploads/photos/inf3.jpg',
                rules=u'Глиссандо, так или иначе, синхронно заканчивает мнимотакт, таким образом конструктивное состояние всей музыкальной ткани или какой-либо из составляющих ее субструктур (в том числе: временнoй, гармонической, динамической, тембровой, темповой) возникает как следствие их выстраивания на основе определенного ряда (модуса).'
                ).save()
                
    models.Item(name=u'Курьерская доставка междугородняя',
                header_photo='uploads/headers/inter.jpg',
                header_photo_min='uploads/mini_headers/inter.jpg',
                image='uploads/photos/inf4.jpg',
                rules=u'Глиссандо, так или иначе, синхронно заканчивает мнимотакт, таким образом конструктивное состояние всей музыкальной ткани или какой-либо из составляющих ее субструктур (в том числе: временнoй, гармонической, динамической, тембровой, темповой) возникает как следствие их выстраивания на основе определенного ряда (модуса).'
                ).save()
                
    models.Item(name=u'Доставка для интернет-магазинов',
                header_photo='uploads/headers/intmag.jpg',
                header_photo_min='uploads/mini_headers/intmag.jpg',
                image='uploads/photos/inf5.jpg',
                rules=u'Глиссандо, так или иначе, синхронно заканчивает мнимотакт, таким образом конструктивное состояние всей музыкальной ткани или какой-либо из составляющих ее субструктур (в том числе: временнoй, гармонической, динамической, тембровой, темповой) возникает как следствие их выстраивания на основе определенного ряда (модуса).'
                ).save()
                    