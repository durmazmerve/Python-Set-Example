
def islemler(set1, set2):    # set1 ve set2 set veri yapisinda iki degiskendir.
  
        
    set3 = set1.union(set2) #iki değişkenin birleşimi, set3 değişkenine atanıyor
    print(len(set3)) #set3 değişkeninin uzunluğunu yazdırılıyor
    set3.add(3.1) #set3 değişkenine sırasıyla, 3.1 sayısı, 'a' karakteri, 56 sayısı ve "merhaba" sözcüğü ekleniyor
    set3.add('a') 
    set3.add(56)
    set3.add('merhaba')
    print(len(set3)) #set3 değişkeninin uzunluğu
    print(len(set3.intersection(set1))) #set3 değişkeni ile set1 değişkenin kesişiminin eleman sayısı ekrana yazdırılır 
    set3.pop() #set3 değişkeninden rastgele iki eleman silinir ve
    set3.pop()
    print(len(set3)) #sonra set3 değişkeninin uzunluğu ekrana yazdırılıyor  