def translit(texr):
    dict_of_letter = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'ie','ы':'y','ь':'','э':'e',
      'ю':'iu','я':'ia', ' ':' '}
    
    new_text = ''

    texr = str(texr)

    for i in texr:
        if i in dict_of_letter:
            new_text = new_text + dict_of_letter[i]
        elif i.lower() in dict_of_letter:
            new_text = new_text + dict_of_letter[i.lower()]
        # else:
        #     return 'Повтори попытку'   #Не ослилил эту вещь. Когда она активна в элс попадают даже фразы, которые без нее работали нормально
    return new_text.upper()
