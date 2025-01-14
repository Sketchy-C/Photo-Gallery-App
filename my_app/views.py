from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from django.contrib.auth import logout as auth_logout


def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

image_url_list = [
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/736x/3f/e3/bf/3fe3bf310ea8ce6045077d36342cb79b.jpg',
        'name': 'Lambo1'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/736x/9e/12/a3/9e12a3368e0d4bfadfd6321f1af87218.jpg',
        'name': 'Lambo'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/0c/d2/ed/0cd2ed43dc909a91ffd84ac53fb432b0.jpg',
        'name': 'LamboLogo'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/474x/ed/9d/6d/ed9d6d9a2e671b85e919b645f91b1146.jpg',
        'name': 'Lambo'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/474x/41/f1/80/41f180020583f4122a00a898957bfbdb.jpg',
        'name': 'Jinx2'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/236x/8c/be/81/8cbe813b58d71265c6cb72291837cb0d.jpg',
        'name': 'Jinx'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/736x/83/9c/63/839c63d060b34293f1724c5db036bdbe.jpg',
        'name': 'Afro'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/736x/1a/03/a0/1a03a01fd366f91a0a8dd1d7ed76ab62.jpg',
        'name': 'Black Afro'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/474x/2f/48/38/2f48388777bf2118cf1a5fd116e97c73.jpg',
        'name': 'Grande'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/736x/32/5f/95/325f957d96f82b71ae6d33c82359a7b3.jpg',
        'name': 'girl'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/236x/68/7f/f2/687ff2f977e24c1ee323bd54545aa45f.jpg',
        'name': 'Girl1'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/736x/24/0e/07/240e070199f4434ae0ba8108bcbd4a4f.jpg',
        'name': 'ford'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/474x/d8/2f/06/d82f062b907f5dcb15cdbfa4f8ae9b12.jpg',
        'name': 'anime'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/236x/2f/de/98/2fde98c959b414caa067d09154c8f86b.jpg',
        'name': 'Luffy'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/736x/ef/99/65/ef996542a1bb55c3d4f97928fa198276.jpg',
        'name': 'samsung'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/736x/71/7d/d6/717dd614f20cebc9a4e0e1114252197b.jpg',
        'name': 'TheeSamsung'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/736x/4d/56/c8/4d56c8a58d1cd9f2f6ec32f212a79a7c.jpg',
        'name': 'samsungSet'
    },
    {
        'category': 'gaming',
        'image': 'https://i.pinimg.com/736x/0f/78/9b/0f789bf4abca81e607a9b3a1bf2a3943.jpg',
        'name': 'ps5'
    },
    {
        'category': 'gaming',
        'image': 'https://i.pinimg.com/736x/26/d9/36/26d93645f569616891f841b82de5461f.jpg',
        'name': 'ps5Pro'
    },

    {
        'category': 'person',
        'image': 'https://i.pinimg.com/236x/7c/53/d9/7c53d979df3c284bcac23755113ed4f0.jpg',
        'name': 'Wednesday'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/236x/c1/bc/e9/c1bce9cded6172ce64f42300951342fb.jpg',
        'name': 'Jenna'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/236x/6c/2e/aa/6c2eaaede6703a8c5169aba0416bc244.jpg',
        'name': 'Ariana'
    },
    {
        'category': 'person',
        'image': 'https://media.licdn.com/dms/image/v2/D4D03AQGjBicHKZgAEg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1732409621550?e=1742428800&v=beta&t=jKDLVMZIBsmp8OxhwV4SuSvJQKoj9A1kzAE0ha88low',
        'name': 'Tr'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/236x/d3/52/3c/d3523c4e128906229c46be8a08fdd69e.jpg',
        'name': 'Tyga'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/474x/32/04/5b/32045b14d17c15e9baabeb2b08525673.jpg',
        'name': 'Takeoff'
    },

{
        'category': 'car',
        'image': 'https://i.pinimg.com/474x/89/e0/09/89e0094675e6f147b58193fc6246f29b.jpg',
        'name': 'Maclaren'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/de/5b/f5/de5bf52c5f616b321f3604132875c6e7.jpg',
        'name': 'P1'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/2f/30/17/2f3017654fdd65fb6793bda33195093d.jpg',
        'name': 'Aventador'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/1d/2c/96/1d2c96c5e3a4cba7879bd544ffd6641b.jpg',
        'name': '2_aventador'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/e3/86/ea/e386eada4c591eef8e168ff3bbf2fe81.jpg',
        'name': 'wallpaper'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/f0/db/b3/f0dbb374e67ca986751d9a33141071ac.jpg',
        'name': 'challenger'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/20/eb/f8/20ebf8652a16c3ab504e774a164c17f7.jpg',
        'name': 'challenger_paper'
    },
    {
        'category': 'car',
        'image': 'https://i.pinimg.com/236x/de/43/1d/de431df4993df9c5f8fbe8a6791aa563.jpg',
        'name': 'srt'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/736x/91/08/ff/9108ffa0ed52ce6d57764a52798e769d.jpg',
        'name': 'Afro 3'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/236x/cb/2a/d0/cb2ad0bbc24149758f88797d22b54ab7.jpg',
        'name': 'iphone'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/236x/db/fe/75/dbfe75990174020a7ebf8799999212d8.jpg',
        'name': 'i_logo'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/236x/38/c1/7b/38c17b657fc52cd82c67da0dc15dfa5c.jpg',
        'name': 'zflip'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/236x/25/15/b5/2515b57b9866693ced732187e6e54acf.jpg',
        'name': 'zflip2'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/236x/fe/79/dc/fe79dc00dfebd18030f96a35c04a6114.jpg',
        'name': 'iphoneXM'
    },

    {
        'category': 'gaming',
        'image': 'https://i.pinimg.com/236x/bb/31/ff/bb31ff51478fa2be7b8476f78bdb4d66.jpg',
        'name': 'ps4Pro'
    },
    {
        'category': 'gaming',
        'image': 'https://i.pinimg.com/236x/bc/66/56/bc6656ce8128f7001891ed8a1564d696.jpg',
        'name': 'logos'
    },
    {
        'category': 'gaming',
        'image': 'https://i.pinimg.com/236x/32/0a/60/320a60bdaa449719bdd15f042f40c7e5.jpg',
        'name': 'hoop'
    },
    {
        'category': 'gaming',
        'image': 'https://i.pinimg.com/236x/01/34/4f/01344fd4a5ecc02d2cc80ca1032baef3.jpg',
        'name': 'cards'
    },
    {
        'category': 'gaming',
        'image': 'https://i.pinimg.com/236x/d2/0c/4a/d20c4a6a2953071668fbed22ce754763.jpg',
        'name': 'foot'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/236x/44/db/f3/44dbf3252affe1b050eef4b7ea01c988.jpg',
        'name': 's24'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/474x/57/6e/86/576e8672eba2985142f59f78c499d3c5.jpg',
        'name': 's24ultra'
    },
    {
        'category': 'phone',
        'image': 'https://i.pinimg.com/236x/31/44/f4/3144f49341cba1d45cc296ccf0bd2984.jpg',
        'name': 'sA14'
    },
    {
        'category': 'person',
        'image': 'https://i.pinimg.com/736x/0f/02/89/0f0289ba0876ed9b8ea10bc23a4255e4.jpg',
        'name': 'A guy'
    },

]


def profile(response):
    userDetail = response.user
    pfpImage = 'https://i.pinimg.com/736x/c2/ee/de/c2eede851b10685ff729d0257aca1420.jpg'
    return render(response,'profile.html',{'userDetail':userDetail, 'pfpImage':pfpImage})

def logout(response):
    auth_logout(response)
    return redirect('home')


def homepage(request):
    selected_category = request.GET.get('category', None)

    if selected_category:
        filtered_images = [image for image in image_url_list if image['category'] == selected_category]
    else:
        filtered_images = image_url_list

    grouped_images = list(chunk_list(filtered_images, 4))

    return render(request, 'index.html', {'grouped_images': grouped_images, 'image_url_list': image_url_list})

def image_detail(request, image_id):
    image = next((item for item in image_url_list if item['name'] == image_id), None)
    
    if image is None:
        raise Http404("Image not found")
    
    return render(request, 'image_detail.html', {'image': image})
